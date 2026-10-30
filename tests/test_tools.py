import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from csv_profile import profile
from file_manifest import manifest


class ToolTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def write(self, text, encoding="utf-8"):
        path = self.root / "input.csv"
        path.write_text(text, encoding=encoding)
        return path

    def test_synthetic_expected_statistics(self):
        result = profile(ROOT / "examples/sample.csv")
        self.assertEqual((result["rows_profiled"], result["exact_duplicate_rows"]), (5, 1))
        self.assertEqual(result["columns"][2]["blank_count"], 1)
        self.assertEqual(result["columns"][2]["numeric_sum"], "400")
        self.assertEqual(result["columns"][3]["numeric_sum"], "16")

    def test_decimal_bom_multiline_and_null(self):
        result = profile(self.write('\ufeff값,설명\n0.1,"첫줄\n둘째줄"\n0.2,NA\n,\nNaN,x\nInfinity,y\n'))
        col = result["columns"][0]
        self.assertEqual(col["numeric_sum"], "0.3")
        self.assertEqual((col["blank_count"], col["non_numeric_count"]), (1, 2))
        self.assertEqual(result["rows_profiled"], 5)

    def test_cp949_and_delimiter(self):
        result = profile(self.write("수량;분류\n2;가\n", "cp949"), "cp949", ";")
        self.assertEqual(result["columns"][0]["numeric_sum"], "2")

    def test_truncation_and_exact_boundary(self):
        path = self.write("x\n1\n2\n3\n")
        self.assertTrue(profile(path, max_rows=2)["truncated"])
        self.assertFalse(profile(path, max_rows=3)["truncated"])
        self.assertEqual(profile(path, max_rows=0)["rows_profiled"], 3)

    def test_header_only(self):
        result = profile(self.write("x,y\n"))
        self.assertEqual(result["rows_profiled"], 0)
        self.assertIsNone(result["columns"][0]["numeric_sum"])

    def test_invalid_headers_and_width(self):
        for text in ("", "x,x\n1,2\n", "x,\n1,2\n", "x,y\n1\n"):
            with self.subTest(text=text), self.assertRaises(ValueError):
                profile(self.write(text))

    def test_exact_large_sum(self):
        result = profile(self.write("x\n123456789012345678901234567890\n0.01\n"))
        self.assertEqual(result["columns"][0]["numeric_sum"], "123456789012345678901234567890.01")

    def test_manifest_hash_and_required(self):
        (self.root / "ok.txt").write_bytes(b"abc")
        (self.root / "empty.txt").touch()
        (self.root / ".git").mkdir()
        (self.root / ".git" / "config").write_text("skip")
        result = manifest(self.root, ["ok.txt", "empty.txt", "missing.txt"])
        self.assertEqual(result["file_count"], 2)
        self.assertFalse(result["required_checks_passed"])
        self.assertEqual([x["status"] for x in result["required_checks"]],
                         ["present_nonempty", "empty", "missing_or_skipped"])
        self.assertEqual(next(x for x in result["files"] if x["path"] == "ok.txt")["sha256"],
                         hashlib.sha256(b"abc").hexdigest())

    def test_required_path_escape(self):
        with self.assertRaises(ValueError):
            manifest(self.root, ["../outside.txt"])

    def test_symlink_skip(self):
        (self.root / "target.txt").write_text("local")
        try:
            (self.root / "link.txt").symlink_to(self.root / "target.txt")
        except OSError:
            self.skipTest("symlinks unavailable for this OS account")
        result = manifest(self.root, ["link.txt"])
        self.assertIn("link.txt", result["skipped"])
        self.assertFalse(result["required_checks_passed"])

    def test_cli_utf8_and_codes(self):
        path = self.write("이름,수량\n가,3\n")
        run = subprocess.run([sys.executable, str(ROOT / "tools/csv_profile.py"), str(path)], capture_output=True)
        self.assertEqual(run.returncode, 0)
        self.assertEqual(json.loads(run.stdout.decode("utf-8"))["columns"][0]["name"], "이름")
        run = subprocess.run([sys.executable, str(ROOT / "tools/file_manifest.py"), str(self.root),
                              "--require", "missing.txt"], capture_output=True)
        self.assertEqual(run.returncode, 1)
        run = subprocess.run([sys.executable, str(ROOT / "tools/csv_profile.py"), str(path),
                              "--max-rows", "-1"], capture_output=True)
        self.assertEqual(run.returncode, 2)
        self.assertEqual(run.stdout, b"")


if __name__ == "__main__":
    unittest.main()

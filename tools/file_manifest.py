#!/usr/bin/env python3
"""Hash a local output folder and check required non-empty files. No uploads."""
import argparse
import hashlib
import json
import os
import stat
import sys
from pathlib import Path

SKIP_DIRS = {".git", ".venv", "__pycache__", "node_modules"}


def is_link(path):
    # Windows junctions are reparse points, including on Python 3.10/3.11.
    attributes = getattr(path.lstat(), "st_file_attributes", 0)
    return path.is_symlink() or bool(attributes & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0))


def manifest(root, required=()):
    root = Path(root).resolve(strict=True)
    if not root.is_dir():
        raise ValueError("root must be a directory")
    requirements = []
    for name in required:
        relative = Path(name)
        if relative.is_absolute() or ".." in relative.parts or not relative.parts:
            raise ValueError("required files must be relative paths inside root")
        candidate = root / relative
        if not candidate.resolve().is_relative_to(root):
            raise ValueError("required path escapes root")
        requirements.append(relative.as_posix())
    files, skipped = [], []
    for current, dirs, names in os.walk(root, followlinks=False):
        folder = Path(current)
        kept = []
        for name in sorted(dirs):
            path = folder / name
            if name in SKIP_DIRS or is_link(path) or not path.resolve().is_relative_to(root):
                skipped.append(path.relative_to(root).as_posix() + "/")
            else:
                kept.append(name)
        dirs[:] = kept
        for name in sorted(names):
            path = folder / name
            relative = path.relative_to(root).as_posix()
            if is_link(path) or not path.resolve().is_relative_to(root) or not path.is_file():
                skipped.append(relative)
                continue
            digest = hashlib.sha256()
            before = path.stat()
            size = 0
            with path.open("rb") as handle:
                for chunk in iter(lambda: handle.read(1024 * 1024), b""):
                    size += len(chunk)
                    digest.update(chunk)
            after = path.stat()
            if (before.st_size, before.st_mtime_ns) != (after.st_size, after.st_mtime_ns) or size != after.st_size:
                raise ValueError(f"file changed during scan: {relative}")
            files.append({"path": relative, "bytes": size, "sha256": digest.hexdigest()})
    files.sort(key=lambda item: item["path"])
    index = {item["path"]: item for item in files}
    checks = [{"path": name, "status": "missing_or_skipped" if name not in index else
               ("empty" if index[name]["bytes"] == 0 else "present_nonempty")}
              for name in requirements]
    return {"schema_version": 1, "file_count": len(files), "files": files,
            "empty_files": [item["path"] for item in files if item["bytes"] == 0],
            "skipped": sorted(skipped), "required_checks": checks,
            "required_checks_passed": all(item["status"] == "present_nonempty" for item in checks),
            "scope": "Existence, byte size and SHA-256 only; content correctness and visual quality are not checked."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path)
    parser.add_argument("--require", action="append", default=[], metavar="RELATIVE_FILE")
    args = parser.parse_args()
    try:
        result = manifest(args.root, args.require)
    except (OSError, ValueError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["required_checks_passed"] else 1


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())

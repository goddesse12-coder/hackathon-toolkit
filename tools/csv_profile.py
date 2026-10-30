#!/usr/bin/env python3
"""Profile a local CSV without dependencies, mutation, or network access."""
import argparse
import csv
import hashlib
import json
import sys
from decimal import Decimal, InvalidOperation, localcontext
from pathlib import Path


def profile(path, encoding="utf-8-sig", delimiter=",", max_rows=100000):
    if len(delimiter) != 1 or delimiter in "\r\n\0":
        raise ValueError("delimiter must be one non-newline character")
    if max_rows < 0:
        raise ValueError("max_rows must be >= 0 (0 means all rows)")
    path = Path(path)
    with path.open("r", encoding=encoding, newline="") as handle:
        reader = csv.reader(handle, delimiter=delimiter, strict=True)
        header = next(reader, None)
        if not header or any(not name.strip() for name in header):
            raise ValueError("CSV must have a non-empty header without blank names")
        if len(set(header)) != len(header):
            raise ValueError("duplicate column names; resolve ambiguity first")
        columns = [dict(name=name, blank=0, numeric=0, non_numeric=0,
                        minimum=None, maximum=None, total=Decimal(0)) for name in header]
        seen, rows, duplicates, truncated = set(), 0, 0, False
        for row in reader:
            if not row:  # csv.reader returns [] for an empty physical record
                continue
            if max_rows and rows >= max_rows:
                truncated = True
                break
            if len(row) != len(header):
                raise ValueError(f"record ending on line {reader.line_num}: "
                                 f"expected {len(header)} fields, got {len(row)}")
            rows += 1
            digest = hashlib.sha256(json.dumps(row, ensure_ascii=False).encode("utf-8")).digest()
            duplicates += digest in seen
            seen.add(digest)
            for col, raw in zip(columns, row):
                value = raw.strip()
                if not value:
                    col["blank"] += 1
                    continue
                try:
                    number = Decimal(value)
                except InvalidOperation:
                    number = None
                if number is None or not number.is_finite():
                    col["non_numeric"] += 1
                    continue
                col["numeric"] += 1
                col["minimum"] = number if col["minimum"] is None else min(col["minimum"], number)
                col["maximum"] = number if col["maximum"] is None else max(col["maximum"], number)
                # Increase precision enough for an exact sum of the two decimals.
                a = col["total"]
                with localcontext() as context:
                    context.prec = max(28, max(a.adjusted(), number.adjusted()) -
                                       min(a.as_tuple().exponent, number.as_tuple().exponent) + 3)
                    # Guard against pathological exponents producing huge allocations.
                    if context.prec > 10000:
                        raise ValueError("numeric exponent range exceeds supported 10000-digit sum")
                    col["total"] = a + number
        output_columns = []
        for col in columns:
            output_columns.append({
                "name": col["name"], "blank_count": col["blank"],
                "numeric_count": col["numeric"], "non_numeric_count": col["non_numeric"],
                "numeric_min": str(col["minimum"]) if col["numeric"] else None,
                "numeric_max": str(col["maximum"]) if col["numeric"] else None,
                "numeric_sum": str(col["total"]) if col["numeric"] else None,
            })
        return {"schema_version": 1, "file_name": path.name, "encoding": encoding,
                "delimiter": delimiter, "rows_profiled": rows, "truncated": truncated,
                "max_rows": max_rows, "exact_duplicate_rows": duplicates,
                "columns": output_columns,
                "notes": ["Statistics describe only rows_profiled, not unseen rows.",
                          "Blank means empty or whitespace; NA/NULL are not automatically missing.",
                          "Numeric-looking identifiers are not automatically measures.",
                          "Blank physical records are skipped. No raw cell samples are emitted."]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path)
    parser.add_argument("--encoding", default="utf-8-sig")
    parser.add_argument("--delimiter", default=",")
    parser.add_argument("--max-rows", type=int, default=100000,
                        help="profile at most this many rows; 0 reads all, with memory proportional to unique rows")
    args = parser.parse_args()
    try:
        result = profile(args.path, args.encoding, args.delimiter, args.max_rows)
    except (OSError, UnicodeError, LookupError, ValueError, csv.Error, ArithmeticError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())

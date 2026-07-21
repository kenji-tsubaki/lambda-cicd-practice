import csv
import sys

csv_path = "csv/sample.csv"
expected_header = ["name", "age"]

with open(csv_path, encoding="utf-8") as file:
    reader = csv.reader(file)

    try:
        actual_header = next(reader)
    except StopIteration:
        print(f"ERROR: {csv_path} is empty.")
        sys.exit(1)

if actual_header != expected_header:
    print(f"ERROR: Invalid CSV header.")
    print(f"  File:     {csv_path}")
    print(f"  Expected: {expected_header}")
    print(f"  Actual:   {actual_header}")
    sys.exit(1)

print(f"OK: {csv_path}")
print(f"Header: {actual_header}")

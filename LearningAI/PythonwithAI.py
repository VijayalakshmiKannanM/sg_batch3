# file_handling_demo.py
"""
File handling demo:
- Write, append, read text files
- Use with-statement (context manager)
- Read lines, iterate, and exception handling
- Work with CSV and JSON
- Safe path handling (cross-platform)
"""

import os
import csv
import json
from pathlib import Path

# ------------- Setup paths -------------
base_dir = Path(__file__).parent  # folder where this script lives
txt_path = base_dir / "notebook.txt"
csv_path = base_dir / "people.csv"
json_path = base_dir / "data.json"

# ------------- 1. Write text (overwrite) -------------
print("1) Writing notebook.txt (overwrite)...")
with open(txt_path, "w", encoding="utf-8") as f:
    f.write("Line 1: Hello, this is notebook.txt\n")
    f.write("Line 2: File handling demo\n")

print("   Written:", txt_path)

# ------------- 2. Append text -------------
print("2) Appending another line...")
with open(txt_path, "a", encoding="utf-8") as f:
    f.write("Line 3: Appended by script\n")

# ------------- 3. Read whole file -------------
print("3) Reading whole file content:")
with open(txt_path, "r", encoding="utf-8") as f:
    content = f.read()
print("----- file content -----")
print(content.strip())
print("------------------------")

# ------------- 4. Read line-by-line -------------
print("4) Reading line-by-line:")
with open(txt_path, "r", encoding="utf-8") as f:
    for i, line in enumerate(f, start=1):
        print(f"  Line {i}: {line.strip()}")

# ------------- 5. Safe file existence check and error handling -------------
print("5) Safe open with existence check:")
if txt_path.exists():
    try:
        with open(txt_path, "r", encoding="utf-8") as f:
            _ = f.readline()  # just read one line
        print("   notebook.txt exists and is readable.")
    except Exception as e:
        print("   Error reading notebook.txt:", e)
else:
    print("   notebook.txt does NOT exist (unexpected).")

# ------------- 6. Write and read CSV -------------
print("6) Writing people.csv and reading it back...")
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35},
]

# write CSV
with open(csv_path, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=["name", "age"])
    writer.writeheader()
    for p in people:
        writer.writerow(p)

# read CSV
with open(csv_path, "r", newline="", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    rows = list(reader)
print("   CSV rows read:", rows)

# ------------- 7. Write and read JSON -------------
print("7) Writing data.json and reading it back...")
data = {
    "title": "Demo",
    "count": len(people),
    "people": people
}

with open(json_path, "w", encoding="utf-8") as jf:
    json.dump(data, jf, indent=2)

with open(json_path, "r", encoding="utf-8") as jf:
    loaded = json.load(jf)
print("   JSON loaded:", loaded)

# ------------- 8. Clean up? (commented out) -------------
# If you want the script to remove created files after demo, uncomment:
# for p in (txt_path, csv_path, json_path):
#     if p.exists():
#         p.unlink()
#         print("Removed:", p)

print("\nDemo complete. Files created:")
for p in (txt_path, csv_path, json_path):
    print(" -", p)

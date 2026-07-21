import csv

with open("csv/sample.csv", encoding="utf-8") as f:
    reader = csv.reader(f)

    header = next(reader)

    if header != ["name", "age"]:
        raise Exception("Header Error")

print("CSV OK!")

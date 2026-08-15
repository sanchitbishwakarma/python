import csv
import json

FILE = "students.csv"
NEW_FILE = "passed_student.json"

passed_student = []

with open(FILE, "r") as file:
    readWala = csv.DictReader(file)
    for row in readWala:
        name = row.get("name")
        marks = int(row.get("marks"))

        if marks >= 45:
            passed_student.append(
                {
                    "name": name,
                    "marks": marks,
                }
            )

with open(NEW_FILE, "w") as file:
    json.dump(passed_student, file)

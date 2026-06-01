import csv
import json

filePath = "./db/students.csv"
topStudentFilePath = "./db/top_students.json"

top_students = []

with open(filePath, "r") as file:
    reader = csv.reader(file)
    for row in reader:
        name, age, score = row
        if int(score) > 80:
            print(f"Student: {name}")
            top_students.append({
                "Name": name,
                "Age": int(age),
                "Score": int(score)
            })
            
with open(topStudentFilePath, "w") as file:
    json.dump(top_students, file, indent=4)
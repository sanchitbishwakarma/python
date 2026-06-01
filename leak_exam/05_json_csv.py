import csv
import json

filePath = "./db/students.csv"

with open(filePath, "r") as file:
    reader = csv.reader(file)
    for row in reader:
        name, age, score = row
        if int(score) > 80:
            print(f"Student: {name}")
       
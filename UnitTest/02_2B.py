import csv
import json

students = {
    "Arav": 85,
    "Diya":92,
    "Kabir": 47,
    "Meera": 73,
    "Rohan": 92,
    "Sita": 38,
    "San": 75
}

#1
high = 0
top_students = []

for name, marks in students.items():
    if marks > high:
        top_students = []
        high = marks
        top_students.append(name)
    elif marks == high:
        top_students.append(name)
print(top_students)

#2
newStudents = students.copy()
for name, marks in students.items():
    if marks < 40:
        newStudents.pop(name)
print(newStudents)

#3
stds = {}
for name, marks in students.items():
    if marks >= 75:
        stds[name] = marks
print(stds)

#4
i = 0
total = 0
for name, marks in newStudents.items():
    total += marks
    i += 1    
print(f"Average: {total/i}")
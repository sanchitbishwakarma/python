import json
import csv

high = 0
high_salary = []


with open("employees.json", "r") as file:
    content = json.load(file)
    for data in content:
        salary = data.get("salary")
        
        if salary > high:
           high = salary
    else:
        high_salary.append(data)

fields = ["name", "department", "salary"]

with open("top_earner.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()
    writer.writerows(high_salary)
    
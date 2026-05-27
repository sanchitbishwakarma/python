import csv

with open("D:\\Python\\database\\users.csv", 'r') as file:
    # data = csv.reader(file)
    data = csv.DictReader(file) # gives the list of dict
    # print(data)
    for row in data:
        print(f"\'{row.get("Name")}\' roll number is {row.get("RollNo")}")
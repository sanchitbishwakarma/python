import csv

data = [
    ["Name", "RollNo"],
    ["Alice", "101"],
    ["Bob", "102"],
    ["Charlie", "103"],
    ["Sanchit", "104"]
]
with open("D:\\Python\\database\\dbWrite.csv", 'w') as file:
    writer = csv.writer(file)
    writer.writerow(data)
    # for x in data:
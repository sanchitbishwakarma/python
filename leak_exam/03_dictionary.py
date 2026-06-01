students = {
    "Jetha": 70,
    "Tarak": 76,
    "AtmaRam": 95,
}

def showAll():
    for name, marks in students.items():
        print(name, marks)
showAll()

search_name = input("\nEnter student's name: ")
print("Marks:", students.get(search_name, "Student not found"))

print("\nStudents scoring more than 75:")
for name, marks in students.items():
    if marks > 75:
        print(name)
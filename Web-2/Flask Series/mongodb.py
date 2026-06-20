from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["college"]

students = db["students"]

students.insert_one({
    "student_id": 101,
    "name": "Ram",
    "age": 20,
    "dept_id": 1
})

for student in students.find():
    print(student)
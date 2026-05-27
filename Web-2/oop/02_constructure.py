class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Hi, I am {self.name} and I am {self.age} years old.")

s1 = Student("Shital", 20)
s2 = Student("Shital 2", 21)

s1.greet()
s2.greet()
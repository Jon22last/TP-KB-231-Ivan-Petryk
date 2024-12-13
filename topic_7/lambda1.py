#Список обєктів класу, сортування з lambda
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"{self.name} (Age: {self.age})"

students = [
    Student("Alice", 22),
    Student("Bob", 20),
    Student("Dima", 23),
    Student("Dina", 21)
]

students_sorted_by_age = sorted(students, key=lambda student: student.age)
print("Sorted by Age:", students_sorted_by_age)
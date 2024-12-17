import csv
from student import Student

class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def load(self):
        students = []
        try:
            with open(self.filename, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    students.append(Student.from_dict(row))
        except FileNotFoundError:
            print(f"File {self.filename} not found. Starting with an empty list.")
        return students

    def save(self, students):
        with open(self.filename, mode='w', encoding='utf-8', newline='') as file:
            fieldnames = ["name", "phone", "email", "group"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows([student.to_dict() for student in students])

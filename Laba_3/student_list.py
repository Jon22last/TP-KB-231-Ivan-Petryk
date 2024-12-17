from student import Student

class StudentList:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        self.students.sort(key=lambda x: x.name)

    def delete_student(self, name):
        for student in self.students:
            if student.name == name:
                self.students.remove(student)
                return True
        return False

    def update_student(self, name, phone=None, email=None, group=None):
        for student in self.students:
            if student.name == name:
                if phone:
                    student.phone = phone
                if email:
                    student.email = email
                if group:
                    student.group = group
                return True
        return False

    def find_student(self, name):
        for student in self.students:
            if student.name == name:
                return student
        return None

    def print_all(self):
        for student in self.students:
            print(student)

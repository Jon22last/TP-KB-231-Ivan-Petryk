import unittest
from student import Student
from student_list import StudentList
from utils import FileManager

class TestStudentManagement(unittest.TestCase):

    def setUp(self):
        self.student_list = StudentList()
        self.student_list.add_student(Student("Alice", "123456789", "alice@example.com", "CS231"))
        self.student_list.add_student(Student("Bob", "987654321", "bob@example.com", "CS231"))

    def test_add_student(self):
        new_student = Student("Charlie", "555555555", "charlie@example.com", "CS231")
        self.student_list.add_student(new_student)
        self.assertEqual(len(self.student_list.students), 3)
        self.assertEqual(self.student_list.students[2].name, "Charlie")

    def test_update_student(self):
        self.student_list.update_student("Alice", phone="111111111", email="alice_new@example.com")
        student = self.student_list.find_student("Alice")
        self.assertEqual(student.phone, "111111111")
        self.assertEqual(student.email, "alice_new@example.com")

    def test_delete_student(self):
        self.student_list.delete_student("Bob")
        self.assertEqual(len(self.student_list.students), 1)
        self.assertIsNone(self.student_list.find_student("Bob"))

    def test_find_student(self):
        student = self.student_list.find_student("Alice")
        self.assertIsNotNone(student)
        self.assertEqual(student.name, "Alice")

    def test_save_and_load(self):
        file_name = "test_students.csv"
        FileManager.save_to_csv(self.student_list, file_name)

        loaded_list = StudentList()
        FileManager.load_from_csv(loaded_list, file_name)

        self.assertEqual(len(loaded_list.students), 2)
        self.assertEqual(loaded_list.students[0].name, "Alice")
        self.assertEqual(loaded_list.students[1].name, "Bob")

if __name__ == "__main__":
    unittest.main()

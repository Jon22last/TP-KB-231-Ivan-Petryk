import unittest
from student import Student
from student_list import StudentList
from utils import FileManager
import os

class TestStudentList(unittest.TestCase):
    def setUp(self):
        self.group = StudentList()
        self.group.add_student(Student("Alice", "123", "alice@example.com", "CS231"))
        self.group.add_student(Student("Bob", "456", "bob@example.com", "CS231"))

    def test_add_student(self):
        self.group.add_student(Student("Charlie", "789", "charlie@example.com", "CS231"))
        self.assertEqual(len(self.group.students), 3)

    def test_delete_student(self):
        self.assertTrue(self.group.delete_student("Alice"))
        self.assertFalse(self.group.delete_student("Nonexistent"))

    def test_update_student(self):
        self.assertTrue(self.group.update_student("Alice", phone="111"))
        self.assertEqual(self.group.find_student("Alice").phone, "111")

class TestFileManager(unittest.TestCase):
    def setUp(self):
        self.filename = "test_students.csv"
        self.file_manager = FileManager(self.filename)
        self.students = [
            Student("Alice", "123", "alice@example.com", "CS231"),
            Student("Bob", "456", "bob@example.com", "CS231")
        ]
        self.file_manager.save(self.students)

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_load(self):
        students = self.file_manager.load()
        self.assertEqual(len(students), 2)
        self.assertEqual(students[0].name, "Alice")

    def test_save(self):
        new_students = [Student("Charlie", "789", "charlie@example.com", "CS231")]
        self.file_manager.save(new_students)
        students = self.file_manager.load()
        self.assertEqual(len(students), 1)

if __name__ == "__main__":
    unittest.main()

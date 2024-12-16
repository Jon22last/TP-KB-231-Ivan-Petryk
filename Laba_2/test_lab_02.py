import unittest
from lab_02 import students, addNewElement, deleteElement, updateElement

class TestStudentDirectory(unittest.TestCase):

    def setUp(self):
        global students
        students.clear()
        students.extend([
            {"name": "Bob", "phone": "0631234567", "email": "bob@example.com", "group": "CS231"},
            {"name": "Emma", "phone": "0637654321", "email": "emma@example.com", "group": "CS231"},
        ])

    def test_add_new_element(self):
        input_data = ["Alice", "0639999999", "alice@example.com", "CS232"]
        with unittest.mock.patch('builtins.input', side_effect=input_data):
            addNewElement()
        self.assertEqual(len(students), 3)
        self.assertEqual(students[0]['name'], "Alice")

    def test_delete_element(self):
        input_data = ["Bob"]
        with unittest.mock.patch('builtins.input', side_effect=input_data):
            deleteElement()
        self.assertEqual(len(students), 1)
        self.assertEqual(students[0]['name'], "Emma")

    def test_update_element(self):
        input_data = ["Emma", "", "emma_new@example.com", ""]
        with unittest.mock.patch('builtins.input', side_effect=input_data):
            updateElement()
        self.assertEqual(students[1]['email'], "emma_new@example.com")

if __name__ == "__main__":
    unittest.main()
import sys
from student_list import StudentList
from utils import FileManager
from student import Student

def main():
    group = StudentList()
    file_manager = FileManager("students.csv")

    group.students = file_manager.load()

    while True:
        print("\nAvailable actions:")
        print("[C] Create, [U] Update, [D] Delete, [P] Print, [X] Exit")
        choice = input("Your choice: ").strip().lower()

        if choice == 'c':
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            group_name = input("Group: ")
            group.add_student(Student(name, phone, email, group_name))
            print("Student added successfully.")

        elif choice == 'u':
            name = input("Name of the student to update: ")
            phone = input("New phone (or press Enter to skip): ")
            email = input("New email (or press Enter to skip): ")
            group_name = input("New group (or press Enter to skip): ")
            if group.update_student(name, phone, email, group_name):
                print("Student updated successfully.")
            else:
                print("Student not found.")

        elif choice == 'd':
            name = input("Name of the student to delete: ")
            if group.delete_student(name):
                print("Student deleted successfully.")
            else:
                print("Student not found.")

        elif choice == 'p':
            print("List of students:")
            group.print_all()

        elif choice == 'x':
            file_manager.save(group.students)
            print("Changes saved. Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()

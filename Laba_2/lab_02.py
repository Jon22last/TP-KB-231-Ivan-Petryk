import csv
import sys

#Початковий список студентів, відсортований за іменами
students = []

#Функція для завантаження початкових даних із CSV файлу
def load_from_csv(data_lab2):
    try:
        with open(data_lab2, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append(row)
        students.sort(key=lambda x: x['name'])  #Сортуємо за іменами
        print(f"Data loaded from {data_lab2}")
    except FileNotFoundError:
        print(f"File {data_lab2} not found. Starting with an empty phonebook.")

#Функція для збереження списку студентів у CSV файл
def save_to_csv(data_lab2):
    with open(data_lab2, mode='w', encoding='utf-8', newline='') as file:
        fieldnames = ["name", "phone", "email", "group"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)
    print(f"Data saved to {data_lab2}")

#Функція для друку списку студентів
def printAllList():
    for elem in students:
        print(f"Name: {elem['name']}, Phone: {elem['phone']}, Email: {elem['email']}, Group: {elem['group']}")

#Функція для додавання нового студента
def addNewElement():
    name = input("Enter student name: ")
    phone = input("Enter student phone: ")
    email = input("Enter student email: ")
    group = input("Enter student group: ")

    newItem = {"name": name, "phone": phone, "email": email, "group": group}

    #Пошук позиції для вставки (щоб список залишався відсортованим)
    insertPosition = 0
    for item in students:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    students.insert(insertPosition, newItem)
    print("New student has been added.")

#Функція для видалення студента
def deleteElement():
    name = input("Enter the name of the student to delete: ")
    deletePosition = -1
    for item in students:
        if name == item["name"]:
            deletePosition = students.index(item)
            break
    if deletePosition == -1:
        print("Student not found.")
    else:
        del students[deletePosition]
        print(f"Student '{name}' has been deleted.")

#Функція для зміни інформації про студента
def updateElement():
    name = input("Enter the name of the student to update: ")
    updatePosition = -1
    for item in students:
        if name == item["name"]:
            updatePosition = students.index(item)
            break
    if updatePosition == -1:
        print("Student not found.")
    else:
        print("Enter new details for the student (leave empty to keep current values):")
        phone = input(f"Current phone ({students[updatePosition]['phone']}): ") or students[updatePosition]["phone"]
        email = input(f"Current email ({students[updatePosition]['email']}): ") or students[updatePosition]["email"]
        group = input(f"Current group ({students[updatePosition]['group']}): ") or students[updatePosition]["group"]

        #Оновлення даних
        students.pop(updatePosition)
        newItem = {"name": name, "phone": phone, "email": email, "group": group}

        #Вставка оновленого елемента у відповідне місце (зберігаємо сортування)
        insertPosition = 0
        for item in students:
            if name > item["name"]:
                insertPosition += 1
            else:
                break
        students.insert(insertPosition, newItem)

        print(f"Student '{name}' has been updated.")

#Основна програма
def main():
    #Завантаження даних із файлу, якщо ім'я файлу передано у командному рядку
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        load_from_csv(file_name)
    else:
        print("No input file specified. Starting with an empty phonebook.")

    while True:
        choice = input("Specify action [C create, U update, D delete, P print, X exit]: ")
        match choice.lower():
            case "c":
                print("Adding a new student...")
                addNewElement()
            case "u":
                print("Updating an existing student...")
                updateElement()
            case "d":
                print("Deleting a student...")
                deleteElement()
            case "p":
                print("Student list:")
                printAllList()
            case "x":
                if len(sys.argv) > 1:
                    save_to_csv(sys.argv[1])
                else:
                    save_to_csv("students.csv")
                print("Exiting the program. Goodbye!")
                break
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
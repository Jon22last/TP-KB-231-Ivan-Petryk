#Початковий список студентів, відсортований за іменами
students = [
    {"name": "Bob", "phone": "0631234567", "email": "bob@example.com", "group": "CS231"},
    {"name": "Emma", "phone": "0637654321", "email": "emma@example.com", "group": "CS231"},
    {"name": "Jon",  "phone": "0639876543", "email": "jon@example.com", "group": "CS231"},
    {"name": "Zak",  "phone": "0635555555", "email": "zak@example.com", "group": "CS231"}
]

#Функція для друку списку студентів
def printAllList():
    for elem in students:
        print(f"Name: {elem['name']}, Phone: {elem['phone']}, Email: {elem['email']}, Group: {elem['group']}")
    return

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
    return

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
    return

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
    return

#Основна програма
def main():
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
                print("Exiting the program. Goodbye!")
                break
            case _:
                print("Invalid choice. Please try again.")

main()

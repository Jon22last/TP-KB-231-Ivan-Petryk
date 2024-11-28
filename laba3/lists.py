#Написати програму тестування функцій списків
def test_list_functions():
    print("Тестуємо функції списків Python")

    # Створення списку
    my_list = [10, 20, 30, 40, 50]
    print(f"Список: {my_list}")

    # Додавання елементів
    my_list.append(60)
    print(f"Після додавання 60: {my_list}")

    # Вставка елемента в конкретне місце
    my_list.insert(2, 25)  # Вставити 25 на позицію 2
    print(f"Після вставки 25 на позицію 2: {my_list}")

    # Видалення елемента за значенням
    my_list.remove(40)
    print(f"Після видалення 40: {my_list}")

    # Видалення останнього елемента
    removed_element = my_list.pop()
    print(f"Після видалення останнього елемента ({removed_element}): {my_list}")

    # Пошук індексу елемента
    index = my_list.index(30)
    print(f"Індекс числа 30: {index}")

    # Перевірка наявності елемента
    is_present = 20 in my_list
    print(f"Чи є 20 у списку? {'Так' if is_present else 'Ні'}")

    # Сортування списку
    my_list.sort()
    print(f"Після сортування: {my_list}")

    # Зворотний порядок списку
    my_list.reverse()
    print(f"Після зворотного порядку: {my_list}")

    # Копіювання списку
    copied_list = my_list.copy()
    print(f"Копія списку: {copied_list}")

    # Очищення списку
    my_list.clear()
    print(f"Після очищення: {my_list}")

# Виклик функції тестування
test_list_functions()
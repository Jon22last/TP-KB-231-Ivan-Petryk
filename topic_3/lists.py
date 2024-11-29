#Написати програму тестування функцій списків
def test_list_functions():
    print("Тестуємо функції списків Python")

    my_list = [10, 20, 30, 40, 50]
    print(f"Список: {my_list}")

    my_list.append(60)
    print(f"Після додавання 60: {my_list}")

    #Вставка елемента в конкретне місце
    my_list.insert(2, 25)  #Вставити 25 на позицію 2
    print(f"Після вставки 25 на позицію 2: {my_list}")

    my_list.remove(40)
    print(f"Після видалення 40: {my_list}")

    removed_element = my_list.pop()
    print(f"Після видалення останнього елемента ({removed_element}): {my_list}")

    index = my_list.index(30)
    print(f"Індекс числа 30: {index}")

    is_present = 20 in my_list
    print(f"Чи є 20 y списку? {'Yes' if is_present else 'No'}")

    my_list.sort()
    print(f"Після сортування: {my_list}")

    my_list.reverse()
    print(f"Після зворотного порядку: {my_list}")

    copied_list = my_list.copy()
    print(f"Копія списку: {copied_list}")

    my_list.clear()
    print(f"Після очищення: {my_list}")

test_list_functions()
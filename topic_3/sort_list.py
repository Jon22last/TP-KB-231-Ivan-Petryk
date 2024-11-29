#Написати функцію пошуку позиції для вставки нового елементу у відсортований список.
def find_insert_position(sorted_list, new_element):

    for i, element in enumerate(sorted_list):
        if new_element <= element:
            return i
    return len(sorted_list)  #Якщо новий елемент більший за всі, вставити в кінець

sorted_list = [1, 3, 5, 7, 9]
new_element = 8
position = find_insert_position(sorted_list, new_element)
print(f"Позиція для вставки {new_element}: {position}")
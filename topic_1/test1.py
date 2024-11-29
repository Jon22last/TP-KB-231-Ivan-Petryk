#Повернути рядок в зворотньому порядку
def reverse_string(a):
    return a[::-1]

original_string = input("Original: ")
reversed_string = reverse_string(original_string)
print("Reversed: ", reversed_string)
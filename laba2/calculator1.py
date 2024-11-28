#Програма калькулятор на основі if elif else
print("Виберіть операцію:")
print("1. Додавання")
print("2. Віднімання")
print("3. Множення")
print("4. Ділення")

choice = input("Введіть номер операції (1/2/3/4): ")

num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))

if choice == "1":
    result = num1 + num2
    print(f"Результат: {num1} + {num2} = {result}")
elif choice == "2":
    result = num1 - num2
    print(f"Результат: {num1} - {num2} = {result}")
elif choice == "3":
    result = num1 * num2
    print(f"Результат: {num1} * {num2} = {result}")
elif choice == "4":
    if num2 != 0:
        result = num1 / num2
        print(f"Результат: {num1} / {num2} = {result}")
    else:
        print("Помилка: ділення на нуль неможливе!")
else:
    print("Невірний вибір операції.")



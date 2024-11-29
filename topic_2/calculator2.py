#Та сама програма калькулятор на основі оператора match
print("Виберіть операцію:")
print("1. Додавання")
print("2. Віднімання")
print("3. Множення")
print("4. Ділення")

choice = input("Введіть номер операції (1/2/3/4): ")

num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))

match choice:
    case "1":
        result = num1 + num2
        print(f"Результат: {num1} + {num2} = {result}")
    case "2":
        result = num1 - num2
        print(f"Результат: {num1} - {num2} = {result}")
    case "3":
        result = num1 * num2
        print(f"Результат: {num1} * {num2} = {result}")
    case "4":
        if num2 != 0:
            result = num1 / num2
            print(f"Результат: {num1} / {num2} = {result}")
        else:
            print("Помилка: ділення на нуль неможливе!")
    case _:
        print("Невірний вибір операції.")
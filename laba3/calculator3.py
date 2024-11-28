#Написати програму калькулятор з постійними запитами на введення нових даних та операцій.
while True:
    print("Виберіть операцію:")
    print("1. Додавання")
    print("2. Віднімання")
    print("3. Множення")
    print("4. Ділення")
    print("5. Вихід")

    choice = input("Введіть номер операції (1/2/3/4/5): ")

    match choice:
        case "1":
            num1 = float(input("Введіть перше число: "))
            num2 = float(input("Введіть друге число: "))
            print(f"Результат: {num1} + {num2} = {num1 + num2}")
        case "2":
            num1 = float(input("Введіть перше число: "))
            num2 = float(input("Введіть друге число: "))
            print(f"Результат: {num1} - {num2} = {num1 - num2}")
        case "3":
            num1 = float(input("Введіть перше число: "))
            num2 = float(input("Введіть друге число: "))
            print(f"Результат: {num1} * {num2} = {num1 * num2}")
        case "4":
            num1 = float(input("Введіть перше число: "))
            num2 = float(input("Введіть друге число: "))
            if num2 != 0:
                print(f"Результат: {num1} / {num2} = {num1 / num2}")
            else:
                print("Помилка: ділення на нуль неможливе!")
        case "5":
            print("Дякуємо за використання калькулятора!")
            break
        case _:
            print("Невірний вибір операції. Спробуйте ще раз.")


#Розширити програму калькулятор функцією запитів від користувача, що обробляє виняткові ситуації
#Розширити функцію ділення обробкою виняткової ситуації ділення но нуль
def calculator():
    print("Вітаю у програмі калькулятора!")
    while True:
        try:
            num1 = input("Введіть перше число (або 'q' для виходу): \n")
            if num1.lower() == 'q':
                print("До побачення!")
                break
            num1 = float(num1)

            operator = input("Введіть оператор (+, -, *, /, або 'q' для виходу): \n")
            if operator.lower() == 'q':
                print("До побачення!")
                break

            num2 = input("Введіть друге число (або 'q' для виходу): \n")
            if num2.lower() == 'q':
                print("До побачення!")
                break
            num2 = float(num2)

            match operator:
                case '+':
                    result = num1 + num2
                case '-':
                    result = num1 - num2
                case '*':
                    result = num1 * num2
                case '/':
                    if num2 == 0:
                        raise ZeroDivisionError("Помилка: ділення на нуль неможливе!")
                    result = num1 / num2
                case _:
                    print("Невідомий оператор. Спробуйте ще раз.")
                    continue

            print(f"Результат: {result}")

        except ValueError:  
            print("Це не число! Спробуйте ще раз.")
        except ZeroDivisionError as e:
            print(e)

calculator()
#Calc with OOP
import os
from datetime import datetime
from interface import get_operation, get_number
from operations import add, subtract, multiply, divide

file_path = os.path.join(os.path.dirname(__file__), "Calc_Log.txt")

def log_operation(a, b, operation, result):
    """Логування операції у файл."""
    with open(file_path, "a") as file:
        log_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{log_time} | {a} {operation} {b} = {result}\n")

def calculator():
    print("Ласкаво просимо до Калькулятора!")
    
    while True:
        operation = get_operation()
        if operation == "ex":
            print("Дякуємо за використання калькулятора!")
            break

        if operation not in ["+", "-", "*", "/"]:
            print("Неправильна операція. Спробуйте ще раз.")
            continue

        a = get_number("Введіть перше число: ")
        b = get_number("Введіть друге число: ")

        try:
            match operation:
                case "+":
                    result = add(a, b)
                case "-":
                    result = subtract(a, b)
                case "*":
                    result = multiply(a, b)
                case "/":
                    result = divide(a, b)

            print(f"Результат: {result}")
            log_operation(a, b, operation, result)
        except ValueError as e:
            print(f"Помилка: {e}")

if __name__ == "__main__":
    calculator()

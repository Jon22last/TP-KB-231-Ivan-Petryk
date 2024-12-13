#calculator5.py - об’єднує функціонал з інших модулів
# calculator.py
from math import add, subtract, multiply, divide
from validation import validate_number, validate_operator

def main():
    print("Вітаю у програмі 'Калькулятор'!")
    while True:
        try:
            num1 = input("Введіть перше число (або 'q' для виходу): ")
            if num1.lower() == 'q':
                print("До побачення!")
                break
            num1 = validate_number(num1)

            operator = input("Введіть оператор (+, -, *, /): ")
            operator = validate_operator(operator)

            num2 = input("Введіть друге число: ")
            num2 = validate_number(num2)

            match operator:
                case '+':
                    result = add(num1, num2)
                case '-':
                    result = subtract(num1, num2)
                case '*':
                    result = multiply(num1, num2)
                case '/':
                    result = divide(num1, num2)
                case _:
                    raise ValueError("Невідомий оператор!")

            print(f"Результат: {result}")

        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()

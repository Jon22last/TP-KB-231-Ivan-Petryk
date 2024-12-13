def get_operation():
    """Запитує у користувача вибір операції."""
    print("\nОберіть операцію: +, -, *, / (або 'ex' для виходу)")
    return input("Операція: ")

def get_number(prompt):
    """Запитує у користувача число."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Це не число. Спробуйте ще раз.")


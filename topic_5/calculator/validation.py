#validation.py - перевіряє ввід користувача
def validate_number(value):
    try:
        return float(value)
    except ValueError:
        raise ValueError("Це не число! Спробуйте ще раз.")

def validate_operator(operator):
    if operator in ['+', '-', '*', '/']:
        return operator
    else:
        raise ValueError("Невідомий оператор. Доступні: +, -, *, /")


def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Ділення на нуль не допускається!"
    return a / b

def rdiv(a, b):
    if a == 0:
        return "Не можна ділити на нуль!"
    return b / a

def deg(a, b):
    return a ** b
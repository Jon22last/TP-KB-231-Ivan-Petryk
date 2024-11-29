#Написати програму тестування функцій словників
def test_animal_dict():
    print("Тестуємо словник з тваринами!")

    animals = {"cat": "кіт", "dog": "пес", "cow": "корова"}
    print(f"Словник: {animals}")

    animals["fox"] = "лисиця"
    print(f"Після додавання лисиці: {animals}")

    animals["dog"] = "собака"
    print(f"Після оновлення 'dog': {animals}")

    animals.pop("cow")
    print(f"Після видалення корови: {animals}")

    print(f"Чи є 'cat' y словнику? {'cat' in animals}")
    print(f"Чи є 'cow' y словнику? {'cow' in animals}")

    print(f"Ключі (тварини англійською): {list(animals.keys())}")
    print(f"Значення (тварини українською): {list(animals.values())}")

test_animal_dict()
#Використання lambda функцій для функції сортування
animals = [
    {"name": "Tiger", "age": 5, "weight": 200},
    {"name": "Elephant", "age": 10, "weight": 5000},
    {"name": "Monkey", "age": 3, "weight": 30},
    {"name": "Dog", "age": 7, "weight": 50},
]

while True:
    criteria = input("Введіть критерій сортування (name, age, weight або 'q' для виходу): ").lower()
    if criteria == "q":
        print("До побачення!")
        break
    if criteria in {"name", "age", "weight"}:
        sorted_animals = sorted(animals, key=lambda x: x[criteria])
        for animal in sorted_animals:
            print(animal)
    else:
        print("Невірний критерій сортування!")
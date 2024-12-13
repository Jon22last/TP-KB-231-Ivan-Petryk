#Гра Камінь Ножиці Папер
import random

def play_game():
    print("Вітаю у грі 'Камінь, Ножиці, Папір'!")
    options = ["камінь", "ножиці", "папір"]

    while True:
        #Вибір гравця
        user_choice = input("Ваш вибір (камінь, ножиці, папір або 'q' для виходу): \n")
        if user_choice == 'q':
            print("Дякуємо за гру!")
            break
        if user_choice not in options:
            print("Неправильний вибір. Спробуйте ще раз.")
            continue

        #Вибір комп'ютера
        computer_choice = random.choice(options)
        print(f"Комп'ютер обрав: {computer_choice}")

        if user_choice == computer_choice:
            print("Нічия!")
        elif (user_choice == "камінь" and computer_choice == "ножиці") or \
             (user_choice == "ножиці" and computer_choice == "папір") or \
             (user_choice == "папір" and computer_choice == "камінь"):
            print("Ви виграли!")
        else:
            print("Ви програли!")

play_game()


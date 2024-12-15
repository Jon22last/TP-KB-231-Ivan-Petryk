#Конвертор валют
import requests

def fetch_exchange_rates(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return {item['cc']: float(item['rate']) for item in data}
    except requests.RequestException as e:
        print(f"Помилка запиту до API: {e}")
        return {}
    except (KeyError, ValueError) as e:
        print(f"Помилка обробки даних: {e}")
        return {}

def convert_currency(amount, from_currency, to_currency, rates):
    try:
        if from_currency == "UAH":
            converted = amount / rates[to_currency]
        elif to_currency == "UAH":
            converted = amount * rates[from_currency]
        else:
            uah_amount = amount * rates[from_currency]
            converted = uah_amount / rates[to_currency]
        return converted
    except KeyError:
        raise ValueError(f"Валюта '{from_currency}' або '{to_currency}' не знайдена!")

def main():
    url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchangenew?json"
    rates = fetch_exchange_rates(url)

    if not rates:
        print("Не вдалося завантажити курси валют.")
        return

    print("Вітаю у Конверторі валют!")
    print("Доступні валюти:", ", ".join(rates.keys()), ", UAH")
    
    while True:
        try:
            amount = float(input("Введіть суму для конвертації: "))
            from_currency = input("Введіть валюту, з якої конвертуємо (наприклад, USD): ").upper()
            to_currency = input("Введіть валюту, в яку конвертуємо (наприклад, EUR): ").upper()

            result = convert_currency(amount, from_currency, to_currency, rates)
            print(f"{amount} {from_currency} = {result:.2f} {to_currency}")

        except ValueError as e:
            print(e)

        cont = input("Бажаєте виконати ще одну конвертацію? (так/ні): ").lower()
        if cont != "так":
            print("Дякуємо за використання конвертора валют!")
            break

main()
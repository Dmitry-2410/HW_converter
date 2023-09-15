from online_requests import get_actual_currencies

CURRENCIES = get_actual_currencies()

def convert(amount, from_currency, to_currency, currencies):
    from_value = currencies.get(from_currency)
    to_value = currencies.get(to_currency)

    coefficient = to_value / from_value
    return round(amount * coefficient, 2)

print('Добро пожаловать в конвертатор валют!')
print("""
Инструкция:
1. Ввести исходную валюту
2. Ввести итоговую валюту
3. Ввести количество валюты
""")

print('Доступные валюты:')

for key in CURRENCIES:
    print(f'* {key}')


current_currency = input('Введите исходную валюту: ').upper()
while not current_currency in CURRENCIES:
    current_currency = input('Введите исходную валюту, которая присутствует в списке: ').upper()
result_currency = input('Введите итоговую валюту: ').upper()
while not result_currency in CURRENCIES:
    result_currency = input('Введите итоговую валюту, которая присутствует в списке: ').upper()
amount = input('Введите количество: ')
while not amount.isdigit():
    amount = input('Введите корректное количество: ')
result = convert(float(amount), current_currency, result_currency, CURRENCIES)

print(f'{amount} {current_currency} = {result} {result_currency}')
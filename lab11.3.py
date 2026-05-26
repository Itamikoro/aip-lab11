import csv

total = 0
print("Нужно купить:")

with open('spisok.csv', 'r', encoding='utf-8') as file:
    read = csv.DictReader(file)
    for i in read:
        product = i['Продукт']
        much = int(i['Количество'])
        price = int(i['Цена'])
        cost = quantity * price
        total += cost
        print(f"{product} - {much} шт. за {price} руб.")

print(f"Итоговая сумма: {total} руб.")

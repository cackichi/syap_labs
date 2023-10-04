# Создать текстовый файл (не программно). Построчно записать
# названия цветов и их стоимость (не менее 10 строк). Вывести на экран все
# цветы дороже 5 рублей. Найти среднюю стоимость всех цветов. Вывести на
# экран все цветы с минимальной стоимостью.
# Пример файла:
# Роза 12
# Гвоздика 5

with open('colors.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
print("Цветы дороже 5 рублей")
for line in lines:
    color, price_str = line.strip().split()
    price = float(price_str)
    if price > 5:
        print(f"{color}: {price} рублей")

print()
total_price = sum(float(line.strip().split()[1]) for line in lines)
average_price = total_price / len(lines)
print(f"Средняя стоимость всех цветов: {average_price:.2f} рублей")

min_price = min(float(line.strip().split()[1]) for line in lines)
min_price_colors = [line.strip().split()[0] for line in lines if float(line.strip().split()[1]) == min_price]

if min_price_colors:
    print("Цветы с минимальной стоимостью:")
    for color in min_price_colors:
        print(color)
else:
    print("Файл пуст.")
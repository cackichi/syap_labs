# Реализуйте программу «Кондитерская», которая будет включать
# в себя шесть пунктов меню. У вас есть словарь, где ключ – название
# продукции (торт, пирожное, маффин и т.д.). Значение – список,
# который содержит состав, цену (за 100гр) и кол-во (в граммах).
# 1. Просмотр описания: название – описание
# 2. Просмотр цены: название – цена.
# 3. Просмотр количества: название – количество.
# 4. Всю информацию.
# 5. Покупка
# В пункте «Покупка» необходимо совершить покупку, с
# клавиатуры вводите название продукции и его кол-во, n – выход из
# программы. Посчитать цену выбранных товаров и сколько товаров
# осталось в изначальном списке
# 6. До свидания

menu = {
    "торт": ["Состав: шоколад, сливки, ягоды", "Цена: 6 бел.руб/100г", "Количество: 500 г"],
    "пирожное": ["Состав: песочное тесто, взбитые сливки, фрукты", "Цена: 5 бел.руб/100г", "Количество: 300 г"],
    "маффин": ["Состав: мука, сахар, яйца, масло", "Цена: 3 бел.руб/100г", "Количество: 200 г"],
    "печенье": ["Состав: мука, сахар, масло", "Цена: 2 бел.руб/100г", "Количество: 400 г"],
    "эклер": ["Состав: заварное тесто, крем, шоколадная глазурь", "Цена: 4 бел.руб/100г", "Количество: 250 г"],
    "шоколадка": ["Состав: шоколад, орехи, сухофрукты", "Цена: 3 бел.руб/100г", "Количество: 350 г"]
}
basket = {}
def display_description():
    for product in menu:
        print(product, "-", menu[product][0])

def display_price():
    for product in menu:
        print(product, "-", menu[product][1])

def display_amount():
    for product in menu:
        print(product, "-", menu[product][2])

def display_all():
    for product in menu:
        print(product)
        print(menu[product][0])
        print(menu[product][1])
        print(menu[product][2])
        print()

def buy_product():
    total_price = 0
    while True:
        product = input("Введите название продукции (или 'q' для выхода): ")
        if product == "q":
            break
        if product not in menu:
            print("Такой продукции нет в меню")
            continue
        amount = int(input("Введите количество (в граммах): "))
        if amount > int(menu[product][2].split()[1]):
            print("Недостаточно товара на складе")
            continue
        if amount <= 0:
            print("Введите положительное значение")
            continue
        price_per_100g = int(menu[product][1].split()[1])
        price = price_per_100g * amount / 100
        total_price += price
        menu[product][2] = menu[product][2].split()[0] + " " + str(int(menu[product][2].split()[1]) - amount) + " г"
        basket[product] = [str(amount) + " г", menu[product][1].split()[1] + " бел.руб"]
    print("Корзина:")
    display_basket()
    print("Общая цена покупки:", total_price, " бел.руб")
    print("Остаток товара:")
    display_amount()

def display_basket():
    basket_price = 0
    for product in basket:
        print(product, basket[product])
        basket_price += int(basket[product][1].split()[0])
    print("Стоимость корзины: ", basket_price, " бел.руб")

def display_menu():
    print("\nМеню:")
    print("1. Просмотр описания")
    print("2. Просмотр цены")
    print("3. Просмотр количества")
    print("4. Вся информация")
    print("5. Покупка")
    print("6. Просмотреть корзину")
    print("7. До свидания")

display_all()

while True:
    display_menu()
    choice = input("Выберите пункт меню: ")
    print()
    if choice == "1":
        display_description()
    elif choice == "2":
        display_price()
    elif choice == "3":
        display_amount()
    elif choice == "4":
        display_all()
    elif choice == "5":
        buy_product()
    elif choice == "6":
        display_basket()
    elif choice == "7":
        print("До свидания!")
        break
    else:
        print("Некорректный выбор пункта меню")
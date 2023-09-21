# Написать функцию ,которая определяет код года по китайскому
# календарю, ввод данных закончить, когда пользователь ввел 0. Сделать
# проверку на правильность введенных данных

def chinese_zodiac():
    while True:
        year = input("Введите год (для выхода введите 0): ")
        if year == '0':
            break
        elif not year.isdigit():
            print("Ошибка! Введите число.")
            continue
        else:
            year = int(year)
            if year < 0:
                print("Ошибка! Год должен быть положительным числом.")
                continue
            zodiac_code = (year - 1900) % 12
            zodiac_animal = ""
            if zodiac_code == 0:
                zodiac_animal = "Крыса"
            elif zodiac_code == 1:
                zodiac_animal = "Бык"
            elif zodiac_code == 2:
                zodiac_animal = "Тигр"
            elif zodiac_code == 3:
                zodiac_animal = "Кролик"
            elif zodiac_code == 4:
                zodiac_animal = "Дракон"
            elif zodiac_code == 5:
                zodiac_animal = "Змея"
            elif zodiac_code == 6:
                zodiac_animal = "Лошадь"
            elif zodiac_code == 7:
                zodiac_animal = "Овца"
            elif zodiac_code == 8:
                zodiac_animal = "Обезьяна"
            elif zodiac_code == 9:
                zodiac_animal = "Петух"
            elif zodiac_code == 10:
                zodiac_animal = "Собака"
            elif zodiac_code == 11:
                zodiac_animal = "Свинья"
            print("Код года по китайскому календарю:", zodiac_code)
            print("Животное года:", zodiac_animal)

chinese_zodiac()
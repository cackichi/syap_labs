#  Напишите функцию, которая будет принимать один аргумент. Если
# в функцию передаётся список, удалить все отрицательные элементы. Найти
# в новом списке сумму после первого нулевого элемента.
# Если кортеж, найти максимальный и минимальный элементы.
# Поменять их местами.
# Число – найти сумму нечетных цифр.
# Строка – подсчитывает количество слов, которые имеют четную
# длину.
# Сделать проверку со всеми этими случаями.

def process_data(data):
    if isinstance(data, list):
        print("Список до: ", data)
        data = [num for num in data if num >= 0]
        print("Список после: ", data)
        if 0 in data:
            sum_after_zero = 0
            for i in range(data.index(0), len(data)):
                sum_after_zero += data[i]
            print("Сумма после первого нулевого элемента:", sum_after_zero)
        else:
            print("В списке нет нулевых элементов.")
    elif isinstance(data, tuple):
        print("\nКортеж до: ", data)
        min_element = min(data)
        max_element = max(data)
        l = list(data)
        temp = l[l.index(min_element)]
        l[l.index(min_element)] = l[l.index(max_element)]
        l[l.index(max_element)] = temp
        data = tuple(l)
        print("Кортеж после: ", data)
        swapped_tuple = (max_element, min_element)
        print("Максимальный элемент:", max_element)
        print("Минимальный элемент:", min_element)
        print("Поменянные местами элементы:", swapped_tuple)
        print()
    elif isinstance(data, int):
        print("Число: ", data)
        summ = 0
        for digit in str(data):
            if int(digit) % 2 != 0:
                summ += int(digit)
        print("Сумма нечетных цифр:", summ)
        print()
    elif isinstance(data, str):
        print("Строка: ", data)
        words = data.split()
        count = 0
        for i in range(0,len(words)):
            if len(words[i]) % 2 == 0:
                count += 1
        print("Количество слов с четной длиной:", count)
    else:
        print("Неподдерживаемый тип данных.")


process_data([1, -2, 3, -4, 5, 0, 6])
process_data((10, 5, 3, 8))
process_data(123456789)
process_data("Привет мой любимый мир")

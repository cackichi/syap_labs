# Напишите программу, демонстрирующую работу try\except\finally

try:
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    result = num1 / num2
    print("Результат деления:", result)
except ValueError:
    print("Ошибка: введено некорректное значение")
except ZeroDivisionError:
    print("Ошибка: деление на ноль")
finally:
    print("Программа завершена")
# Дано натуральное число. Напишите программу, которая
# определяет, является ли последовательность его цифр при просмотре
# справа налево упорядоченной по убыванию.

num = input("Введите натуральное число: ")
flag = False
for i in range(len(num) - 1, -1, -1):
    print(num[i])
    if int(num[i]) < int(num[i-1]):
        flag = True
    else:
        flag = False
if(flag):
    print("Последовательность есть")
else:
    print("Последовательности нет")
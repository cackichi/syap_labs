num = input("Введите натуральное число: ")
flag = True
for i in range(0, len(num) - 1):
    if int(num[i]) < int(num[i+1]):
        flag = False
if(flag):
    print("Последовательность есть")
else:
    print("Последовательности нет")
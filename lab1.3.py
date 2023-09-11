list = []
positive_sum = 0
call = 0
after_zero_sum = 0
zero_index = -1
print("Заполните список")
while True:
    num = input("Введите число (для завершения введите 'q'): ")
    if num == 'q':
        break
    list.append(int(num))

for i in range(0, len(list)):
    if list[i] > 0:
        positive_sum += list[i]
    if call == 0 and list[i] == 0:
        zero_index = i
        call += 1

if zero_index != -1:
    for i in range(zero_index, len(list)):
        after_zero_sum += list[i]
    print("Сумма элементов после первого нуля:", after_zero_sum)
else:
    print("Сумму после нуля посчитать нельзя, так как его нет в списке")

call = 0
while call < len(list):
    if(list[call] < 0):
        list.pop(call)
        call -= 1
    call += 1

print("Сумма положительных элементов:", positive_sum)
print("Список после удаления отрицательных элементов:", list)

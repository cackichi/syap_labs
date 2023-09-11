numbers = (-2, 5, -7, 10, -3, 0, 8)

positive_count = 0

for num in numbers:
    if num > 0:
        positive_count += 1

print("Количество положительных элементов:", positive_count)
sequence = "012345678934265198651289340912384"

# Создаем пустой словарь
count_dict = {}

for num in sequence:
    num = int(num)
    count_dict[num] = count_dict.get(num, 0) + 1

print(count_dict)

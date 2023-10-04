# Посчитать, сколько пар (стоят рядом) верхнего и нижнего
# регистра находится в веденном с клавиатуры слове. (Пример HjkLM- 1
# пара нижнего, 1 пара верхнего), а также сколько гласных букв в слове.

word = input("Введите слово: ")
upper_pairs = 0
lower_pairs = 0
vowels = 0
i = 0

while i < len(word):
    if word[i].islower() and word[i + 1].islower():
        lower_pairs += 1
        i += 1
    elif word[i].isupper() and word[i + 1].isupper():
        upper_pairs += 1
        i += 1
    i += 1

for i in range(len(word) - 1):
    if word[i].lower() in "aeiuoуеыаоэяию":
        vowels += 1

print("Количество пар верхнего регистра: ", upper_pairs)
print("Количество пар нижнего регистра: ", lower_pairs)
print("Количество гласных: ", vowels)
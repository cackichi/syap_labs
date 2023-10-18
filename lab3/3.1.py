# Создать программный файл F1 в текстовом формате, записать в него
# построчно данные, вводимые пользователем. Об окончании ввода данных
# будет свидетельствовать пустая строка. Скопировать из файла F1 в файл F2
# все строки, в которых нет слов, совпадающих с первым словом. Определить
# количество согласных букв в первой строке файла F2.

with open('F1.txt', 'w') as f1:
    print("Введите данные для записи в файл F1 (для окончания ввода введите пустую строку):")

    while True:
        line = input()
        if not line:
            break
        f1.write(line + '\n')

with open('F1.txt', 'r') as f1, open('F2.txt', 'w') as f2:
    first_line = f1.readline()

    first_words = first_line.split()
    consonants_count = 0
    for char in first_line:
        if char.isalpha() and char.lower() not in 'aeiouуеыаоэяию':
            consonants_count += 1

    if not first_line.strip():
        f2.write(first_line)

    for line in f1:
        if not any(word in line.split() for word in first_words):
            f2.write(line)

print(f"Количество согласных букв в первой строке файла F2: {consonants_count}")

# Сформировать (не программно) текстовый файл. В нём каждая
# строка должна описывать учебный предмет и наличие лекционных,
# практических и лабораторных занятий по предмету. Сюда должно входить и
# количество занятий. Необязательно, чтобы для каждого предмета были все
# типы занятий.
# Сформировать словарь, содержащий название предмета и общее
# количество занятий по нему. Вывести его на экран.
# Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
#  Физика: 30(л) 10(лаб)
#  Физкультура: 30(пр)
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”:
# 30}

lessons_dict = {}

with open('lessons.txt', 'r', encoding='utf-8') as file:
    for line in file:
        parts = line.strip().split(': ')
        if len(parts) == 2:
            subject, details = parts
            lesson_parts = details.split()
            total_lessons = 0
            for lesson_part in lesson_parts:
                if lesson_part.endswith('(л)') or lesson_part.endswith('(пр)') or lesson_part.endswith('(лаб)'):
                    lesson_count = int(lesson_part.split('(')[0])  # Разделяем число и скобку и берем число
                    total_lessons += lesson_count

            lessons_dict[subject] = total_lessons

print(lessons_dict)





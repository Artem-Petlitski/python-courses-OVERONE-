# Задание 1. В файле записан текст, определить какое слово встречается чаще всего.

with open("input[1].txt", "r", encoding="utf-8") as file:
    lst = [word if word[-1].isalpha() else word[:-1] for line in file for word in line.strip().split()]
    print(lst)
    max_word = lst[0]
    length = lst.count(max_word)
    for word in lst:
        if lst.count(word) > length:
            max_word = word
            length = lst.count(word)
    print(max_word)

import random

# Задание 2.сделать чтобы файл копировал себя и создавал новый с таким же кодом(2 строки)
# with open("main.py", "r", encoding="utf-8") as file, open(f"{random.randint(-100, 100)}.py", 'w', encoding='utf-8') as file_2:
#     file_2.write(file.read())
#

# Задание 3.заменить строку на новую строку.Если нет новой строки,то пишу в конец
# with open("input[2].txt", "r", encoding="utf-8") as file:
#     lst = [line.strip() for line in file]
# with open("input[2].txt", "w", encoding="utf-8") as file_2:
#     string_number = int(input("Введите номер изменяемой строки"))
#     string = input("Введите  строку")
#     if string_number <= len(lst):
#         lst[string_number-1] = string
#     else:
#         lst.append(string)
#     file_2.write('\n'.join(lst))

# Задание 4.В0 файле gosud.txt  государства ,в другом stolic.txt

# with open ("stolic.txt","r",encoding="utf-8") as file,open("gosud.txt", "r", encoding='utf-8') as file_2:
#     stolica = input("Введите столицу государства: ").capitalize()
#     file_stolica = [line.strip() for line in file]
#     print(file_stolica)
#     file_gos = [line.strip() for line in file_2]
# if stolica in file_stolica:
#     print(file_gos[file_stolica.index(stolica)])
# elif stolica in file_gos:
#     print(file_stolica[file_gos.index(stolica)])
# else:
#     print("Данной сталицы не обнаружено")

# Задание 5. В файле input[5].txt записаны числа.Первую строку в один список чисел,вторую строку в другой список чисел.Посчитать сколько общих чисел

# with open("input[5].txt", 'r', encoding="utf-8") as file:
#     lst = [set(number.strip().split()) for number in file]
#     print(len(lst[0] & lst[1]))

# Задание 6.

with open("input_6.txt", 'r', encoding="utf-8") as file:
    lst = [word if word[-1].isalnum() else word[:-1] for line in file for word in line.strip().split()]
print(lst)
max_word = lst[0]
max_count = lst.count(max_word)
for word in lst:
    if lst.count(word) > max_count:
        max_count = lst.count(word)
        max_word = word
print(f"{max_word}-{max_count}")

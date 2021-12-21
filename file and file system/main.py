import json
import os

# count = 0
# with open("result.json", 'a', encoding='utf-8') as json_file:
#     data = {
#
#         count: "Artem",
#         "lastname": "Petlitski"
#
#     }
#     json.dump(data, json_file)
#
#     count += 1
# with open("result.json", "r", encoding="utf-8") as json_file:
#     user = json.load(json_file)
# print(type(user))
# with open("input.txt", "r", encoding="utf-8") as file, open("output.txt", 'w', encoding="utf-8") as file2:
#     lst = [line.strip() for line in file]
#     file2.write("\n".join(lst))
# print(lst)
# os.makedirs("papkax/lox/lox")
# print(os.getcwd())

# Задание 1. Файл input.txt содержит некий многострочный текст, нужно этот текст прочитать,проанализировать(посчитать кол-во симоволов) и результат записать в output.txt

# with open("input.txt", "r", encoding='utf-8') as file, open("output.txt", 'a', encoding='utf-8') as file2:
#     lst = [line.strip() for line in file]
#     for i in range(len(lst)):
#         count_other = 0
#         count_letter = 0
#         count_digit = 0
#         for j in lst[i]:
#             if j.isdigit():
#                 count_digit += 1
#             elif j.isalpha():
#                 count_letter += 1
#             else:
#                 count_other += 1
#         file2.write(
#             f"В {i + 1} строке: Кол-во чисел:{count_digit},кол-во букв:{count_letter},кол-во других символов: {count_other}\n")

# Домашнее задание 1.

# with open("zad1.txt", "r", encoding='utf-8') as file:
#     lst = [line.strip() for line in file]
#     word = ""
#     for i in range(len(lst)):
#         for j in range(2):
#             word += lst[i][j]
# print(word)

# Домашнее задание 2.

# with open("zad2.txt", "r", encoding='utf-8') as file, open("result2.json", 'w', encoding='utf-8') as json_file:
#     lst = [line.strip() for line in file]
#     id = 0
#     users_list = []
#     for i in lst:
#         words = i.split(" ")
#         id += 1
#         data = {id: {"fname": words[0], "flname": words[1], "city": words[2], "tel": words[3]}}
#         users_list.append(data)
#         # json_file.write(json.dumps(data, ensure_ascii=False)+"\n")
#     json.dump(users_list, json_file, ensure_ascii=False)
# with open('result2.json', 'r', encoding='utf-8') as json_file1:
#     lst = json.load(json_file1)
#     count = 1
#     for word in lst:
#         print(f"Имя - {word[str(count)]['fname']}, Фамилия - {word[str(count)]['flname']}, Город - {word[str(count)]['city']}, Телефон - {word[str(count)]['tel']}")
#         count += 1


# Домашнее задание 3.Переброс файлов

# with open("zad3[1].txt", "w+", encoding='utf-8') as file1, open("zad3[2].txt", "w+", encoding='utf-8') as file2, open("zad3[3].txt", "w", encoding='utf-8') as file3:
#
#     file3.write(file1.read())
# # with open("zad3[1].txt", "w", encoding='utf-8') as file1, open("zad3[2].txt", "w", encoding='utf-8') as file2, open("zad3[3].txt", "r", encoding='utf-8') as file3:
# #
#     file2.write(file2.read())
#     file1.write(file3.read())

#Домашнее задание 4.Сумма чисел

# sum = 0
# with open("file4.txt","r",encoding="utf-8") as file:
#     lst = [line.strip() for line in file]
#     for word in lst:
#         if word.isdigit():
#             sum += int(word)
# print(sum)

#Домашнее задание 5.Стих
#
# gl = "аиюеёэыя"
# count_gl = 0
# count_sgl = 0
# with open("file5.txt","r",encoding="utf-8") as file:
#     lst = [line.strip() for line in file]
#     for word in lst:
#         print(word)
#     for word in lst:
#         for letter in word:
#             if letter[0] in gl:
#                 count_gl += 1
#             else:
#                 count_sgl += 1
# if count_gl > count_sgl:
#     print("Больше гласных")
# else:
#     print("Больше согласных")

#Задание Есть файл с текстом ,развернуть его содержимое и в другой файл положить

# with open("txt.txt",'r',encoding="utf-8") as file ,open("output[1].txt",'w',encoding="utf-8") as file2:
#     file2.write(file.read()[::-1].strip())

#Задание С партиями.

elections = {
    "1": "пивная",
    "2": "кпрб",
    "3": "смерть цыганам",
    "4": "водочная",
    "5": "джависты"
}
with open("input.txt", "r", encoding="utf-8") as file:
    lst = file.read().split()
    print(lst)
    for i in elections.keys():
        n = 0
        for j in lst:
            if i == j:
                n += 1
        print(f"За партию {elections[i]} - {n}")








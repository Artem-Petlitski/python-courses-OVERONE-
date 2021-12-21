
    #1. Вывести четные числа от  0 до 100

# for i in range(2, 101, 2):
#     print(i, end=" ")

    #2.  Пример с дом.задачей на проверку полиндрома

# text = input().lower()
# res = ""
# for i in text:
#     if i.isalpha() == True:
#         res += i
# if res == res[::-1]:
#     print("Полиндром")
# else:
#     print("Не полиндром")

    #3. Вводится число , вывести таблицу умножения от 1 до 10 на это число

# num = int(input("Введите число: "))
# for i in range(1,11):
#     print(f"{i} * {num} = {i*num}")

    #4. Вводится число(к примеру 60) вывести четные числа в формате
# num = int(input("Введите число: "))
# for i in range (2, num+1, 2):
#     if i % 10 == 0:
#         print(i)
#     else:
#         print(i, end=" ")

    #5. Вводится строка, посчитать кол-во больших и маленьких букв

# str = input("Введите строку: ")
# count_low = 0
# count_up = 0
# for i in str:
#     if i.islower():
#         count_low += 1
#     elif i.isupper():
#         count_up += 1
# print(f'Количетсво больших букв: {count_up} \nКоличество маленьких букв: {count_low}')

    #6. Поступает текст на русском.Подсчитать кол-во гласных и согласных

# str = input("Введите строку: ").lower()
# str_glas = "аеёяуоюэыиaoieyu"
# count_vowels = 0 #гласные
# count_consonants = 0 #согласные
# count_anothers = 0
# for i in str:
#     if not i.isalpha():
#         count_anothers += 1
#         continue
#     else:
#         if i in str_glas:
#             count_vowels += 1
#         else :
#             count_consonants += 1
# print(f"Кол-во согласных:{count_consonants}\nКол-во гласных: {count_vowels}\nКол-во прочих символов: {count_anothers}")

#     #7.Домашнее задание. Вводится число вывести четные числа в формате
#
# num = int(input("Введите число: "))
# for i in range (2, num+1, 2):
#     if i % 10 == 0:
#         print(i)
#     else:
#         print(i, end=" ")
#
#     #8. Домашнее задание. Вводится 2 слова, определить являются ли они аннограммами (состоят из одного и того же набора букв)
#
# str_1 = input("Введите первое слово: ").lower()
# str_2 = input("Введите второе слово: ").lower()
# count = 0
# if len(str_1) == len(str_2):
#     for i in str_1:
#         if str_1.count(i) != str_2.count(i):
#             print("Не анограмма")
#             break
#     else:
#         print("Анограмма")
# else:
#     print("Не анограмма")
#
#     #9. Домашнее задание. Вводится строка, вывести уникальные символы в этой строке
#
# str = input("Введите строку: ").lower()
# count = 0
# for i in str:
#     if str.count(i) == 1:
#         print(i, end="   ")
#     else:
#         continue
#
#     #10. Домашнее задание. В строке определить количество пар одинаковых символов рядом стоящих в строке, пример Hello 1 пара, АааИИ 2 пары
# str = input("Введите строку: ").lower()
# str = str.strip()
# count_moment = 0
# count_common = 0
# for i in range(0,len(str)-2):
#     if (str[i]==str[i+1]):
#         count_moment += 1
#         if count_moment >= 1:
#             count_common += 1
#     else:
#         continue
# print(f'Количетсво пар одинаковых элементов: {count_common}')

    #11. Домашнее задание.  ord возвра код символа char возвр символ из кода. На вход идет строка, зашифровать её шифром Цезаря со сдвигом на указанное число
str = input("Введите строку: ")
num = int(input("Введите число сдвига: "))
str_end = ""
for i in str:
    if i.isalnum():
        if i.isalpha() and i.isupper():
            if ord(i) + num > 90:
                str_end += chr(ord(i) + num - 26)
            else:
                str_end += chr(ord(i) + num)
        elif i.isalpha() and i.islower():
            if ord(i) + num > 122:
                str_end += chr(ord(i) + num - 26)
            else:
                str_end += chr(ord(i) + num)
        else:
            if ord(i) + num > 57:
                str_end += chr(ord(i) + num - 10)
            else:
                str_end += chr(ord(i) + num)
    else:
        str_end += i

print(str_end)

    #12. Домашнее задание. На вход поступает число бильярдных шаров. Определить, сколько можно построить рядов(неполные тоже считаем)
sh = int(input("Введите количетсво бильярдных шаров: "))
count = 0
i = 1
while sh > 0:
    if sh - i > 0:
        sh = sh - i
        count += 1
        i += 1
    elif sh - i == 0:
        count += 1
        break
    else:
        count += 1
        break
print(count)





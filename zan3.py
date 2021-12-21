# #1. На вход поступает строка состоящая из 3 слов. Определить какой из них самое длинное

# str = input("Введите 3 слова:")
# probel_1 = str.find(" ")
# probel_2 = str.rfind(" ")
# slovo_1 = str[:probel_1]
# slovo_2 = str[probel_1 + 1:probel_2]
# slovo_3 = str[probel_2 + 1:]
# dlina_1 = len(slovo_1)
# dlina_2 = len(slovo_2)
# dlina_3 = len(slovo_3)
# if dlina_1 > dlina_2 and dlina_1 > dlina_3:
#     print(slovo_1)
# elif dlina_3 > dlina_2:
#     print(slovo_3)
# else:
#     print(slovo_2)

#2. Вводится предложение. Все а и А заменить на @ после каждого слова вставить!
#
# str = input("Введите предложение: ")
# str = str.replace("a", "@")
# str =str.replace("а", "@")
#
# str = str.replace("A", "@")
# str = str.replace("А", "@")
# str = str.replace(" ", "! ")
# str = str + "!"
# print(str)

#3. Вволится предложение проверить есть ли в этом предложении ошибка в правописании жи-ши и вывести это слово
# str = input("Введите предложение: ")
# name = str.split(" ")
# for slovo in name:
#     if "жы" in slovo:
#         print(slovo)

#4. На вход поступает предложение и 2 числа.Задача удалить из этого предложения  все содержимое между первым и вторым числом по индексу
# str=input("Введите строку")
# beg=int(input())
# end = int(input())
# if beg > len(str) and end > len(str) and end < -len(str) and beg < - len(str)  :
#     print( "Ошибка")
# else:
#   if beg > end:
#     beg,end = end, beg;
#    str = str[:beg] + str[end+1:]
#    print(str)

#5. Домашнее задание. Вводится строка переставить местами первое и последнее слово
#!!!!!Переделать c  f-string!!!!!!#

# str = input("Введите предложение:")
# str=str.strip()
# probel_1 = str.find(" ")
# probel_2 = str.rfind(" ")
# if probel_1 or probel_2 == -1:
#     print('ERROR')
# else:
#     slovo_1 = str[:probel_1]
#     slovo_2 = str[probel_2+1:]
#     str = str[probel_2+1:] +" " + str[probel_1+1:probel_2] + " " + str[:probel_1]
#     print(str)

#6. Домашнее задание. Вводится слово,определить является ли оно полиндромом.

word_1 = input("Введите слово: ").lower().replace(" ","")
word_2 = word_1[::-1]
if word_2 == word_1:
    print("Слово полиндром")
else:
    print("Слово не полиндром")



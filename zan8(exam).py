import  random
#Задание 1.
# str = input("Введите число: ")
# count_neven = 0 //нечетные
# count_even = 0 //четные
# count = 0
# proizv = 1
# if len(str) == 7 and str.isdigit():
#    for i in range(len(str)):
#         if int(str[i]) % 2 == 0 and int(str[i]) != 0:
#             count_even += 1
#         elif int(str[i]) % 2 == 1 and int(str[i]) != 0:
#             count_neven +=1
#    if count_even > count_neven:
#        for i in range(len(str)):
#            count += int(str[i])
#        print(f"Сумма всех элементов: {count}")
#    elif count_even < count_neven:
#            proizv = proizv * int(str[0]) * int(str[5]) * int(str[2])
#            print(f"Произведение 1, 3, 6 числа: {proizv}")
#    else:
#        if str.count("0") == 7:
#            print("Все семь 0")
#        else:
#            print("Кол-во четных и нечетных равно")
# else:
#     print("ERROR!")

#Задание 2.

# str = input("Введите текст: ").lower()
# gl = "ауоыиэяюёеaeiouy"
# glas = 0
# sogl = 0
# sym = 0
# for i in str:
#     if i.isalpha() == False:
#         sym += 1
#     elif i in gl:
#         glas += 1
#     else: sogl += 1
# if g == s:
#     for i in str:
#         if i in gl:
#             print(i,end = "")
#     print()
# print(f"Кол-во гласных:{glas}, кол-во согласных: {sogl}, кол-во прочих символов: {sym}")

#Задание 3.
# count = 0
# i = 0
# while i < 7:
#     num_1 = int(input("Введите первое число от 1 до 20: "))
#     num_2 = int(input("Введите второе число от 1 до 20: "))
#     sum_1 = num_1 + num_2
#     if num_1 in range(1,21) and num_2 in range(1, 21):
#         num_3 = random.randint(1, 20)
#         num_4 = random.randint(1, 20)
#         sum_2 = num_3 + num_4
#         if sum_1 > sum_2:
#             print(f"Введенная пара больше. num_1 = {num_1}, num_2 = {num_2}, num_3 = {num_3}, (ранд.)num_4 = {num_4}")
#             count += 1
#         elif sum_1 < sum_2:
#             print(f"Введенная пара меньше. num_1 = {num_1}, num_2 = {num_2}, num_3 = {num_3}, (ранд.)num_4 = {num_4}")
#         else:
#             print("Пары введенных чисел равны")
#         i += 1
#     else:
#         print("Вышло из диапазона!")
# print(f"Введенная с клавиатуры пара больше рандомной {count} раз")

#Задание 4.

# count_num = 0
# count = 0
# number = ""
# count = int(input("Укажите количество вводимых чисел: "))
# num = input("Введите искомое число: ")
# i = 0
# for _ in range(count):
#     number += str(random.randint(1,1000))
#
# print(number.count(num))

#Задание 5.

str_5 = input("Введите строку: ")
num =''
for i in range(len(str_5)):
    if str_5[i].isdigit():
        num += str_5[i]
        if i<len(str_5)-1 and not str_5[i+1].isdigit():
            print(num)
            num = ''
print(num)



#Задание 6.

# str_6 = input("Введите текст: ")
# gl = "ауоыиэяюёеaeiouyАУОЫИЭЯЮЕЁAEIOUY"
# g = 0
# s = 0
# sym = 0
# count_up= 0
# count_low= 0
# for i in str_6:
#     if i.isalpha() == False:
#         sym += 1
#     elif i in gl:
#         g += 1
#     else: s += 1
# for i in range(0,len(str_6)-1):
#     if  (str_6[i].isupper() and str_6[i+1].isupper()):
#         i += 2
#         count_up += 1
#     elif (str_6[i].islower() and str_6[i+1].islower()):
#         i += 2
#         count_low += 1
#     else:
#         i+=1
# print(f"Кол-во гласных:{g}, кол-во согласных: {s}, кол-во прочих символов: {sym},кол-во букв в слове {g+s},кол-во пар верхнего регистра {count_up},кол-во пар нижнего регистра:{count_low}")
#
#
#
#
#
#

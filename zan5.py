#Задание 1. Вывести 13 чисел кратных 17 начиная от 100

# c = 0
# i = 100
# while c < 13:
#     if i % 17 == 0:
#         print(i)
#         c += 1
#     i += 1

#Задание 2. Дано целое число не меньше 2(2..),необходимо вывести его наименьший натуральный делитель отличный от 1

# num = int(input("Введите число: "))
# dl = 2
# while dl <= num:
#     if num % dl == 0:
#         print(dl)
#         break
#     else:
#         dl += 1

#Задание 3. Определить нарушается ли где-то порядок и указать индекс

# st = input()
# i = 1
# while i < len(st):
#     if int(st[i-1]) <= int(st[i]):
#         i += 1
#     else:
#         print(f"нарушен порядок на {i+1} элементе")
#         break
# else:
#     print("Всё ок")

#Задание 4. Вводится число, распечатать все квадраты нат чисел не превосход это число

# num = int(input("Введите число: "))
# i = 1
# while i ** 2 <= num:
#     print(i ** 2, end = " ")
#     i += 1

#Задание 5. Вводится какая-то строка и число(разбить строку на указанное количетсво частей)

# str = input("Введите строку: ")
# num = int(input("Введите число: "))
# while len(str) % num != 0:
#     str += "0"
# count = len(str) // num
# i = 0
# while i < len(str):
#     print(str[i], end ="")
#     i += 1
#     if i % count == 0:
#         print(" ", end = "")

#Задание 6. Есть строка из чисел(любая). Определить сколько элементов больше предыдущего

# str = input()
# i = 1
# count = 0
# while i < len(str):
#     if int(str[i-1]) < int(str[i]):
#         count += 1
#     i += 1
# print(count)

#Задание 7.Вводится какая-то строка и число(разбить строку на указанное количетсво cимволов в части)

# str = input("Введите строку: ")
# num = int(input("Введите число: "))
# while len(str) % num != 0:
#     str += "0"
# count = len(str) // num
# i = 0
# while i < len(str):
#     print(str[i], end ="")
#     i += 1
#     if i % num == 0:
#         print(" ", end = "")


#Домашнее задание 8. Вводится число N, определить максимальную степень 2,где 2 в этой степени не превышает N.

N = int(input("Введите число: "))
i = 0
value = 1
if N < 1:
    print("ERROR!")
else:
    while i < N:
        if value <= N:
            value = value * 2
            i += 1
        else:
            break

    print(i-1)




#Домашнее задание 9. Развернуть строку без использования среза

str_0 = input("Введи строку: ")
str_1 = ""
i = len(str_0) - 1
while i >= 0:
    str_1 += str_0[i]
    i -= 1
print(str_1)

#Домашнее задание 10. Вводится число, определить является ли оно простым или нет(делится на само себя и на 1)

N = int(input("Введите число: "))
i = 1
cot = 0
while i < N:
    if N % i == 0:
        cot += 1
        i += 1
    else:
        i += 1
    if cot == 2:
        print("Не простое")
        break
else:
    print("Простое")


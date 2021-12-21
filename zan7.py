import random
#Задание 1.Есть список чисел,найти макс и мин элементы списка

# lst = [random.randint(-20,20) for i in range(10)]
# print(lst)
# max = lst[0]
# min = lst[0]
# adres_max = 0
# adres_min = 0
#
# for i in range(len(lst)):
#     if lst[i] > max:
#         max = lst[i]
#         adres_max = i
#     if lst[i] < min:
#         min = lst[i]
#         adres_min = i
#     i += 1
# print(f"Максимальный элемент: {max}, минимальный элемент: {min}")


#Задание 2.Доработка.Нашли второй максимальный и второй минимальный

# i = 0
# max_twelth = min
# min_twelth = max
# for i in range(len(lst)):
#     if lst[i] > max_twelth and lst[i] < max:
#         max_twelth = lst[i]
#     if lst[i] < min_twelth and lst[i] > min:
#         min_twelth = lst[i]
# print(f"Второй максимальный: {max_twelth}, второй минимальный элемент: {min_twelth}")


#Задание 3.Доработка.Поменяли местами мин и макс


# lst[adres_min], lst[adres_max]=lst[adres_max], lst[adres_min]
# print(lst)

#Задание 4.Есть список ЛЮБЫХ элементов.Переставить соседние элементы местами.Если элементов нечетное число,то последний на месте.

# lst = [1,2,True,False,'Artem',"dima"]
# for i in range(0,len(lst)-1,2):
#     lst[i],lst[i+1] = lst[i+1],lst[i]
# print(lst)

#Задание 5.


#Домашнее задание(спираль).
lst = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
i = 0
j = 0
num = 1
while j < 4:
    lst[i][j] = num
    num += 1
    j += 1
while i < 4:
    lst[i][j] = num
    i += 1
    num += 1
while j > 0:
    lst[i][j] = num
    j -= 1
    num += 1
while i > 0:
    lst[i][j] = num
    i -= 1
    num += 1
while j < 3:
    lst[i][j] = num
    j += 1
    num += 1
while i < 3:
    lst[i][j] = num
    i += 1
    num += 1
while j < 1:
    lst[i][j] = num
    j -= 1
    num += 1
while i < 1:
    lst[i][j] = num
    i -= 1
    num += 1
i=0
j=0
while i<5:
    j = 0
    while j<5:
        print(lst[i][j],end=" ")
        j+=1
    print()
    i+=1



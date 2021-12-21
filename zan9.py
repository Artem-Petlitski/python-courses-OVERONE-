#Задание 1.Дан список элементов. Используя только  while вывести все элементы в обратном порядке

list = ["abc", True, 1]
i = len(list)-1
while i >= 0:
    print(list[i])
    i -= 1



#Задание 2.Понять можно ли походить конем

# x_1 = int(input())
# y_1 = int(input())
# y_2 = int(input())
# x_2 = int(input())
#
# if abs(x_2 - x_1) == 1 and abs(y_2 - y_1) == 2 or abs(y_2 - y_1) == 1 and abs(x_2 - x_1) == 2:
#     print("Можно")
# else:
#     print("Нельзя")



#Задание 3. Вводится координата коня, вывести координаты всех клеток куда можно перейти за один ход.

# str = int(input())
# stl = int(input())
# list_str = [0,0,0,0,0,0,0,0,0]
# list_stl = [0,0,0,0,0,0,0,0,0]
#
# list_str[0] += str + 2
# list_stl[0] += stl + 1
#
# list_str[1] += str + 1
# list_stl[1] += stl + 2
#
# list_str[2] += str - 2
# list_stl[2] += stl - 1
#
# list_str[3] += str - 1
# list_stl[3] += stl - 2
#
# list_str[4] += str + 2
# list_stl[4] += stl - 1
#
# list_str[5] += str - 2
# list_stl[5] += stl + 1
#
# list_str[6] += str + 1
# list_stl[6] += stl - 2
#
# list_str[7] += str - 1
# list_stl[7] += stl + 2
#
# for i in range(8):
#     if 1 <= list_str[i] <= 8 and 1 <= list_stl[i] <= 8:
#         print(f"{list_str[i]}--{list_stl[i]}")

# #!!!Задание 4. Судоку!!!
#
# # import random
# # sudoky = []
# # str = [1,2,3,4,5,6,7,8,9]
# # random.shuffle(str)
# # sudoky.append(str)
# # str = [random.randint(1,10) for i in range(10)]
# # random.shuffle(str)
# # sudoky.append(str)
# # print(sudoky)
# import random
#
# lst_1 = [[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]]
#
# j = 0
# i = 0
# random.shuffle(lst_1[0])
# while i < 8:
#     count = 0
#     j = 0
#     while j < 9  :
#         count = 0
#         if lst_1[i+1][j] ==  lst_1[i][j]:
#             random.shuffle(lst_1[i+1])
#             continue
#         elif lst_1[i+1][j] == lst_1[i-count][j]:
#             random.shuffle(lst_1[i + 1])
#             continue
#         else:
#             while count <= i:
#                 count += 1
#             else:
#                 j+= 1
#
#     i += 1
#
# for i in range(len(lst_1)):
#     print(lst_1[i])
#

#!!!Задание 5. Таблица Пифагора!!!

# for i in range(1,11):
#     for j in range(1,11):
#         if i*j == 1:
#             print(f'{"":>4}',end ='')
#             j += 1
#             continue
#         print(f'{i*j:>3}',end = ' ')
#     print()






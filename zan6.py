import random
#Домашнее задание 1.Определить является ли список упордяоченныи по возрастанию. Если нет,то  опеределить номер первого этомента нарушающего последовательность

# spisok_1 = [1,3,5,7,9,6]
# i = 0
# while i < len(spisok_1)-1:
#     if spisok_1[i] <= spisok_1[i+1]:
#         i += 1
#     else:
#         print(f"Индекс элемента, нарушающего последовательность: {i+1}")
#         break
# else:
#     print("Список является упорядоченным")
#



#Домашнее задание 2. Дан список некоторых целых чисел,найти в нем число 20 и заменить на 200,заменить только первую 20

# spisok_2 = [1,10,5,7,12,20]
# i = 0
# while i < len(spisok_2):
#     if spisok_2[i] == 20:
#         print(f"Список до: {spisok_2}")
#         spisok_2[i] = 200
#         print(f"Список после: {spisok_2}")
#         break
#     else:
#         i += 1
# else:
#     print("Число 20 не обнаружено")

#Домашнее задание 3.Необходимо удалить пустые строки из списка строк.

# spisok_3 = ['ads','sad','','312','132']
# i= 0
# print(f"Список до: {spisok_3}")
# while "" in spisok_3 :
#     spisok_3.remove("")
# print(f"Список после: {spisok_3}")

#Домашнее задание 4.Заполнить список ста 0, кроме первого и последнего значения, они должны быть равны 1.

# spisok_4 = []
# i = 0
# while i < 102:
#     if i == 0 or i == 101:
#         spisok_4.append(1)
#         i += 1
#     else:
#         spisok_4.append(0)
#         i += 1
# print(spisok_4)
# print(len(spisok_4))

#Домашнее задание  5.Пользатель вводит число, определить содержит список это число или нет.Если есть - выводим TRUE иначе FALSE

# spisok_5 = [random.randint(1,100) for i in range (10)]
# num = int(input("Введите число: "))
# if num in spisok_5:
#     print(True)
# else:
#     print(False)

#!!! Генератор: spisok_5 = [1 if i==0 or i==101 else 0 for i in range (102)] #Генератор списка!!
# lst = [i for i in range(101)]

# Домашнее задание  6. На вход поступает строка чисел, разделенных пробелом, сформировать из этой строки список и вывести сумму соседей элемента

# spisok_6 = []
# str = input("Введите числа, разделенные пробелом: ")
# str = str.strip()
# spisok_6 = str.split(" ")
# print(spisok_6)
# i = 0
# while i < len(spisok_6):
#     if i == 0:
#         print(f'{i+1}-ый элемент списка, сумма его соседних элементов {int(spisok_6[-1]) + int(spisok_6[1])}')
#     elif i == (len(spisok_6)-1):
#         print(f'{i + 1}-ый элемент списка, сумма его соседних элементов {int(spisok_6[- 2]) + int(spisok_6[0])}')
#     else:
#         print(f'{i+1}-ый элемент списка, сумма его соседних элементов {int(spisok_6[i-1]) + int(spisok_6[i+1])}')
#     i += 1

# Домашнее задание  7.Дан список рандомных чисел, а также с клавиатуры поступает число, необходимо сместить элементы списка вправо по индексам на это число

# spisok_7 = [1,2,3,4,5,6,7]
# print(spisok_7)
# length = len(spisok_7)
# num = int(input("Введите число сдвига: "))
# spisok_buffer = []
# i = 0
# while i < len(spisok_7):
#     if i - num <= 0:
#         spisok_buffer.insert((i - num + length),spisok_7[i])
#         i += 1
#     else:
#         spisok_buffer.insert((i-num-1),spisok_7[i])
#         i += 1
# print(spisok_buffer)

#7 Ещё одно решение.

# lst =[1,2,3,4,5,6,7,8,9,10,11]
# num=int(input())
# lst = lst[len(lst)-num:]+lst[:len(lst)-num]
# print(lst)

# Домашнее задание  8.Дан список,переставить след.образом(на четных оставим, на нечетных поменяем)

lst = [1,2,3,4,5,6,7]
for i in range(len(lst)//2):
    if i % 2 == 0:
        lst[i], lst[len(lst)-1-i] = lst[len(lst)-1-i], lst[i]
    else:
        continue
print(lst)








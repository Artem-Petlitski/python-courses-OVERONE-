# #1. Вводится 2 числа с клавиатуры вывести True если расстояние между числами 135 иначе False
# a=float(input("Введите первое число: "))
# b=float(input("Введите второе число: "))
# if abs(a - b) == 135:
#     print(True)
# else:print(False)
#
# #2. True если а меньше -100 или а больше 100 иначе false:
# a=float(input("Введите первое число: "))
# if a < -100 or a > 100:
#     print(True)
# else:
#     print(False)
#
# #3. Даны 3  числа True если из них можно построить треугольник:
# a = float(input("Введите первое число: "))
# b = float(input("Введите второе число: "))
# c = float(input("Введите третье число: "))
# if a + b > c and a + c > b and b + c > a:
#     print(True)
# else:print(False)
#
# #4. Даны 2 числа вывести наименьшее:
# a = float(input("Введите первое число: "))
# b = float(input("Введите второе число: "))
# if a < b:
#     print(a)
# elif b < a:
#     print(b)
# else:
#     print("а=b")
#
# #5. Из 3-x чисел вывести среднее:(1)
# a = float(input("Введите первое число: "))
# b = float(input("Введите второе число: "))
# c = float(input("Введите третье число: "))
# if b > a and b < c or b > c and b < a:
#     print(b)
# elif c > b and c < a or c > a and c < b:
#     print(c)
# elif a > b and a < c or a > c and a < b:
#     print(a)
# else:
#     print("Числа равны")
#
#
#
# #6. Високсные года делятся нацело на 4, однако столетия, которые не делятся нацело на 400 не являются столетиями. На вход поступает год: определить или является год високосным.
# year = int(input("Введите год: "))
# if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
#     print("Високосный")
# else:
#     print("Не подходит")
#
# #7. Поступает на вход число 1 <= n <= 9999 (во копеек выразить это в рублях и копейках
# kop=int(input("Введите число копеек в диапазоне от 1 до 9999: "))
# while kop < 1 or kop > 9999:
#     print("Вы ввели неверное число!")
#     kop = int(input("Введите число копеек в диапазоне от 1 до 9999: "))
# else:
#
#     print("Рублей:", kop//100, "копеек:", kop % 100)
# #
# #8. Дан радиус круга и сторона квадрата true  если квадрат можно вместить в круг
#
# rad = float(input("Введите радиус круга: "))
# st = float(input("Введите сторону квадрата: "))
# diag = (2 * st ** 2) ** (1 / 2)
# if rad >= diag / 2:
#     print(True)
# else:
#     print(False)
#
#9. НА вход номер телефона без + определить валидный он или нет(isdigit использовать)

# nomer=input("Введите номер телефона: ")
# if nomer.isdigit() and len(nomer)==12:
#     if nomer.startswith("37529") or nomer.startswith("37544") or nomer.startswith("37525") or nomer.startswith("37533"):
#         print("Валидный")
#     else:
#         print("Неверный номер телефона")
# else:
#         print("Неверный номер телефона")
#
#

# #10 Домашнее задание.В зависимости от введенного возраста мы приветствуем пользователя по-разному
# age = int(input("Введите ваш возраст: "))
# if age > 0 and age < 18:
#     print("Ку")
# elif age >= 18 and age <= 40:
#     print("Привет")
# elif age > 40 and age <= 60:
#     print("Приветствую")
# elif age > 60 and age < 80:
#     print("Здравствуйте")
# elif age >= 80 and age <= 100:
#     print("Моё почтение")
# elif age > 100 and age <= 120:
#     print("Hello")
# else:
#     print("Введите корректный возраст")
#
# #11. Домашнее задание. На вход поступают два числа(координаты на шахматной доске),сказать черная эта клетка или белая.
# coordinate1 = input("Введите первую координату фигуры (английская буква A-H): ")
# coordinate2 = int(input("Введите вторую координату фигуры (1-8): "))
# if coordinate1 == 'A' or coordinate1 == 'C' or coordinate1 == 'E' or coordinate1 == 'G' \
#        or coordinate1 == 'a' or coordinate1 == 'c' or coordinate1 == 'e' or coordinate1 == 'g':
#     if coordinate2 % 2 == 1 and coordinate2 in range(1, 9):
#         print("Черная клетка")
#     elif coordinate2 % 2 == 0 and coordinate2 in range(1, 9):
#         print("Белая клетка")
#     else:
#         print("Введите корректные данные!")
# elif coordinate1 == 'B' or coordinate1 == 'D' or coordinate1 == 'F' or coordinate1 == 'H' \
#         or coordinate1 == 'b' or coordinate1 == 'd' or coordinate1 == 'f' or coordinate1 == 'h':
#     if coordinate2 % 2 == 1 and coordinate2 in range(1, 9):
#         print("Белая клетка")
#     elif coordinate2 % 2 == 0 and coordinate2 in range(1, 9):
#         print("Черная клетка")
#     else:
#         print("Введите корректные данные!")
# else:
#     print("Введите корректные данные!")

# #12. Домашнее задание. На вход поступают два числа(координаты на шахматной доске),сказать черная эта клетка или белая.(тут поступает 2 числа)
# coordinate1 = int(input("Введите первую координату фигуры (1-8): "))
# coordinate2 = int(input("Введите вторую координату фигуры (1-8): "))
# if coordinate1 % 2 == 1 and coordinate1 in range(1, 9):
#     if coordinate2 % 2 == 1 and coordinate2 in range(1, 9):
#         print("Черная клетка")
#     elif coordinate2 % 2 == 0 and coordinate2 in range(1, 9):
#         print("Белая клетка")
#     else:
#         print("Введите корректные данные!")
#
# elif coordinate1 % 2 == 0 and coordinate1 in range(1, 9):
#     if coordinate2 % 2 == 1 and coordinate2 in range(1, 9):
#         print("Белая клетка")
#     elif coordinate2 % 2 == 0 and coordinate2 in range(1, 9):
#         print("Черная клетка")
#     else:
#         print("Введите корректные данные!")
# else:
#     print("Введите корректные данные")
#
# #13. Домашнее задание. На вход поступает номер месяца, сказать какой это сезон года.
# month_number = int(input("Введите номер месяца: "))
# if month_number in range(1, 3) or  month_number == 12:
#     print("Зима")
# elif month_number in range(3, 6):
#     print("Весна")
# elif month_number in range(6,9):
#     print("Лето")
# elif month_number in range(9,12):
#     print("Осень")
# else:
#     print("Вы ввели неверный номер месяца!")

#14. Домашнее задание с шахматами.
coordinate1 = int(input("Введите первую координату фигуры (1-8): "))
coordinate2 = int(input("Введите вторую координату фигуры (1-8): "))
if (coordinate1 + coordinate2) % 2 == 0 and coordinate2 in range(1,9) and coordinate1 in range(1,9):
    print("Черная клетка")
elif (coordinate1 + coordinate2) % 2 == 1 and coordinate2 in range(1,9) and coordinate1 in range(1,9):
    print("Белая клетка")
else:
    print("Введите корректные даннные!")






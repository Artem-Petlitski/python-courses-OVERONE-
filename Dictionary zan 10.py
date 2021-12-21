# Словари
# from random import randint
# Задача 1. Дан словарь(сами задаем ключи) с числовыми значениями.Перемножить все значения

# product = 1 #произведение
# dict_1 = {i: randint(1, 10) for i in range(3)}
#
# for j in dict_1.values():
#     product *= j
#
# print(product)

# Task 2.

# dict_2 = {i: i**3 for i in range(1,11)}
# print(dict_2)

# Task 3.Реализовать программа со словарем Users
i = 1
flag = 0

users = {}
choice = 0
while choice != 5:
    choice = input("\n""Введите действие:""\n 1:Добавление пользователя \n ""2:Вывод информации о пользователе. \n "
                   "3:Удалить пользователя. \n ""4:Обновление информации о пользователе \n ""5:Выход \n")

    if choice == "1":

        try:
            users[i]= {
                'name': input("Введите ваше имя:").strip(),
                'lastname': input("Введите вашу фамилию:").strip(),
                'age': int(age) if (age := input()) and age.isdigit() and int(age) in range(0, 101) else 'Некоректный возраст',
            }
            i += 1
            flag = 1
            print("Пользователь добавлен!")

        except ValueError:
            print('Вы ввели некорректный возраст!')

    elif choice == "2":
        if flag == 0:
            print("Пользователи не были добавлены")
        else:
            print("ID существующих пользователей:")
            for k in users.keys():
                print(k)
            try:
                id_inf = int(input("Введите id пользователя: "))

                g = users.get(id_inf, {})

                print(f'\nID пользователя: {id_inf}''\v\tИмя: ' + g['name']+'\v\t Фамилия: ' + g['lastname'] + '\v\tВозраст: ' + f"{g['age']}")


            except KeyError:
                print('Пользователь с таким ID не найден ')
            except ValueError:
                print('Пользователь с таким ID не найден ')

    elif choice == "3":

        if flag == 0:
            print("Пользователи не были добавлены")
        else:
            print("ID существующих пользователей:")
            for i in users.keys():
                print(i)

            try:
                id_del = int(input("\nВведите id удаляемного пользователя: "))
                del users[id_del]
                print("Пользователь удалён!\n")
            except KeyError:
                print('Пользователь с таким ID не найден ')
            except ValueError:
                print('Пользователь с таким ID не найден ')

    elif choice == "4":
        if flag == 0:
            print("Пользователи не были добавлены")
        else:
            print("ID существующих пользователей:")
            for i in users.keys():
                print(i)
            try:
                id_edit = int(input("Введите id обновляемого пользователя: "))
                print(users[id_edit])

                num = input("Выберите изменяемое поле: 1:name, 2: lastname, 3: age\n").strip()
                if num == "1":
                    edit_value = input('Введите новое значение: ')
                    g = users.get(id_edit, {})
                    g['name'] = edit_value
                elif num == "2":
                    edit_value = input('Введите новое значение: ')
                    g = users.get(id_edit, {})
                    g['lastname'] = edit_value
                elif num == "3":
                    try:
                        edit_value = int(input('Введите новое значение: '))
                        g = users.get(id_edit, {})
                        g['age'] = edit_value
                    except ValueError:
                        print('Вы ввели неверное значение ')
                else:
                    print("Вы ввели неверное  значение!")
            except KeyError:
                print('Пользователь с таким ID не найден ')
            except ValueError:
                print('Пользователь с таким ID не найден ')

    elif choice == "5":
        print("Exit...")
        break

    else:
        print("Вы ввели некорректное значение!")

# Домашнее задание 1. Словарь с числовыми ключами и значениями:1) вывести пары ключ значения в порядке убывания ключей
# 2)вывести пары ключ значения в порядке возрастания ключей

# dictionary = {randint(1,20):"name" for i in range(10)}
# tuple1_dictionary = sorted(dictionary.items(), reverse=True)
# tuple2_dictionary = sorted(dictionary.items())
# print(dict(tuple1_dictionary))
# print(dict(tuple2_dictionary))
# print("##################")

# Домашнее задание 2. Задан словарь с ключами в виде строк, вводится слово, есть есть в словаре такой ключ,
# то вывести значение по этому ключу, иначе вывести False

# dictionary_2 = {"Artem": 1, "Dima": 2}
# required_value = input("Введите искомое значение: ")
# if required_value in  dictionary_2:
#     print(dictionary_2.get(required_value))
# else:
#     print(False)
# print("##################")

# Домашнее задание 3.Есть словарь, вывести те ключи, значения по которым имеют тип int

# dictionary_3 = {"Artem": 1, "Dima": 2, 3: "valera", 4: ["as","asd"],"пятый ключ:)": 4}
# for key,int_value in dictionary_3.items():
#     if type(int_value) == int:
#         print(key)
# print("##################")

# Домашнее задание 4.Есть Словарь с ключами разных типов, сформировать строку состоящую из ключей которые по типу str

# dictionary_4 = {"Artem": 1, "Dima": 2, 3: "valera", 4: ["as","asd"],"пятый ключ:)": 4}
# finished_line = ""
# for key in dictionary_4.keys():
#     if type(key) == str:
#         finished_line += key
# print(finished_line)

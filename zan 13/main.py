# Плюсы: 1) Скорость, 2) Память
# stack -> 1)LIFO(в питоне) 2)FIFO
# Принцип работы LIFO:создали список и удаляем элементы с конца

# Создание функции:
# def foo(c):
#     c += 1
#     if c != 10:
#         return foo(c)
#     else:
#         return c
#
#
# d = foo(5)
# print(d)

# Выносим в функцию блок кода, который независим от другого блока

# Рекурсия (пример)
# def foo(c):
#     c += 1
#     if c != 10:
#         return foo(c)
#     else:
#         return c
#
#
# d = foo(5)
# print(d)

# 5 задача из  экзамена.

backery = {"cake": {
    "price": 100,
    "total": 10},
    "maffin": {"price": 120, "total": 10}
}


def tovar(info):
    global backery
    products = list(backery.keys())
    for index, value in enumerate(products):
        print(f"Введите {index} для {value}")
    choice = int(input())
    while choice >= len(products):
        print("Вы ввели неверное число, повторите ввод, пожалуйста")
        choice = int(input())
    else:
        product = products[choice]
    f"{value}--price:{backery[product]['price']}, total:{backery[value]['total']}


def get_price(fil):
    product = tovar()
    print(','.join([f"{product}--{f}:{backery[product][f]}" for f in fil]))


def get_all_info():
    global backery
    products = list(backery.keys())
    for index, value in enumerate(products):
        print(f"{value}--price:{backery[value]['price']}, total:{backery[value]['total']}")


def buy():
    product = tovar()
    total = int(input("Введите кол-во товара"))
    while total > backery[product]['total']:
        print("Данное количество не найдено на складе, повторите ещё")
        print(f"Имеется на складе данного товара: {backery[product]['total']}")
        total = int(input("Введите кол-во товара"))
    else:
        backery[product]['total'] = backery[product]['total'] - total
        print(f"Ваш чек:{total * backery[product]['price']}")


def main():
    while True:
        print('''
        1.Посмотреть описание
        2.Посмотреть цену
        3.Посмотреть количество
        4.Вся информация
        5.Приступить к покупке.
        6.До свидания
        ''')
        choice = input(
        )
        if choice == "1":
            get_price(('price', 'total'))
        elif choice == "2":
            get_price(('price',))
        elif choice == "3":
            get_price(('total',))
        elif choice == "4":
            get_all_info()
        elif choice == "5":
            buy()
        elif choice == "6":
            print("До свидания")
            break
        else:
            print("Неверный ввод!")


if __name__ == '__main__':
    main()

#
# lst = [1, 2, 3, 4, 5]
# lst = list(map(lambda x: x ** 3, lst))
# print(lst)

# def foo(name):
#     for index, val in enumerate(name):
#         name[index] = val ** 3
#     return name
#
# print(foo(lst))
#
# lst_1 = [1,2,3,4,5]
# txt = "abc"
# print(list(zip(lst_1,txt)))


# РЕализовать функцию. На вход поступает кол-во шаров, сколько рядов(даже неполных, можно построить рядов)
#
# def piramida (balls):
#     count = 0
#     for i in range(1, balls+1):
#
#         if balls - i > 0:
#             count += 1
#             balls -= i
#
#         elif balls != 0:
#             count += 1
#             break
#     return count
#
#
# print(piramida(4))

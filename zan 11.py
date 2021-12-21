#вывод всех путей к файлам в директории.

# import os
# p = list(os.walk('.'))
# listt = [[i[0] + "/" + j for j in i[2]] for i in p]
# print(listt)
#


#Задание 2. На вход поступает строка "собака это животное"" и выввести dog это animal

# data = {"dog":"собака", "house":"дом", "animal":"животное"}
# text = input().lower()
# for key, value in data.items():
#         text = text.replace(value, key)
# print(text)

#Задание 3.Объединить 2 словаря без  update

# dict_1 = {
#             "name":"Artem",
#           "lastname":"Petlitski"
#           }
# dict_2 = {"age":"19"}
# for key, value in dict_2.items():
#         if key in dict_1:
#             continue
#         else:
#             dict_1[key] = value
# print(dict_1)

#Задание 4

# storage = {"bread":{"price":2, "weigth": 1, "total":1000, "description":" "},
#            "milk":{"price":3, "weigth": 2, "total":500, "description":" "}}
# product_list = [["bread",200],["milk",100]]
# for product,ind in product_list:
#     if product[0] in storage:
#         total = storage[product[0]]["total"]
#         if total >= product[1]:
#             storage[product[0]]["total"] - product[1]
#             check = product[1] * storage[product[0]]["price"]
#             print(f"{product[0]}--{storage[product[0]]['price']}")
#         elif total < product[1]:
#             print("Товара недостаточно")
#
# print(check)










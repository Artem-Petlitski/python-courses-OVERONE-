# Задание 1.Есть словарь необходимо сделать возможность сделать добавление в него чего-нибудь
# storage = {i + 1: {key: input() for key in ['name', 'lastname']} for i in range(3)}
#
# # storage={}
# # for i in range(3):
# #     storage[input("Введите ID")] = \
# #         {
# #         'name': input("Введите имя: "),
# #         'lastname': input("Введите фамилию: "),
# #     }
# print(storage)

# Домашнее Задание 1.  Дан словарь , вводится строка с ключами через запятую, если есть ключ в словаре, выводим ключ-True, если нету -False

# storage = {"price": 1000, "name": "art", "vid": "adsas"}
# str = input("Введите искомые ключи: ").split(',')
# for value in str:
#     if value in storage:
#         print(f"{value}-True")
#     else:
#         print(f"{value}-False")

# Домашнее Задание 2. Даны 2 словаря, объединить два словаря без потери данных.

# storage = {"price": 1000, "name": "art", "vid": "adsas"}
# storage_1 = {"price": 6000, "мф": "art", "фвы": "adsas"}

# for key, val in storage.items():
#     if key in storage_1:
#         storage_1[f"{key}_new"] = val
#     else:
#         storage_1[key] = val
# print(storage)

# Домашнее Задание 3. дан словарь со строковыми значениями. удалить ключи, где значение пустая строка

storage_3 = {"price": "", "name": "art", "vid": "adsas"}
storage_3 = {key: val for key, val in storage_3.items() if val != ""}

# storage_new = {k:v for k,v in storage_3.items() if v != ""}
# print(storage_new)
# print(list(storage_3.items()))
# for key,value in list(storage_3.items()):
#     if value == "":
#         storage_3.pop(key)
print(storage_3)

# users = {i + 1: {key: input() for key in ["name", "lastname"]} for i in range(3)}
# print(users)

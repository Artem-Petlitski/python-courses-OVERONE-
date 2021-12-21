for i in range(100):
    if (i%7==0 and i!=0):
        continue
    print(i,end=" ")
print()
print("----------------------")
stroka=input("Введите строку для проверки: ")
for simvol in stroka:
    if simvol == "q":
        print(".....Выход из программы.....")
        break
else:
    print("Программа успешно отработала,символ q отсутствует.")


i=1
spisok=[]
while i<4:
    num=int(input("Введите четное число [{}]: ".format(i)))
    if (num%2==0):
        spisok.append(num)
        i+=1

print("Задание 1: {}".format(spisok),end=" ")
print()
result=0;
spisok2=[]
length2=int(input("Введите размер списка: "));
i=0;
result_proizv=1 # произведение
while i<length2:
    num1=int(input("Введите элемент списка: "))
    spisok2.append(num1)
    i+=1
for number in spisok2:
    result+=number
print("Сумма элементов списка: {}".format(result))
spisok3=[]
length=int(input("Введите размер списка: "));
i=0;
result_proizv=1 # произведение
while i<length:
    num1=int(input("Введите элемент списка: "))
    spisok3.append(num1)
    i+=1
min_elem=spisok3[0]
for number1 in spisok3:
    result_proizv*=number1
    if(number1<min_elem):
        min_elem=number1

print("Произведение элементов списка:{}".format(result_proizv))
print("Минимальный элемент списка:{}".format(min_elem))



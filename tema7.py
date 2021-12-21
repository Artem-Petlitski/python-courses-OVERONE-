A = (13, 5, 43, 49, 67, 32, 12, 98, 6, 10, 34, 20, 55, 68, 14, 60, 14)
B = (53, 21, 4, 23, 76, 3, 43, 12, 54, 342, 21)
sum1=0
min_num1=A[0]
sum2=0
min_num2=B[0]
res=1
for a in A:
    sum1+=a
    res=res*a
    if a<min_num1:
        min_num1=a
print(res)
for b in B:
    sum2+=b
    res=res*b
    if b < min_num2:
        min_num2 = b
if(sum1>sum2):
    print("Сумма элементов первого кортежа больше суммы элементов второго кортежа")

elif(sum2>sum1):
    print("Сумма элементов второго кортежа больше суммы элементов первого кортежа")
else:
    print("Суммы кортежей равны.")
print("Минимальный элемент первого кортежа: {}".format(min_num1))
print("Минимальный элемент второго кортежа: {}".format(min_num2))
print("Произведение элементов двух кортежей: {}".format(res))



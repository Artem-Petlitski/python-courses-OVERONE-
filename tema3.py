i=2;
result1=1;
while i<=20:
    result1*=i;
    i+=2;
print("Результат выполнения первого задания: "+str(result1));
print("Результат выполнения второго задания: ", sep=" ");
i=15;
while i>0:
    print(i,end=' ');
    i-=1;
print();

num_dip1=int(input("Введите первое число из диапазона: "));
num_dip2=int(input("Введите второе  число из диапазона: "));
if (num_dip1<num_dip2):
    print("Результат выполнения третьего задания: ");
    while num_dip1<num_dip2:
        if(num_dip1<0):
            print(num_dip1,end=" ")
        num_dip1+=1;
elif (num_dip1==num_dip2):
    print("Числа равны");
elif(num_dip1>0 and num_dip2>0):
    print("Оба числа положительны.")
else:
     print("Результат выполнения третьего задания: ");
     while (num_dip2<num_dip1):
         if (num_dip2 < 0):
            print(num_dip2, end=" ");
         num_dip2 += 1;




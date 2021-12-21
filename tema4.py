stroka=input("Введите строку: ");
simvol=input("Введите символ,который будем исключать из строки: ");
for sim in stroka:
    if(sim!=simvol):
        print(sim,end="")
print()
print("--------------------------");
num_begin=int(input("Введите число начала последовательности: "));
num_end=int(input("Введите число конца последовательности: "));
num_step=int(input("Введите шаг последовательности: "))
for i in range(num_begin,num_end,num_step):
    print(i,end=" ")
print()
print("--------------------------");
for i in range(54,170,5):
    print(i,end=",")

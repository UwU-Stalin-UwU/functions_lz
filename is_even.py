def even(a):                         #Функция проверки на четность
    if a%2==0 : return 1
    elif a%2==1 : return 2


print("Введите число для проверки на четность: ") #Ввод
num=input()
num=int(num)
check=even(num)                       #Использование функции
if check==1 : print("Число четно")    #Вывод
elif check==2 : print("Число нечетно")
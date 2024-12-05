def sumdigits(a):                          #Функция нахождения суммы цифр числа
    list_1=[0]*255
    for i in range (0, 254):               #Разделение числа на цифры
        list_1[i]=a%10
        a=a/10
        a=int(a)
    sum=0
    for i in list_1:                       #Поиск суммы
        sum=sum+i
    return sum


print("Введите число для поиска суммы его цифр: ") #Ввод
ch=input()
ch=int(ch)
sum=sumdigits(ch)                                  #Использование функции
print("Сумма цифр данного числа:", sum)            #Вывод
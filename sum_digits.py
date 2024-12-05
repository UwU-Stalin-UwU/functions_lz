def sumdigits(a):                          #Функция нахождения суммы цифр числа
    aa=list(a)
    for i in range (0, len(aa)):
        aa[i]=int(aa[i])
    sum=0
    for i in aa:
        sum=sum+i
    return sum


print("Введите число для поиска суммы его цифр: ") #Ввод
ch=input()
sum=sumdigits(ch)                                  #Использование функции
print("Сумма цифр данного числа:", sum)            #Вывод
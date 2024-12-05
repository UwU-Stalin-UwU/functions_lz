def sec(a, b, c):                 #Функция перевода введенного времени в секунды 
    sum=0
    sum=a*3600+b*60+c
    return sum


print("Введите время в формате <Часы-Минуты-Суекунды>: ") #Ввод
vremya=input()
ch, mn, sc=vremya.split("-")       #Разделение строки 
ch, mn, sc=int(ch), int(mn), int(sc)
timeinsec=sec(ch, mn, sc)          #Использование функции
print("Время в секундах: ",timeinsec) #Вывод
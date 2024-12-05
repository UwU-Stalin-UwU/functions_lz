def plosh(a):        #Функция для поиска площади
    pl=a*a*3.14
    return pl

 
def dlina(a):        #Функция поиска длины
    dl=2*a*3.14
    return dl


print("Введите радиус: ") #Ввод
rad=input()
rad=int(rad)
pl=plosh(rad)             #Использовние функций
dl=dlina(rad)
print("Длина этой окружности:", dl)    #Вывод
print("Площадь этой окружности:", pl)
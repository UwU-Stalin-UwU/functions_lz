def palindrom(a):
    list_1=list(a)
    j=len(list_1)
    pr=0
    if j%2!=0 : j+=1
    for i in range(0, int(j/2)):
        if list_1[i]!=list_1[j] : pr=1
    return pr


stroka=input()
prov=palindrom(stroka)
if prov==1 : print("1")
else : print("2")
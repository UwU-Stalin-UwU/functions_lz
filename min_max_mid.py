def minimal(a):
    minim=a[0]
    for i in a:
        if i<minim : minim=i
    return minim


def maximal(a):
    maxim=a[0]
    for i in a:
        if i>maxim : maxim=i
    return maxim


def sredn(a):
    c=minimal(a)
    d=maximal(a)
    sr=(c+d)/2
    prov=i-a[0]
    if prov<0 : prov=prov*(-1) 
    sredn=a[0]
    for i in a:
        pr=i-sr
        if pr<0 : pr=pr*(-1)
        if pr<prov: 
            sredn=i
            prov=pr
    return sr


a=[input()]
minim=minimal(a)
maxim=maximal(a)
print(minim)
print(maxim)
def bijele (lista):
    tabl = [1,1,2,2,2,8]
    lres = [0,0,0,0,0,0]
    for i in range(6):
        lres[i] = tabl[i]-lista[i]
    return lres
#print(bijele([1,0,3,1,0,20]))
def desmembrarNumero(num):
    lres = []
    while (num >= 1):
        lres.insert(0,num%10)
        num/=10
    return lres

def multiplicacionVacuna(a, b):
    la = desmembrarNumero(a)
    lb = desmembrarNumero(b)
    res = 0
    for va in la:
        for vb in lb:
            res+=va*vb
    return res

def multiplicacionVacunaS(a, b):
    sa = str(a)
    sb = str(b)
    res = 0
    for va in sa:
        for vb in sb:
            res+=int(va)*int(vb)
    return res

#print (multiplicacionVacunaS(12,3))

# Recursividad
def factorial (num):
    if (num == 1 or num == 0):
        return 1
    else:
        return num * factorial(num-1)

print (factorial(900))




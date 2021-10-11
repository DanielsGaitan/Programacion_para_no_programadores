'''def sumatoria(a):
    sum = 0
    for i in range(a):
        sum += (i + 1)
    return sum

def sumat(b):
    sumat = 0
    cont = 0
    while cont < b:
        sumat += cont + 1
        cont += 1
    return sumat

print(sumat(5))
print(sumatoria(5))
#Puedo tener una variable local llamada suma y una función del mismo nombre
'''
def contar(n):
    cifras = 1
    unidadDecimal = '9'
    cond = True
    while True:
        if n > int(unidadDecimal):
            cifras += 1
            unidadDecimal += '9'
        else:
            break
    return cifras
#print(len(list(str(3442))))
#print(contar(354))

def contPares(n):
    c = 0
    while n!= 0:
        if (n-((n//10)*10)) % 2 == 0:
            c += 1
        n //= 10
    return c
#print(contPares(32329164))

def secuencia(n):
    while n != 1:
        print(n, end=', ')
        if n % 2 == 0:
            n /= 2
        else:
            n = 3*n + 1
    return n
secuencia(50)
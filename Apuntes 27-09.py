import time

def sumar (numero):
    suma = 0
    for i in range (numero+1):
        suma+=i
    return suma
hasta =  1000000

t_ini = time.process_time()
resultado = sumar(hasta)
t_fin = time.process_time()
print(t_fin - t_ini)


t_ini2 = time.process_time()
resultado = sum(range(hasta+1))
t_fin2 = time.process_time()
import mi_modulo
print(mi_modulo.saludo)
a = "los pollitos dicen pio pio"
print(mi_modulo.contar(a))
print(mi_modulo.leer())
print(t_fin2 - t_ini2)

'''
ar = open("texto.txt", "r")
nuevo = open("ejemplo.txt", "w")
text = ar.readlines()
for i in text:
    print(i)
    if "w" in i or "W" in i:
        nuevo.write(i)
ar.close()
nuevo.close()'''
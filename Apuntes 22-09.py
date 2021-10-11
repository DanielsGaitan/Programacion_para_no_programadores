'''texto = "Hoy es viernes y el cuerpo lo sabe"
print(texto.split())
texton = texto.split()
print(".,*".join(texton))
def cont_palabras(a):
    lista = []
    for i in a.split():
        lista.append((i, len(i)))
    return lista
print(cont_palabras("corazón de melón"))
#diccionario, son modificables, no se ingresa por el índice sino por la clave
#o key
diccionario = {1:"uno", 2:"dos", 3:"tres", 4:"cuatro", 5:"cinco"}
print(diccionario.values())
diccionario_spa_eng = {"uno":"one", "dos":"two", "tres":"three",
                       "cuatro":"four", "cinco":"five"}
diccionario_spa_eng["seis"]="six"
print(diccionario_spa_eng)
print(diccionario_spa_eng)
del diccionario_spa_eng["seis"]
print(diccionario_spa_eng)
diccionario_spa_eng["uno"] = "uan" #No puede haber dos keys
print(diccionario_spa_eng)
#pide una fruta y su cantidad y las vaya agregando
inventario = {}
while True:
    entrada = input("Ingrese la fruta, o 'fin' si la finalizó \t")
    if entrada.lower() != "fin":
        inventario[entrada] = int(input(f"Ingrese las cantidades de {entrada} \t"))
    else:
        break
print(inventario) #Retorna los items a modo de tuplas
inventariofin = {'Peras': 34, 'Manzanas': 10, 'Mangos': 4,
                 'Limones': 35, 'Lychees': 45, 'Cocos': 10}
suma = 0
for i in inventariofin.values():
    suma += i
print(f"Hay {suma} frutas")
#cuando a una variable le asigno otra que tiene  un diccionario, hay una asignación por
#referencia, para crear un clon
inventaario = inventariofin.copy()
#Función que reciba un texto y cuente cuantos caracteres hay de cada
texto = input("Ingrese la cadena \n")
letras = {}
for i in texto:
    try:
        letras[i]
    except KeyError:
        letras[i] = 1
    else:
        letras[i] += 1
print(letras)'''
def cont_pal(texto):
    palabras = {}
    for i in texto.split():
        if i not in palabras:
            palabras[i] = 1
        else:
            palabras[i] += 1
    return palabras
print(cont_pal("mi nombre es Santiago Gaitan soy de Colombia Colombia es un país de América soy de Bogotá Bogotá es un departamento de Colombia"))
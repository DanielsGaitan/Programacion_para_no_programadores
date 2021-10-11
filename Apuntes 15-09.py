mensaje = "Hola mundo"
print('f' in mensaje)
print('f' not in mensaje)
mensaje_sin_vocales = ""
'''
for i in mensaje:
    if i.upper() == "A" or i.upper() == "E" or i.upper() == "I" or i.upper() == "O" or i.upper() == "U":
        continue
    mensaje_sin_vocales += i
mensaje = mensaje.replace("a", "")
mensaje =mensaje.replace("A", "")
mensaje =mensaje.replace("e", "")
mensaje =mensaje.replace("E", "")
mensaje =mensaje.replace("i", "")
mensaje =mensaje.replace("I", "")
mensaje =mensaje.replace("o", "")
mensaje =mensaje.replace("O", "")
mensaje =mensaje.replace("u", "")
mensaje =mensaje.replace("U", "")
print(mensaje)
for i in mensaje:
    if i in "aeiouAEIOU":
        continue
    else:
        mensaje_sin_vocales += i
print(mensaje_sin_vocales)

def remov(text, character):
    textn = ""
    for i in text:
        if i not in character:
            textn += i
    return textn
print(remov("Corazon de melon", "o"))
print(mensaje.find("o"))
print(mensaje.split())
'''
nombre, apellido, edad = "Santiago", "Gaitán", 16
msn = f"Hola, mi nombre es {nombre} mi apellido es {apellido} y tengo {edad} años"
nombres = ["andres", "angela", "julian", "adrian", "miguel"]
for i in nombres:
    message = "Hola {0} bienvenido a mi clase de programación".format(i)
    print(message)
for i in range (1, 11):
    linea = "{0:>4}\t{1:>8}\t{2:>12}\t".format(i, pow(i,2), pow(i,3))
    linea = f"{i:>4}\t{i ** 2:>8}\t{i ** 3:>12}\t"
    #Son equivalentes
    print (linea)

#Tuplas, son como cadenas de caracteres, son un objeto compuesto que no se puede modificar, inmutable
#Las tuplas son útiles en tanto se puede empaquetar y desempaquetar informacion
'''frutas = [("Pera", 5), ("Mango", 6), ("Uva", 10)]
for i in frutas:
    print(i) #Imprime las tuplas
for (fruta, cantidad) in frutas:
    print(F"De la {fruta} hay {cantidad} unidades")
personas = [("Daniela", "Valderrama", 17),
           ("Julián", "Parra", 20),
           ("Santiago", "Gaitán", 16),]
for (name, lastname, age) in personas:
    print("Te llamas {0}, te apellidas {1} y tienes {2} años".format(name, lastname, age))

print(personas[0]+frutas[1])
'''
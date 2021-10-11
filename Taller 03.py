#punto 1
print("Punto 1")
mensaje = "Su nombre es " + input("Ingrese su nombre: ") + " y tiene " + input("Ahora su edad: ") + " años"
print(mensaje)

#punto 2
print("Punto 2")
print(6 * (1-2))

#punto 3
print("Punto 3")
t = int(input("Ingrese número de años: "))
print("La cantidad de interés es", 10000*((1+(0.08/12))**(12*t)), "pasados", t, "años")

#punto 4
print ('#')
print ("El intérprete no ejecuta la función print '#', pues ese es el statement encargado de imprimir cadenas de caracteres o variables en la versión de python 2.x, esa versión fue descontinuada y ahora solo se usa python 3.x, el equvalente es la función print(), con la función equvalente sí se ejecuta correctamente, pues todo lo que se encuentre entre comillas (ya sean dobles o sencillas) se tomará como un caracter o cadena de caracteres, el caracter '#' al estar entre las comillas se toma como caracter y no como token, lo que permite su impresión en pantalla")
print("Para hacer comentarios multilíneas sin usar el sharp, se usan las triples comillas (ya sean dobles o sencillas) para iniciar un bloque de comentario, y para finalizarlo se debe repetir las triples comillas, teniendo la precaución de que si el comentario se inició con triple comilla simple, se debe finalizar con triple comilla simple, no se pueden mezclar")
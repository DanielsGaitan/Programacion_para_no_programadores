'''estudiantes = [("Daniel", ["fisica", "español", "etica"]),
               ("Sergio", ["matem", "musica", "español"]),
               ("Silvia", ["etica", "matem", "quimica"]),
               ("Adrian", ["fisica", "musica", "etica"]),
               ("Angela", ["español", "matem", "quimica"]),
               ("Miguel", ["etica", "musica", "español"])]
count = 0
for (name, subjects) in estudiantes:
    if "español" in subjects:
        count += 1
print(f"De todos los setudiantes, {count} ven español")
vocales = ["a", "e", "i", "o", "u"]
vocales[2:2] = "I"
print(vocales)
vocales [2:4] = ["dos","tres"]
print(vocales)
del vocales[0]
frutas = []
print(frutas)
frutas.append("Papaya")
print(frutas)
frutas.append("Mango")
print(frutas)
frutas.append("uva")
print(frutas)
frutas.insert(1, "zapote")
print(frutas)
print(frutas.count("zapote"))
frutas.sort()
print(frutas)
#Pide números al usuario, cuando quiera terminar de describir los numeros, coloca fin
suma = []
while True:
    entrada = input()
    if entrada == "fin":
        break
    else:
        suma.append(float(entrada))
print(sum(suma))'''
vowels = ["a", "e", "i", "o", "u"]
letters = vowels #Asignación por referencia de datos compuestos Alias se le da un segundo nombre a la misma lista
letters[0] = letters[0].upper()
print(vowels)
clon = vowels[:]#aquí se clona, no se coloca alias
# may 200 rojo
# 100-200 amarillo
#men 100, verde
'''
import turtle
def barra (imagen, to, colour):
    t.color(colour)
    to.begin_fill()
    to.lt(90)
    to.fd(imagen)
    t.color("black")
    to.write(str(imagen), font=("Grand Hotel", 15, "normal"))
    t.color(colour)
    to.rt(90)
    to.fd(30)
    to.rt(90)
    to.fd(imagen)
    to.left(90)
    to.penup()
    to.fd(15)
    to.pendown()
    to.end_fill()
v = turtle.Screen()
t = turtle.Turtle()
t.speed(10)

datos = [48, 75, 121, 135, 154, 162, 183, 150, 220]
for i in datos:
    if i > 200:
        color = "red"
    elif i > 100 and i <= 200:
        color = "yellow"
    elif i <= 100:
        color = "green"
    barra(i,t,color)

#función para escribir texto
#t.write("hola", font=("Grand Hotel", 15, "normal"))

v.mainloop()
v.screensize(5000, 5000)
#########################
car = str(input())
#car = car.upper()

def rotar(cardinal):
    if cardinal == "N" or cardinal == "n":
        print("E")
    elif cardinal == "E" or cardinal == "e":
        print("S")
    elif cardinal == "S" or cardinal == "s":
        print("O")
    elif cardinal == "O" or cardinal == "o":
        print("N")
rotar(car)

def buscar_de (lista):
    cont = 0
    u = 1
    for i in lista:
        cont = i
        if len(i) % 2 == 1:
            break
        u += 1
    return cont, u
l = ["hola", "alumnosi", "de", ]
print(f"La primera palabra impar es {buscar_de(l)[0]} en la posición {buscar_de(l)[1]}")
'''
def meses(mes):
    mes = mes.upper()
    if mes == "ENERO" or mes == "MARZO" or mes == "MAYO" or mes == "JULIO" or mes == "AGOSTO" or mes == "OCTUBRE" or mes == "DICIEMBRE":
        return 31
    elif mes == "FEBRERO":
        return 28
    elif mes == "ABRIL" or mes == "JUNIO" or mes == "SEPTIEMBRE" or mes == "NOVIEMBRE":
        return 30
    else:
        return "No es un mes"
while True:
    a = input()
    print(f"El mes de {a.lower()} {meses(a)}")
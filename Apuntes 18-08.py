#grados celsius
'''
gradosCelcius = float(input("¿Cuántos grados  celcius?"))
farenheit = gradosCelcius * 1.8 +32
print(f"Equivale a { farenheit } farenheit")

palabra = input("Ingrese una palabra para contar los caracteres: ")
print(f"La palabra {palabra} tiene {len(palabra)} caracteres")
import turtle

ventana = turtle.Screen() #instancia la ventana

t = turtle.Turtle() #instancia la tortuga
t.penup()#recoje el lápiz
t.goto(-100, -100)#mueve a la tortuga hasta la coordenada
t.pendown()#raya nuevamente


#t.pensize(1) #grosor
t.pencolor("red") #Color del borde la tortuga
t.color("orange") #color del objeto y trazo
t.speed(1) #velocidad de ta ortuga de 1-10
t.shape("square")#forma de la tortuga


a = 6
#t.begin_fill() #lo que esté entre eso, rellene
for i in range(a):
    t.forward(100)
    t.left(360/a)
    t.stamp()#queda estampada la forma de la tortuga
#t.end_fill()#lo que esté entre eso, rellene
t.penup()
t.goto(-25, -25)
t.pendown()
for i in range(4):
    t.forward(50)
    t.left(360 / 4)
    #t.stamp()
ventana.mainloop()'''
import turtle
v = turtle.Screen()
r = turtle.Turtle()
r.pensize(1)
#r.speed(1)
def cuadrado(numero):
    for i in range(4):
        r.fd(20+numero*20)
        r.lt(90)
def mover():
    r.penup()
    r.rt(90)
    r.fd(10)
    r.rt(90)
    r.fd(10)
    r.rt(180)
    r.pendown()
for i in range(8):
    cuadrado(i)
    mover()

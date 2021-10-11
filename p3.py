import turtle
v = turtle.Screen()
t = turtle.Turtle()
def square(longitud):
    for i in range(4):
        t.fd(longitud)
        t.lt(360/4)
t.pensize(3)
t.speed(10)
#paredes
square(100)
#posición puerta
t.penup()
t.fd(35)
t.pendown()
#puerta
t.color("green")
t.lt(90)
t.fd(40)
t.rt(90)
t.fd(30)
t.rt(90)
t.fd(40)
#posición ventana 1
t.penup()
t.lt(90)
t.fd(35)
t.lt(90)
t.fd(80)
t.lt(90)
t.fd(10)
t.pendown()
#ventana 1
t.color("blue")
square(30)
#posición ventana 2
t.penup()
t.fd(50)
t.pendown()
#ventana 2
square(30)
#posición techo
t.penup()

t.fd(40)
t.rt(90)
t.fd(20)
t.pendown()
#techo
t.rt(30)
t.color("red")
t.fd(100)
t.rt(120)
t.fd(100)
v.mainloop()
'''import turtle
v = turtle.Screen()
t = turtle.Turtle()
t.speed(10)
def square():
    for i in range(30):
        for j in range(4):
            t.fd(100)
            t.lt(90)
        t.lt(360/30)
square()
v.mainloop()'''
def par(n):
    if n % 2 == 0:
        print("Es par")
par(int(input("Ingrese numero ")))
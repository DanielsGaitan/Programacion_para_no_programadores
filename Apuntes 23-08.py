'''lista = ["Daniel", "Andrés", "Daniela", "Silvia"]
for i in lista:
    print(f"{i}, te invito a tomar un café a Juan Valdez")
edades = [16, 21, 22, 17, 20, 21, 20, 23, 39]
suma = 0
cont = 0
for i in edades:
    suma = pow(i,2) + suma
    cont += 1

print(suma)
print(cont)
print(suma/cont)'''
import turtle
def triangle(lado):
    for i in range(3):
        t.fd(lado)
        t.lt(360/3)
v = turtle.Screen()
t = turtle.Turtle()
long = 10
t.speed(10)
for i in range(30):
    triangle(long)
    t.fd(long)
    t.rt(50)
    long += 3
v.mainloop()
#11-08-2021
import math

"""
+ Los decimales se representan con coma y no con punto
+ Para representar un string de varias líneas se usan las triples
comillas o los triples apóstrofes
"""
type (snake_case_variable) #la función type() arroja el tipo de dato
str(12)#castear datos x --> string
int("12") #castear x *condicionado* --> integer
float(12) #castea x *str que represente decimal e int* --> float
int(3.6) #elimina los decimales, NO REDONDEA, para redondear round()
# el operador // siempre toma el valor menor -15//2 da -8

#years, name = int(input()), input()
#print(f"Te llamas {name} y tienes {years} años")

# ingrese una cantidad de segundos y arroja esa cantidad de segundos en horas
#print(f"La cantidad de horas a las que equivale es: {float(input('Ingresa una cantidad de segundos: '))/3600} horas")
#print(f"La cantidad a la que equivale es: {int(input('Ingresa una cantidad de segundos: '))/3600} horas")

#ingrese el radio y devuelva el área y perímetro
radio = float(input('Ingrese el radio sin hacer uso de unidades de medida: '))
print(f"El área es: {math.pow(radio, 2) * math.pi} unidades cuadradas y el perímetro es: {2*radio*math.pi} unidades")

import turtle
window = turtle.Screen()
juan = turtle.Turtle()
juan.forward(100)
juan.right(45)
juan.color("red")
juan.forward(100)
juan.left(90)
window.mainloop()

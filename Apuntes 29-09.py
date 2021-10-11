"""class Carro:
    def __init__ (self, color = "Azul", marca = "Chevrolet", tracción = "4x2"):
        self.color = color
        self.marca = marca
        self.tracción = tracción
        self.luces = False
        self.km_l = 50
        self.tanque = 100
    def __str__(self):
        return f"{self.km_l}"

    def apagarLuces(self):
        self.luces = False
    def prenderLuces(self):
        self.luces = True
    def recorrido(self, distancia):
        if self.luces:
            self.km_l = 45
        consumo = distancia/self.km_l
        if self.tanque >= consumo:
            self.tanque -= consumo
            return f"Se consumió {consumo} lt"
        else:
            return "No se puede hacer el recorrido, hay muy poco"
    def recargarTanque(self, val):
        if val + self.tanque > 100:
            print("No es posible recargar, el tanque se va a rebosar")
        else:
            self.tanque += val
            print("Tanque recargado")

laNave = Carro(color = "rojo")
print(laNave.tanque)
print(laNave.recorrido(125))
print(laNave.tanque)
laNave.prenderLuces()
print(laNave.recorrido(125))
print(laNave)
NOmbre, apellido, id, saldo
CLiente
"""
class Cliente:
    def __init__(self, n = "nombre", a = "apellido", i = 0, s = 0):
        self.nombre = n
        self.apellido = a
        self.identificación = i
        self.salario = s
    def __str__(self):
        return f"{self.nombre}, {self.apellido}, identificación {self.identificacion}, saldo {self.saldo}"

    def consignar(self, v):
        self.salario += v
        print (f"Su nuevo saldo es {self.salario}")

    def retirar(self, v):
        if self.salario - v > 0
            self.salario -= v
            print(f"El nuevo salario es {self.salario}")
        else:
            print("Es más de lo que hay en la cuenta, es imposible hacer esa operación")

gaitán = Cliente("Daniel Santiago", "Gaitán Calderón", "1011321254", 1000000)

gaitán.consignar(500000)



"""Desarrollar un programa que conste de una clase padre Cuenta y dos subclases
PlazoFijo y CajaAhorro. Definir los atributos titular y cantidad y un método para
imprimir los datos en la clase Cuenta. La clase CajaAhorro tendrá un método para
heredar los datos y uno para mostrar la información.
La clase PlazoFijo tendrá dos atributos propios, plazo e interés. Tendrá un método
para obtener el importe del interés (cantidad*interés/100) y otro método para mostrar
la información, datos del titular plazo, interés y total de interés. Crear al menos un
objeto de cada subclase"""

class cuenta:
    def __init__(self,titular = "",cantidad = 0):
        self.titular = titular
        self.cantidad = cantidad
    def imprimir(self):
        self.titular = input ("ingrese el nombre del titular: ")
        self.cantidad = int(input("ingrese la cantidad: "))
        return f"\nEl nombre del titular es: {self.titular}\nLa cantidad es: {self.cantidad}"

class caja_ahorro(cuenta):
    def __init__(self, titular = "", cantidad = 0):
        super().__init__(titular, cantidad)

class plazo_fijo(cuenta):
    def __init__(self, cantidad = 0 ,titular = "",interes = 0,plazo = 0,importe = 0):
        super().__init__(titular,cantidad)
        self.interes = interes
        self.plazo = plazo
        self.importe = importe
    def importes(self,importe = 0):
        self.interes = int(input("ingrese sus intereses: "))
        self.plazo = int(input("ingrese el plazo: "))
        self.importe = self.cantidad * self.interes/ 100
        return ""
    def imprimir2(self, titular = ""):
        return f"\nEltitular es: {self.titular}\nEl plazo es: {self.plazo}\nEl interes es: {self.interes}\nEl total de intereses es: {self.importe}"

plazo_fijo2 = plazo_fijo()
print (f"{plazo_fijo2.imprimir()}{plazo_fijo2.importes()}{plazo_fijo2.imprimir2()}")
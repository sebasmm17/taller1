"""Realizar un programa que conste de una clase Persona con dos atributos nombre y
edad. Los atributos se introducirán por teclado y habrá otro método para imprimir los
datos. Declarar una segunda clase llamada Empleado que hereda de la clase Persona
y agrega el atributo Sueldo. Debe mostrar si tiene que pagar impuesto o no (sueldo
superior a 3000000)"""

class persona:
    def __init__(self,nombre,edad = 0):
        self.nombre = input("ingrese su nombre completo: ")
        self.edad = int(input("ingrese su edad: "))
    def datos(self):
        return f"\nEste es tu nombre:{self.nombre}\nEsta es tu edad: {self.edad}\n"

class empleado(persona):
    def __init__(self,nombre = "",edad = 0,sueldo = 0):
        persona.__init__(self,nombre,edad)
        self.sueldo = sueldo
    
    def impuesto(self):
        self.sueldo = float(input("ingrese su sueldo: "))
        if self.sueldo > 3000000:
            return f"la persona con el nombre {self.nombre} tiene que pagar impuestos."
        else:
            return f"la persona con el nombre {self.nombre} no necesita pagar impuestos."

persona1 = empleado()
print(f"{persona1.datos()}{persona1.impuesto()}")


"""(HERENCIA) Plantear una clase Persona que contenga dos atributos: nombre y edad. Definir como
responsabilidades la carga por teclado y su impresión.
En el bloque principal del programa definir un objeto de la clase persona y llamar a sus métodos.
Declarar una segunda clase llamada Empleado que herede de la clase Persona y agregue un atributo
sueldo y muestre si debe pagar impuestos (sueldo superior a 3000)
También en el bloque principal del programa crear un objeto de la clase Empleado."""

class Persona:
    def __init__(self,):
        self.nombre = input("Ingrese el nombre: ")
        self.edad = int(input("Ingrese la edad: "))

    def imprimir_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")


class Empleado(Persona):
    def __init__(self, sueldo):
        super().__init__()
        self.sueldo = sueldo

    def pagar_impuestos(self):
        if self.sueldo > 3000:
            print(f"El empleado {self.nombre} debe pagar impuestos.")
        else:
            print("El empleado no debe pagar impuestos.")


persona1 = Persona()
persona1.imprimir_datos()

empleado1 = Empleado(3500)
empleado1.imprimir_datos()
empleado1.pagar_impuestos()
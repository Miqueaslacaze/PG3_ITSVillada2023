"""Plantear una clase Operaciones que solicite en el método __init__ la carga de dos enteros e
inmediatamente muestre su suma, resta, multiplicación y división. Hacer cada operación en otro método de
la clase Operación y llamarlos desde el mismo método __init__"""

class Operaciones:
    def __init__(self):
        self.notauno = int(input("Primer numero: "))
        self.notados = int(input("Segunda numero: "))
        self.suma()
        self.resta()
        self.multi()
        self.division()

    def suma(self):
        print(f"La suma es igual a {self.notauno+self.notados}")

    def resta(self):
        print(f"La resta es igual a {self.notauno-self.notados}")

    def multi(self):
        print(f"La multiplicacion es igual a {self.notauno*self.notados}")

    def division(self):
        print(f"La division es igual a {self.notauno/self.notados}")


operacion1 = Operaciones()
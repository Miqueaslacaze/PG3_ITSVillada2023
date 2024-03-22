"""Desarrollar un programa que cargue los lados de un triángulo e implemente los siguientes métodos:
inicializar los atributos, imprimir el valor del lado mayor y otro método que muestre si es equilátero o no. El
nombre de la clase llamarla Triangulo."""

class Triangulo:
    def __init__(self):
        self.lado_1 = int(input("Ingrese el lado 1: "))
        self.lado_2 = int(input("Ingrese el lado 2: "))
        self.lado_3 = int(input("Ingrese el lado 3: "))
        
    def imprimir_mayor(self):
        lado_mayor = max(self.lado_1, self.lado_2 , self.lado_3)
        print(f"\nEl lado mayor es: {lado_mayor}")

    def equilatero(self):
        if self.lado_1 == self.lado_2 == self.lado_3 :
            print("El triangulo es equilatero.")
        else:
            print("El triangulo no es equilatero.")


triangulo1 = Triangulo()
triangulo1.imprimir_mayor()
triangulo1.equilatero()
"""
) Implementaremos una clase llamada Persona que tendrá como atributo (variable) su nombre y dos
métodos (funciones), uno de dichos métodos inicializará el atributo nombre y el siguiente método mostrará
en la pantalla el contenido del mismo.
Definir dos objetos de la clase Persona.
""" 

class Persona:
    def inicializar(self,nom):
        self.nombre=nom

    def imprimir(self):
        print(f"Nombre", self.nombre)

persona1=Persona()
persona1.inicializar("andy")
persona1.imprimir()

persona2=Persona()
persona2.inicializar("valen")
persona2.imprimir()

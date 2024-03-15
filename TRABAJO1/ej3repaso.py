def rectangulo(ancho, alto, caracter):
    for i in range(alto):
        print(caracter * ancho)
    
ancho = int(input(f"Ingrese el ancho:"))
alto = int(input(f"Ingrese el alto:"))
caracter = str(input(f"Ingrese el caracter:"))

rectangulo(ancho,alto, caracter)
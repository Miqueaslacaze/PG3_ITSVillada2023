def contar_vocales(frase):
    vocales = "aeiouAEIOU"
    cantidad_vocales = 0
    for caracter in frase:
        if caracter in vocales:
            cabtidad_vocales += 1
    return cantidad_vocales
   

frase = str(input(f"Escribe una frase y contare su vocales"))

cantidad = contar_vocales(frase)

print(f"Tu frase tiene {cantidad} de vocales")
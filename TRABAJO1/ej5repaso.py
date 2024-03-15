def es_palindromo(palabra):

    palabra = palabra.lower()  
    return palabra == palabra[::-1]

palabra1 = str(input("dime una palabra y te dire si es un palindromo: "))

if es_palindromo(palabra1):
    print(f"la palabra elegida {palabra1} es un palindromo")
else:
    print(f"la palabra elegida {palabra1} no es un palindromo")

es_palindromo(palabra1)
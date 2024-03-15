def buscar_elemento(lista, elemento):
   
    for i, num in enumerate(lista):
        if num == elemento:
            return i
    return None

def main():
    lista = [8, 12, 9, 45]
    elemento_buscado = int(input("Ingrese el elemento que desea buscar: "))
    indice = buscar_elemento(lista, elemento_buscado)
    if indice is not None:
        print(f"El elemento {elemento_buscado} se encuentra en el índice {indice} de la lista.")
    else:
        print(f"El elemento {elemento_buscado} no se encuentra en la lista.")

if __name__ == "__main__":
    main()


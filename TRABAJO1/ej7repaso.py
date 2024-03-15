def es_numero_step(numero):
    numero_str = str(numero)
    for i in range(len(numero_str) - 1):
        diferencia = abs(int(numero_str[i]) - int(numero_str[i + 1]))
        if diferencia != 1:
            return False
    return True

numero = int(input(f"dime un numero y te dire si un numero step: "))

if es_numero_step(numero):
    print(f"tu numero {numero} es un step")
else:
    print(f"tu numero {numero} no es step")
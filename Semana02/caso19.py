def buscar_edad(edades, objetivo):
    izq = 0
    der = len(edades) -1

    while izq <= der:
        medio = (izq + der) // 2

        if edades[medio] == objetivo:
            return medio
        elif edades[medio] < objetivo:
            izq = medio +1
        else:
            der = medio -1
    return -1

edad = [18, 20, 22, 25, 27, 30, 35]
print(buscar_edad(edad, 35))
def suma_total(lista):
    total = 0
    for numero in lista:
        total += numero
    return total

numeros = [1, 2, 3, 4, 5]
resultado = suma_total(numeros)
print("La suma total es:", resultado)


def contar_positivos(lista):
    contador = 0
    for numero in lista:
        if numero > 0:
            contador += 1
    return contador

numeros = [-2, 0, 3, 5, -1, 4]
resultado = contar_positivos(numeros)
print("La cantidad de números positivos es:", resultado)

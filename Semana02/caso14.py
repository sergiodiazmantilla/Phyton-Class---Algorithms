def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

datos = [5, 3, 8, 1, 2]
print("posicion: ", busqueda_lineal(datos, 8))

"""
if resultado != -1:
    print("Elemento encontrado en el índice: {resultado}")
else:
    print("Elemento no encontrado en la lista.")
"""

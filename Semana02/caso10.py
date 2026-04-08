#Devuelve la posicion del elemento a buscar
def buscar_inicio(lista, objetivo):
    for i in range(len(lista)):
        if lista [i] == objetivo:
            return i
    return -1
datos=[50, 21, 30, 21, 40]
print(buscar_inicio(datos, 21))

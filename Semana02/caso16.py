def busqueda_acotada(lista, objetivo, limite):
    for i in range(min(limite, len(lista))):
        if lista [i] == objetivo:
            return i
    return -1

datos = [3, 6, 9, 12, 15, 18, 21]
print(busqueda_acotada(datos, 15, 5))
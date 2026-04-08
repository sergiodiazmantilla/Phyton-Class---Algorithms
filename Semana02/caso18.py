def busqueda_binaria_iteractiva(lista, objetivo):
    izquierda = 0
    derecha = len(lista) -1
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2

        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio +1
        else:
            derecha = medio -1
    
    return -1

datos = [2, 5, 8, 12, 16, 23, 30]
print(busqueda_binaria_iteractiva(datos, 2))

#Binaria busca en listas ordenadas, sin embargo la lineal busca en todo

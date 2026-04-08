#busqueda binnaria recursiva

def busqueda_binaria(lista, objetivo, izq, der):
    if izq > der:
        return -1
    
    medio = (izq + der) //2

    if lista[medio] == objetivo:
        return medio
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista,  objetivo, medio +1, der)
    else:
        return busqueda_binaria(lista,  objetivo, izq, medio -1)
    
datos = [1, 2, 3, 5, 7, 9]
print(busqueda_binaria(datos, 7, 0, len(datos) -1))


def busqueda_binaria_recursiva(lista, objetivo, izquierda, derecha):
    if izquierda > derecha:
        return -1
    
    medio =(izquierda + derecha) // 2

    if lista[medio] == objetivo:
        return medio
    
    elif lista[medio] < objetivo:
        return busqueda_binaria_recursiva(lista,  objetivo, medio +1, derecha)
    else:
        return busqueda_binaria_recursiva(lista,  objetivo, izquierda, medio -1)
    
datos = [1, 4, 7, 9, 13, 18, 21]
print(busqueda_binaria_recursiva(datos, 1, 0, len(datos) -1))
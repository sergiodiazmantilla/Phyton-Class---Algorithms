def busqueda_binaria_recursiva(lista, objetivo, izquierda, derecha): 
    if izquierda > derecha: 
        return -1 
 
    medio = (izquierda + derecha) // 2 
 
    if lista[medio] == objetivo: 
        return medio 
    elif lista[medio] < objetivo: 
        return busqueda_binaria_recursiva(lista, objetivo, medio + 1, derecha) 
    else: 
        return busqueda_binaria_recursiva(lista, objetivo, izquierda, medio - 1) 
 
productos = [1001, 1005, 1010, 1018, 1020, 1035, 1040, 1055] 
codigo = 1020 
 
posicion = busqueda_binaria_recursiva(productos, codigo, 0, len(productos) - 1) 
 
if posicion != -1: 
    print("Producto encontrado en la posición:", posicion) 
else: 
    print("Producto no encontrado") 
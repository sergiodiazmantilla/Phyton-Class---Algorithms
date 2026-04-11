def busqueda_binaria_recursiva(lista, objetivo, izquierda, derecha):
    if izquierda > derecha:
        return -1  # No encontrado

    medio = (izquierda + derecha) // 2

    if lista[medio] == objetivo:
        return medio  # Elemento encontrado
    elif lista[medio] < objetivo:
        return busqueda_binaria_recursiva(lista, objetivo, medio + 1, derecha)
    else:
        return busqueda_binaria_recursiva(lista, objetivo, izquierda, medio - 1)


# Ejemplo de uso 01
cadenas = ["Producto 1", "Producto 2", "Producto 3", "Producto 4", "Producto 5"]
productos = [1001, 1002, 1003, 1004, 1005]
codigo_cad = "Producto 3"
codigo_prod = 1003

posicion = busqueda_binaria_recursiva(productos, codigo_prod, 0, len(productos) - 1)

if posicion != -1:
    print(f"El código '{codigo_prod}' se encuentra en la posición: {posicion}")
else:
    print(f"El código '{codigo_prod}' no se encuentra en la lista de productos.")

#Modificar tipo de dato a entero para codigo_cad


# Ejemplo de uso 02
#if __name__ == "__main__":
#    lista_ordenada = [1, 3, 5, 7, 9, 11, 13]
#    objetivo = 7
#    resultado = busqueda_binaria_recursiva(lista_ordenada, objetivo, 0, len(lista_ordenada) - 1)

#    if resultado != -1:
#        print(f"Elemento {objetivo} encontrado en el índice: {resultado}")
#    else:
#        print(f"Elemento {objetivo} no encontrado en la lista.") 



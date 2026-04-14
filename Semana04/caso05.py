def busqueda_binaria(lista, objetivo):
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2

        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1

precios = [3.50, 5.49, 7.25, 8.75, 10.99, 12.00]
objetivo = 8.75
indice = busqueda_binaria(precios, objetivo)

if indice != -1:
    print(f"El precio {objetivo} se encuentra en el índice {indice}.")
else:
    print(f"El precio {objetivo} no se encuentra en la lista.")

#Aplicaciones
#1. Buscar un producto por su precio en una tienda
#2. Buscar una calificación específica de un estudiante
#3. Buscar un tiempo de respuesta específico en un sistema
#4. Buscar una fecha de evento específica
#5. Buscar un nombre específico de persona o lugar
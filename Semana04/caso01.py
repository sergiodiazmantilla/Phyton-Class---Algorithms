def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    medio = len(lista) // 2
    izquierda = merge_sort(lista[:medio])
    derecha = merge_sort(lista[medio:])

    return merge(izquierda, derecha)

def merge(izquierda, derecha):
    resultado = []
    i = j = 0

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])

    return resultado

pedidos = [5, 2, 9, 1, 5, 6, 400, 345, 3, 2, 1, 0]
print("Ordenados:", merge_sort(pedidos))

# Aplicaciones
# 1. Ordenar una lista de nombres de estudiantes
# 2. Ordenar una lista de productos por precio
# 3. Ordenar una lista de fechas
# 4. Ordenar una lista de calificaciones de estudiantes
# 5. Ordenar una lista de tareas por prioridad
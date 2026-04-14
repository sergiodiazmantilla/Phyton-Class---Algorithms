def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    menores = [x for x in arr if x < pivot]
    iguales = [x for x in arr if x == pivot]
    mayores = [x for x in arr if x > pivot]
    return quicksort(menores) + iguales + quicksort(mayores)

precios = [10.99, 5.49, 3.50, 8.75, 12.00]
print("Precios originales:", precios)
precios_ordenados = quicksort(precios)
print("Precios ordenados:", precios_ordenados)

#Aplicaciones
#1. Ordenar una lista de precios de productos en una tienda.
#2. Ordenar una lista de calificaciones de estudiantes.
#3. Ordenar una lista de edades de personas en un grupo.
def merge_sort(lista): 
    if len(lista) <= 1: 
        return lista 
 
    medio = len(lista) // 2 
    izquierda = merge_sort(lista[:medio]) 
    derecha = merge_sort(lista[medio:]) 
 
    return merge(izquierda, derecha) 
 
def merge(izquierda, derecha): 
    resultado = [] 
    i = 0 
    j = 0 
 
    while i < len(izquierda) and j < len(derecha): 
        if izquierda[i] <= derecha[j]: 
            resultado.append(izquierda[i]) 
            i += 1 
        else: 
            resultado.append(derecha[j]) 
            j += 1 
 
    while i < len(izquierda): 
        resultado.append(izquierda[i]) 
        i += 1 
 
    while j < len(derecha): 
        resultado.append(derecha[j]) 
        j += 1 
 
    return resultado 
 
def heapify(lista, n, i): 
    mayor = i 
    izquierda = 2 * i + 1 
    derecha = 2 * i + 2 
 
    if izquierda < n and lista[izquierda] > lista[mayor]: 
        mayor = izquierda 
 
 
    if derecha < n and lista[derecha] > lista[mayor]: 
        mayor = derecha 
 
    if mayor != i: 
        lista[i], lista[mayor] = lista[mayor], lista[i] 
        heapify(lista, n, mayor) 
 
def heap_sort(lista): 
    n = len(lista) 
 
    for i in range(n // 2 - 1, -1, -1): 
        heapify(lista, n, i) 
 
    for i in range(n - 1, 0, -1): 
        lista[0], lista[i] = lista[i], lista[0] 
        heapify(lista, i, 0) 
 
    return lista 
 
# Programa principal 
datos = [38, 27, 43, 3, 9, 82, 10] 
 
print("Lista original:", datos) 
 
resultado_merge = merge_sort(datos[:]) 
resultado_heap = heap_sort(datos[:]) 
 
print("Ordenado con Merge Sort:", resultado_merge) 
print("Ordenado con Heap Sort:", resultado_heap) 
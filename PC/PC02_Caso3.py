import time 
import random 
 
# ========================= 
# MERGE SORT 
# ========================= 
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
 
 
    resultado.extend(izquierda[i:]) 
    resultado.extend(derecha[j:]) 
    return resultado 
 
# ========================= 
# HEAP SORT 
# ========================= 
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
 
    # Construir heap 
    for i in range(n // 2 - 1, -1, -1): 
        heapify(lista, n, i) 
 
    # Extraer elementos 
    for i in range(n - 1, 0, -1): 
        lista[0], lista[i] = lista[i], lista[0] 
        heapify(lista, i, 0) 
 
    return lista 
 
# ========================= 
# PROGRAMA PRINCIPAL 
# ========================= 
# Generar datos aleatorios 
datos = [random.randint(1, 100) for _ in range(10)] 
 
print("=" * 50) 
print("COMPARACIÓN: HEAPSORT vs MERGESORT") 
print("=" * 50) 
 
print("Lista original:", datos) 
print() 
 
# -------- MergeSort -------- 
inicio_merge = time.time() 
resultado_merge = merge_sort(datos[:]) 
fin_merge = time.time() 
 
# -------- HeapSort -------- 
inicio_heap = time.time() 
resultado_heap = heap_sort(datos[:]) 
fin_heap = time.time() 
 
# ========================= 
# REPORTE 
# ========================= 
print("{:<15} {:<25}".format("ALGORITMO", "RESULTADO")) 
print("-" * 50) 
 
print("{:<15} {:<25}".format("MergeSort", str(resultado_merge))) 
print("{:<15} {:<25}".format("HeapSort", str(resultado_heap))) 
 
print("-" * 50) 
 
print("{:<15} {:.8f}".format("Tiempo Merge:", fin_merge - inicio_merge)) 
print("{:<15} {:.8f}".format("Tiempo Heap:", fin_heap - inicio_heap)) 
 
print("=" * 50) 
# Redes de ordenación
# Concepto
'''
Las redes de ordenación usan comparadores para ordenar datos en paralelo.
Ejemplo en Python: Bitonic Sort
'''

# Explicacion
'''
Este código implementa Bitonic Sort, 
donde los datos se dividen en sublistas, 
se ordenan de forma ascendente y descendente, 
y luego se combinan. Es adecuado para sistemas paralelos.
'''

def bitonic_sort(arr):
    def compare_and_swap(i, j, up):
        if (arr[i] > arr[j]) == up:
            arr[i], arr[j] = arr[j], arr[i]
    def bitonic_merge(low, cnt, up):
        if cnt > 1:
            mid = cnt // 2
            for i in range(low, low + mid):
                compare_and_swap(i, i + mid, up)
            bitonic_merge(low, mid, up)
            bitonic_merge(low + mid, mid, up)
    def bitonic_sort_rec(low, cnt, up):
        if cnt > 1:
            mid = cnt // 2
            bitonic_sort_rec(low, mid, True)
            bitonic_sort_rec(low + mid, mid, False)
            bitonic_merge(low, cnt, up)
    bitonic_sort_rec(0, len(arr), True)
    return arr
print(bitonic_sort([3, 7, 2, 8, 1, 5, 4, 6]))
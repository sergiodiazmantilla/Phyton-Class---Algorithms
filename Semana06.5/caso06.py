import random

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = random.choice(arr)
    menores = [x for x in arr if x < pivot ]
    iguales = [x for x in arr if x == pivot ]
    mayores = [x for x in arr if x > pivot ]

    return quicksort(menores) + iguales + quicksort(mayores)

arr = [3, 6, 10, 1, 2, 1]

print("Lista Original: ", arr)
print("Lista Ordenada: ", quicksort(arr))

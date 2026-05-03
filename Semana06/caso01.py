import random
def quicksort(arr):
    if len(arr) <=1:
        return arr
    
    pivot = random.choice(arr)
    menor = [x for x in arr if x < pivot]
    igual = [x for x in arr if x == pivot]
    mayor = [x for x in arr if x > pivot]
    return quicksort(menor) + igual + quicksort(mayor)

arr = [3, 6, 8, 10, 1, 2, 1]

print("Lista Original: ", arr)
print("Lista Ordenada: ", quicksort(arr))

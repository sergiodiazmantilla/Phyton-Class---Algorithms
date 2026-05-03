import random

def las_vegas_partition(arr):
    while True:
        pivot = random.choice(arr)
        left  = [x for x in arr if x < pivot]
        right = [x for x in arr if x >= pivot]

        if len(left) < len(arr) and len(right) < len(arr):
            return left + right
        
# Lista de ejemplo
arr = [1, 2, 3, 4, 3,  5, 9, 6, 8]
print("Resultado: ", las_vegas_partition(arr))
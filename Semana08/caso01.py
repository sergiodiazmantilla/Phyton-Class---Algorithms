from multiprocessing import pool
import random

def bitonic_sort(arr):
    def compare_and_awap(i, j, up):
        if (arr[i] > arr[j] == up):
            arr[i], arr[j] = arr[j], arr[i]
    
    def bitonic_merge(low, cnt, up):
        if cnt > 1:
            mid = cnt // 2

            for i in range(low, low + mid):
                compare_and_awap(i, i+mid, up)
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

#-------------------
#Funcion en Paralelo
#-------------------

def merge_lists(l1, l2):
    result = []
    i = j = 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            result.append(l1[i])
            i += 1
        else:
            result.append(l2[j])
            j += 1
    result.extend(l1[i:])
    result.extend(l2[j:])
    return result

#----------------
#Datos de Pedidos
#----------------

server_1 = random.sample(range(1, 100), 8)
server_2 = random.sample(range(1, 100), 8)
server_3 = random.sample(range(1, 100), 8)
server_4 = random.sample(range(1, 100), 8)

print("Pedido Original:\n")

print("Servidor Norte:  ", server_1)
print("Servidor Sur:    ", server_2)
print("Servidor Este:   ", server_3)
print("Servidor Oeste:  ", server_4)

#------------------
#Ordenamiento Local
#------------------

server_1 = bitonic_sort(server_1)
server_2 = bitonic_sort(server_2)
server_3 = bitonic_sort(server_3)
server_4 = bitonic_sort(server_4)

#------------------
#Fusion en Paralelo
#------------------

with pool(2) as pool:
    partial_result= pool.starmap(
        merge_lists,
        [
            (server_1, server_2),
            (server_3, server_4)
        ]
    )

#------------
#Fusion Final
#------------

final_result = merge_lists(
    partial_result[0],
    partial_result[1]
    #partial_result[2],
    #partial_result[3]
)

print("\n Lista Global de Pedidos Ordenados: \n")
print(final_result)
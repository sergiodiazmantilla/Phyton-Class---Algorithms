from multiprocessing import Pool
import random

# =====================================================
# BITONIC SORT
# Algoritmo de ordenamiento basado en Divide y Vencerás
# =====================================================

def bitonic_sort(arr):
    # -------------------------------------------------
    # Compara dos elementos y los intercambia
    # dependiendo del orden deseado:
    # up = True  -> ascendente
    # up = False -> descendente
    # -------------------------------------------------
    def compare_and_swap(i, j, up):
        # Si la condicion se cumple, intercambia valores
        if (arr[i] > arr[j]) == up:
            arr[i], arr[j] = arr[j], arr[i]
    
    # Fusiona secuencias bitónicas
    def bitonic_merge(low, cnt, up):
        # Solo trabaja si hay más de un elemento
        if cnt > 1:
            mid = cnt // 2

            # Compara elementos de ambas mitades
            for i in range(low, low + mid):
                compare_and_swap(i, i+mid, up)
            
            # Fusion recursiva izquierda
            bitonic_merge(low, mid, up)

            # Fusion recursiva derecha
            bitonic_merge(low + mid, mid, up)
    
    # Funcion recursiva principal del Bitonic Sort
    def bitonic_sort_rec(low, cnt, up):
        if cnt > 1:
            # Divide el arreglo en dos partes
            mid = cnt // 2
            # Primera mitad en orden ascendente
            bitonic_sort_rec(low, mid, True)
            # Segunda mitad en orden descendente
            bitonic_sort_rec(low + mid, mid, False)
            # Fusiona ambas partes
            bitonic_merge(low, cnt, up)
    # Inicia el algoritmo desde la posicion 0
    bitonic_sort_rec(0, len(arr), True)

    return arr

#-------------------
# Funcion en Paralelo
# FUNCION DE FUSION
# Une dos listas ya ordenadas
#-------------------

def merge_lists(l1, l2):
    result = []
    # Punteros para recorrer ambas listas
    i = j = 0
    # Recorre ambas listas comparando elementos
    while i < len(l1) and j < len(l2):
        # Agrega el menor elemento
        if l1[i] < l2[j]:
            result.append(l1[i])
            i += 1
        else:
            result.append(l2[j])
            j += 1
    # Agrega elementos restantes de l1
    result.extend(l1[i:])
    # Agrega elementos restantes de l2
    result.extend(l2[j:])
    return result

# Necesario para multiprocessing en Windows
if __name__ == "__main__":
#----------------
# Datos de Pedidos
#----------------

    # Simula pedidos distribuidos en 4 servidores
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
    # Ordenamiento Local
    # Cada servidor ordena sus propios datos
    #------------------

    server_1 = bitonic_sort(server_1)
    server_2 = bitonic_sort(server_2)
    server_3 = bitonic_sort(server_3)
    server_4 = bitonic_sort(server_4)

    #------------------
    # Fusion en Paralelo
    # Se utilizan 2 procesos simultáneos
    #------------------

    with Pool(2) as pool:
        partial_result= pool.starmap(
            merge_lists,
            [
                # Fusion 1
                (server_1, server_2),
                # Fusion 2
                (server_3, server_4)
            ]
        )

    #------------
    #Fusion Final
    # Une los dos resultados parciales
    #------------

    final_result = merge_lists(
        partial_result[0],
        partial_result[1]
    )

    #---------------
    #Resultado Final
    #---------------
    print("\n Lista Global de Pedidos Ordenados: \n")
    print(final_result)
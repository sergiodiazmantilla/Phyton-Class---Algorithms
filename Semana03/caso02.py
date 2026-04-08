#Ruta mas corta entre dos puntos

import heapq

def rutas_minimas(grafo, inicio):
    distancias = {nodo: float ('inf') for nodo in grafo}
    distancias[inicio] = 0

    cola = [(0, inicio)]

    while cola:
        distancia_actual, nodo = heapq.heappop(cola)

        for vecino, peso in grafo[nodo]. items():
            nueva_distancia = distancia_actual + peso
            
            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia
                heapq. heappush(cola, (nueva_distancia, vecino))
    return distancias

grafo = {
    'A':{'B': 4, 'C': 2},
    'B':{'D': 5},
    'C':{'D': 8},
    'D':{}
}
print (rutas_minimas(grafo, 'A'))

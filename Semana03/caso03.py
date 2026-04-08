def sucursal(grafo):
    grafo.sort(key=lambda x: x[2])
    padres = {}

    def find(n):
        if padres[n] != n:
            padres[n] = find(padres[n])
            return padres[n]
        
    def union (a, b):
        padres[find(a)] = find(b)
    
    nodos = set()
    for u, v, _ in grafo:
        nodos.add(u)
        nodos.add(v)
    
    for nodo in nodos:
        padres[nodo] = nodo
    
    resultado = []

    for u, v, peso in grafo:
        if find(u) != find(v):
            union(u, v)
            resultado. append((u, v, peso))

            return resultado

grafo = [
    ('A', 'B', 4),
    ('A', 'C', 2),
    ('B', 'C', 1),
    ('B', 'D', 5),
    ('A', 'D', 8)
]

print (sucursal(grafo))
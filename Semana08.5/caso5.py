# Broadcast - Algoritmos Distribuidos
# Concepto
'''
Un nodo inicial difunde un mensaje 
a todos los demás nodos en la red.
Ejemplo en Python: Broadcast
'''

# Explicacion
'''
Se simula la propagación de un mensaje 
desde un nodo inicial a través de una red.
'''

graph = {'A': ['B', 'C'], 'B': ['D'], 'C': ['D'], 'D': []}

def broadcast(node, message, visited=None):
    if visited is None:
        visited = set()
    if node not in visited:
        print(f"{node} recibió: {message}")
        visited.add(node)
        for neighbor in graph[node]:
            broadcast(neighbor, message, visited)
broadcast('A', "Mensaje global")
# Casos de uso reales
# Concepto
'''
Ejemplo: Consenso en Bases de Datos Distribuidas (ejemplo
similar a Paxos o Raft)
'''

# Explicacion
'''
Evalúa el estado de los nodos para determinar la
disponibilidad en el sistema.
'''

nodes = {"Node1": "Up", "Node2": "Up", "Node3": "Down"}
if all(status == "Up" for status in nodes.values()):
    print("Todos los nodos están disponibles.")
else:
    print("Algunos nodos están fuera de servicio.")
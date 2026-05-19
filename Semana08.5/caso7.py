# Algoritmos distribuidos: consenso
# Concepto
'''
Asegura que todos los nodos acuerden un único valor.
Ejemplo en Python: Consenso Simple
'''

# Explicacion
'''
Se simula un consenso donde la mayoría de los votos
determinan el resultado.
'''

votes = {
    "Node1": "A", 
    "Node2": "A", 
    "Node3": "B"
    }

decision = max(
    set(votes.values()), 
        key=list(votes.values()).count
)
print(f"Consenso alcanzado: {decision}")

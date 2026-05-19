# Token Ring
# Concepto
'''
Un token circula entre nodos conectados, 
asegurando acceso exclusivo a un recurso.
Ejemplo en Python: Token Ring
'''

# Explicacion
'''
El token se mueve cíclicamente entre los nodos,
representando el control del acceso
'''

nodes = ['A', 'B', 'C', 'D']
token = 0
for _ in range(5):
    print(f"Token en: {nodes[token]}")
    token = (token + 1) % len(nodes)
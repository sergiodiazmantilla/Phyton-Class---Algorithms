class linkedlistNode:
    def __init__(self, value):
        self.value = value
        self.next = None
    def _repr_(self):
        return f"Node({self.value})"

# Crear el node inicial
node1 = linkedlistNode(10)

# Dos punteros al mismo nodo
pointer1 = node1
pointer2 = node1

print("Antes del cambio")
print("pointer1: ", pointer1.value)
print("pointer2: ", pointer2.value)

# Modificar desde el puntero

pointer1.value = 80

print("\nDespues del cambio")
print("pointer1: ", pointer1.value)
print("pointer2: ", pointer2.value)

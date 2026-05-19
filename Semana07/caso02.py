# Relaciones entre elementos
'''
personas y amistades
ciudades y carreteras
computadoras y redes
usuarios y seguidores
estaciones y rutas
'''
class grafosnodirigidos:
    def __init__(self):
        self.grafo = {}
    
    def agregar_aristas(self, u, v):
        if u not in self.grafo:
            self.grafo[u] = []
        if v not in self.grafo:
            self.grafo[v] = []
        self.grafo[u].append(v)
        self.grafo[v].append(u)
    
    def mostrar(self):
        for nodo in self.grafo:
            print(f"{nodo} -> {self.grafo[nodo]}")

amigos = grafosnodirigidos()
amigos.agregar_aristas("ana", "Carlos")
amigos.agregar_aristas("Carlos", "Maria")
amigos.agregar_aristas("ana", "Jose")
amigos.mostrar()
        
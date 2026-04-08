def buscar_estudiante_acotado(estudiante, nombre, limite):
    for i in range(min(limite, len(estudiante))):
        if estudiante [i] == nombre:
            return i
    return -1

lista = ["Ana", "Luis", "Pedro", "Carlos", "Rosa", "Laura"]
print(buscar_estudiante_acotado(lista, "Carlos", 4))
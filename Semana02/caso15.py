def buscar_nombre(nombres, objetivo):
    for i in range(len(nombres)):
        if nombres[i] == objetivo:
            return i
    return -1
personas = ["Ana", "Luis", "Pedro", "Carlos", "Rosa", "Laura"]
print("posicion:", buscar_nombre(personas, "Carlos"))
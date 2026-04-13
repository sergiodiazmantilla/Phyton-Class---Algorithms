estudiantes = [
    {"codigo": 101, "nombre": "Juan", "edad": 20},
    {"codigo": 102, "nombre": "María", "edad": 22},
    {"codigo": 103, "nombre": "Pedro", "edad": 19}
]

nombre_buscar = "Pablo"
encontrado = False
for estudiante in estudiantes:
    if estudiante ["nombre"] == nombre_buscar:
        print("Estudiante encontrado:")
        print(estudiante)
        encontrado = True
        break
if not encontrado:
    print("Estudiante no encontrado.")



estudiantes = [
        {"codigo": 101, "nombre": "Juan", "curso": "Python", "ciclo": 1, "nota": 16.5, "promedio": 17.0},
        {"codigo": 102, "nombre": "María", "curso": "Java", "ciclo": 2, "nota": 18.0, "promedio": 18.5},
        {"codigo": 103, "nombre": "Pedro", "curso": "Data Base", "ciclo": 3, "nota": 15.5, "promedio": 16.0}
    ]

#encabezado de la tabla
print("{:<10} {:<15} {:<15} {:<10} {:<10}".format(
    "Codigo", "Nombre", "Curso", "Ciclo", "Nota", "Promedio"
    ))
print("-" * 65)

    #mostrar los estudiantes en formato de tabla
for estudiante in estudiantes:
        print("{:<10} {:<15} {:<15} {:<10} {:<10}".format(
            estudiante["codigo"],
            estudiante["nombre"],
            estudiante["curso"],
            estudiante["ciclo"],
            estudiante["nota"],
            estudiante["promedio"]
        ))

#buscar un estudiante por codigo
codigo_buscar = 102
encontrado = False

for estudiante in estudiantes:
        if estudiante["codigo"] == codigo_buscar:
            print("\n Estudiante encontrado:")
            print("{:<10} {:<15} {:<15} {:<10} {:<10}".format(
                "Codigo", "Nombre", "Curso", "Ciclo", "Nota", "Promedio"
            ))
            print("-" * 65)
            print("{:<10} {:<15} {:<15} {:<10} {:<10}".format(
                estudiante["codigo"],
                estudiante["nombre"],
                estudiante["curso"],
                estudiante["ciclo"],
                estudiante["nota"],
                estudiante["promedio"]
            ))
            encontrado = True
            break

if not encontrado:
        print("Estudiante no encontrado.")
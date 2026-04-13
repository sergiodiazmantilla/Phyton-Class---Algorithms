from datetime import datetime

empleados = [
    {"nombre": "Juan", "edad": 30, "departamento": "Ventas"},
    {"nombre": "María", "edad": 25, "departamento": "Marketing"},
    {"nombre": "Carlos", "edad": 28, "departamento": "Recursos Humanos"}
]

#obtener fecha actual
fecha_actual = datetime.now().strftime("%Y-%m-%d")

#mostrar fecha actual
print("Fecha actual:", fecha_actual)
print()

#encabezados de la tabla
print("{:<10} {:<10} {:<20}".format("Nombre", "Edad", "Departamento"))
print("-" * 40)

#filas de la tabla
for empleado in empleados:
    print("{:<10} {:<10} {:<20}".format(
        empleado["nombre"], 
        empleado["edad"], 
        empleado["departamento"]
    ))    



"""
for empleado in empleados:
    print("Nombre:", empleado["nombre"])
    print("Edad:", empleado["edad"])
    print("Departamento:", empleado["departamento"])
    print()
"""

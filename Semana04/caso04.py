from datetime import datetime
def quicksort_detalle(lista):
    if len(lista) <= 1:
        return lista
    
    pivote = lista[0]
    
    menores = [x for x in lista[1:] if x < pivote]
    iguales = [x for x in lista[1:] if x == pivote]
    mayores = [x for x in lista[1:] if x >= pivote]

    pasos = [{
        "Pivote: {pivote}",
        "Menores: {menores}",
        "Iguales: {iguales}",
        "Mayores: {mayores}"
    }]
    
    izq_ordenada = quicksort_detalle(menores)
    der_ordenada = quicksort_detalle(mayores)

    return izq_ordenada + iguales + der_ordenada

precios = [10.99, 5.49, 3.50, 8.75, 12.00, 7.25]
precios_ordenados = quicksort_detalle(precios)

fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print("-" * 60)
print(" REPORTE DE ORDENAMIENTO QUICKSORT ")
print("-" * 60)
print("Fecha del reporte", fecha)
print("-" * 60)

print("{:>20} | {:>20} | {:>20}".format("Pivote", "Menores", "Mayores"))
print("-" * 60)

pasos = [
    {"Pivote": 10.99, "Menores": [5.49, 3.50, 8.75, 7.25], "Mayores": [12.00]},
    {"Pivote": 5.49, "Menores": [3.50], "Mayores": [8.75, 7.25]},
    {"Pivote": 3.50, "Menores": [], "Mayores": []},
    {"Pivote": 8.75, "Menores": [7.25], "Mayores": []},
    {"Pivote": 7.25, "Menores": [], "Mayores": []},
    {"Pivote": 12.00, "Menores": [], "Mayores": []}
]

for paso in pasos:
    print("{:>20} | {:>20} | {:>20}".format(paso["Pivote"], str(paso["Menores"]), str(paso["Mayores"])))
    print("-" * 60)
print("Precios ordenados:", precios_ordenados)

#Aplicaciones
#1. Ordenar precios de productos en una tienda
#2. Ordenar calificaciones de estudiantes
#3. Ordenar tiempos de respuesta en un sistema
#4. Ordenar fechas de eventos
#5. Ordenar nombres de personas o lugares



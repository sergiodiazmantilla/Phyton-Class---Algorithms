import random

def quicksort_aleatorio(lista):
    if len(lista) <= 1:
        return lista
    
    pivote = random.choice(lista)

    menores = []
    iguales = []
    mayores = []

    for elemento in lista:
        if elemento < pivote:
            menores.append(elemento)
        elif elemento == pivote:
            iguales.append(elemento)
        else:
            mayores.append(elemento)
    return quicksort_aleatorio(menores) + iguales + quicksort_aleatorio(mayores)

productos =[
    {"codigo": 101, "nombre": "Laptop", "precio": 3500},
    {"codigo": 102, "nombre": "Mouse", "precio": 50},
    {"codigo": 103, "nombre": "Teclado", "precio": 150},
    {"codigo": 104, "nombre": "Monitor", "precio": 1000},
    {"codigo": 105, "nombre": "Tablet", "precio": 300}
]
precios = [productos["precio"] for productos in productos]
precios_ordenados = quicksort_aleatorio(precios)

print("\nCaso2: Ordenamiento aleatorio de precios")
print("*" * 50)
print("Precios originales: ", precios)
print("Precios ordenados: ", precios_ordenados)
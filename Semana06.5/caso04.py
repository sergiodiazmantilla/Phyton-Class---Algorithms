import random
def simular_demanda(productos, simulaciones=1000):
    resultados = {}
    for producto in productos:
        nombre = producto["nombre"]
        ventas_simuladas = []

        for _ in range(simulaciones):
            # Simulación probabilística (ventas entre 50% y 150%)
            factor = random.uniform(0.5, 1.5)
            venta = int(producto["demanda_base"] * factor)
            ventas_simuladas.append(venta)
        # Promedio esperado
        demanda_esperada = sum(ventas_simuladas) / simulaciones
        resultados[nombre] = int(demanda_esperada)
    return resultados

def quicksort_productos_desc(lista):
    if len(lista) <= 1:
        return lista
    
    pivote = random.choice(lista)["demanda"]
    mayores, iguales, menores = [], [], []
    for p in lista:
        if p["demanda"] > pivote:
            mayores.append(p)
        elif p["demanda"] == pivote:
            iguales.append(p)
        else:
            menores.append(p)
    return quicksort_productos_desc(mayores) + iguales + quicksort_productos_desc(menores)

productos = [
    {"codigo": 101, "nombre": "Laptop", "precio": 3500, "demanda_base": 80},
    {"codigo": 102, "nombre": "Mouse", "precio": 80, "demanda_base": 200},
    {"codigo": 103, "nombre": "Teclado", "precio": 150, "demanda_base": 150},
    {"codigo": 104, "nombre": "Monitor", "precio": 900, "demanda_base": 120},
    {"codigo": 105, "nombre": "Audífonos", "precio": 120, "demanda_base": 170}
]

demanda_simulada = simular_demanda(productos)

productos_con_demanda = []
for p in productos:
    productos_con_demanda.append({
        "nombre": p["nombre"],
        "precio": p["precio"],
        "demanda": demanda_simulada[p["nombre"]]
    })

ranking = quicksort_productos_desc(productos_con_demanda)

print("\n REPORTE DE DEMANDA Y PRIORIDAD DE VENTA")
print("=" * 60)
print("\nDemanda estimada (Monte Carlo):")

for p in productos_con_demanda:
    print(f"{p['nombre']}: {p['demanda']} unidades")
    print("\nRanking de productos (mayor a menor demanda):")
    print("-" * 60)
for i, p in enumerate(ranking, 1):
    print(f"{i}. {p['nombre']} | Demanda: {p['demanda']} | Precio: S/ {p['precio']}")
    print("=" * 60)

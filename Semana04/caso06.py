from datetime import datetime

def busqueda_binaria_detallada(lista, objetivo):
    izq, der = 0, len(lista) - 1
    pasos = [] # Contador de pasos

    while izq <= der:
        medio = (izq + der) // 2
        
        pasos.append({
            "izquierda": izq,
            "derecha": der,
            "medio": medio,
            "valor_medio": lista[medio]
        })

        if lista[medio] == objetivo:
            return medio, pasos
        elif lista[medio] < objetivo:
            izq = medio + 1
        else:
            der = medio - 1
    return -1, pasos

productos = [
    {"cod": "1001", "nombre": "Laptop", "precio": 1000},
    {"cod": "1002", "nombre": "Smartphone", "precio": 500},
    {"cod": "1003", "nombre": "Tablet", "precio": 300},
    {"cod": "1004", "nombre": "Monitor", "precio": 200},
    {"cod": "1005", "nombre": "Teclado", "precio": 100},
    {"cod": "1006", "nombre": "Ratón", "precio": 50},
    {"cod": "1007", "nombre": "Impresora", "precio": 150},
    {"cod": "1008", "nombre": "Cámara", "precio": 400},
    {"cod": "1009", "nombre": "Auriculares", "precio": 80},
    {"cod": "1010", "nombre": "Altavoces", "precio": 120}
]

ids = [p["cod"] for p in productos]

codigo_buscar = int(input("Ingrese el código del producto a buscar: "))
posicion, pasos = busqueda_binaria_detallada(ids, str(codigo_buscar))
fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print("\n" + "="*80)
print("      REPORTE DE BUSQUEDA BINARIA DE PRODUCTOS")
print("="*80)
print("Fecha de la búsqueda:", fecha)
print("="*80)

print("{:<10} {:<10} {:<10} {:<15}".format(
    "IZQ", "DER", "MEDIO", "VALOR_MEDIO"
    ))
print("-"*80)

for paso in pasos:
    print("{:<10} {:<10} {:<10} {:<15}".format(
        paso["izquierda"], 
        paso["derecha"], 
        paso["medio"], 
        paso["valor_medio"]
    ))
print("="*80)

if posicion != -1:
    productos=productos[posicion]
    print("{:<10} {:<20} {:<10}".format(
        "COD", "NOMBRE", "PRECIO"
    ))
    print("-"*80)
    print("{:<10} {:<20} {:<10}".format(
        productos["cod"], 
        productos["nombre"], 
        productos["precio"]
    ))
else:
    print("Producto no encontrado.")

# Aplicaciones
#1. Ordenar productos por código y buscar un producto específico, mostrando los pasos de la búsqueda.
#2. Buscar un producto por código y mostrar un reporte detallado de los pasos de la búsqueda, incluyendo la fecha y hora de la búsqueda.


"""
# Ordenar productos por código
productos.sort(key=lambda x: x["cod"])
codigo_buscar = "1003"
indice, pasos = busqueda_binaria_detallada([p["cod"] for p in productos], codigo_buscar)
if indice != -1:
    print(f"Producto encontrado: {productos[indice]}")
else:    print("Producto no encontrado.")

# Mostrar los pasos de la búsqueda
print("\nPasos de la búsqueda:")
for paso in pasos:
    print(paso)

"""


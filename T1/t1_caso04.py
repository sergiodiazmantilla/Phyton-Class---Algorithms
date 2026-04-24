"""
Caso práctico Nº04: 
Enunciado del caso propuesto: 

La empresa Distribuidora Nacional Andina se dedica a la distribución de productos a nivel 
nacional y cuenta con múltiples sedes en diferentes ciudades del país: 
Cada sede administra su propio almacén, pero la gerencia central necesita consolidar la 
información para tomar decisiones estratégicas. 

Actualmente, la empresa presenta dificultades en: 
• conocer el estado del inventario en cada sede  
• identificar qué sede tiene mayor volumen de ventas  
• detectar productos con bajo stock a nivel nacional  
• comparar el rendimiento entre sedes  
• realizar búsquedas rápidas de productos en diferentes sedes  
• generar reportes claros y organizados  

Además, cada consulta debe registrar la fecha y hora, para control de auditoría. 
La empresa requiere un sistema que permita visualizar información de forma 
estructurada y registrar la fecha y hora de cada consulta.
"""

from datetime import datetime

sedes = []
busquedas = []

# Crear sede
def registrar_sede():
    nombre = input("Nombre de la sede: ")
    sedes.append({"nombre": nombre, "productos": []})
    print("Sede registrada")

# Registrar producto en sede
def registrar_producto():
    nombre_sede = input("Ingrese sede: ")

    for s in sedes:
        if s["nombre"].lower() == nombre_sede.lower():
            id = int(input("ID: "))
            nombre = input("Nombre producto: ")
            stock = int(input("Stock: "))
            vendidos = int(input("Vendidos: "))

            producto = {
                "id": id,
                "nombre": nombre,
                "stock": stock,
                "vendidos": vendidos
            }

            s["productos"].append(producto)
            print("Producto registrado")
            return

    print("Sede no encontrada")

# Mostrar inventario por sede
def mostrar_sedes():
    for s in sedes:
        print(f"\nSEDE: {s['nombre']}")
        for p in s["productos"]:
            print(p)

# Sede con más ventas
def mejor_sede():
    mejor = None
    max_ventas = 0

    for s in sedes:
        total = sum(p["vendidos"] for p in s["productos"])

        if total > max_ventas:
            max_ventas = total
            mejor = s["nombre"]

    print("Sede con más ventas:", mejor)

# Productos con bajo stock
def bajo_stock():
    print("\nPRODUCTOS CON BAJO STOCK (<5)")

    for s in sedes:
        for p in s["productos"]:
            if p["stock"] < 5:
                print(s["nombre"], "-", p["nombre"], "-", p["stock"])

# Buscar producto en todas las sedes
def buscar():
    dato = input("Buscar por ID o nombre: ")
    encontrado = False

    for s in sedes:
        for p in s["productos"]:
            if str(p["id"]) == dato or p["nombre"].lower() == dato.lower():
                print("Encontrado en sede:", s["nombre"], p)

                busquedas.append({
                    "dato": dato,
                    "fecha": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                })

                encontrado = True

    if not encontrado:
        print("No encontrado")

# Reporte de búsquedas
def reporte():
    print("\nREPORTE DE CONSULTAS")

    for b in busquedas:
        print(b["dato"], "-", b["fecha"])

# Menú
while True:
    print("""
1. Registrar sede
2. Registrar producto en sede
3. Mostrar inventario por sede
4. Sede con más ventas
5. Productos con bajo stock
6. Buscar producto
7. Reporte de consultas
8. Salir
""")

    op = input("Opción: ")

    if op == "1":
        registrar_sede()
    elif op == "2":
        registrar_producto()
    elif op == "3":
        mostrar_sedes()
    elif op == "4":
        mejor_sede()
    elif op == "5":
        bajo_stock()
    elif op == "6":
        buscar()
    elif op == "7":
        reporte()
    elif op == "8":
        break
    else:
        print("Opción inválida")
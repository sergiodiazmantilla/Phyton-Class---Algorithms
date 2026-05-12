"""
Caso práctico Nº03: 
Enunciado del caso propuesto: 

La ferretería El Constructor vende materiales de construcción y herramientas. 

Debido al crecimiento del negocio, presenta problemas en: 
• control del inventario  
• identificación de productos más demandados  
• organización de datos  
• consultas rápidas  
• generación de reportes 
"""

productos = []

# Registrar producto
def registrar():
    id = int(input("ID: "))
    nombre = input("Nombre: ")
    categoria = input("Categoría: ")
    stock = int(input("Stock: "))
    vendidos = int(input("Cantidad vendida: "))

    producto = {
        "id": id,
        "nombre": nombre,
        "categoria": categoria,
        "stock": stock,
        "vendidos": vendidos
    }

    productos.append(producto)
    print("Producto registrado correctamente")

# Mostrar inventario
def mostrar():
    print("\nINVENTARIO")
    print("ID\tNombre\tCategoría\tStock\tVendidos")

    for p in productos:
        print(f"{p['id']}\t{p['nombre']}\t{p['categoria']}\t{p['stock']}\t{p['vendidos']}")

# Producto más demandado
def mas_demandado():
    if productos:
        p = max(productos, key=lambda x: x["vendidos"])
        print("Producto más demandado:", p["nombre"])

# Productos sin stock
def sin_stock():
    print("\nPRODUCTOS SIN STOCK")

    for p in productos:
        if p["stock"] == 0:
            print(p["nombre"])

# Buscar producto
def buscar():
    dato = input("Buscar por ID o nombre: ")
    encontrado = False

    for p in productos:
        if str(p["id"]) == dato or p["nombre"].lower() == dato.lower():
            print("Encontrado:", p)
            encontrado = True

    if not encontrado:
        print("No encontrado")

# Reporte ordenado por stock
def ordenar_stock():
    ordenados = sorted(productos, key=lambda x: x["stock"])
    
    print("\nPRODUCTOS ORDENADOS POR STOCK")
    for p in ordenados:
        print(p["nombre"], "-", p["stock"])

# Menú
while True:
    print("""
1. Registrar producto
2. Mostrar inventario
3. Producto más demandado
4. Productos sin stock
5. Buscar producto
6. Reporte ordenado por stock
7. Salir
""")

    op = input("Opción: ")

    if op == "1":
        registrar()
    elif op == "2":
        mostrar()
    elif op == "3":
        mas_demandado()
    elif op == "4":
        sin_stock()
    elif op == "5":
        buscar()
    elif op == "6":
        ordenar_stock()
    elif op == "7":
        break
    else:
        print("Opción inválida")
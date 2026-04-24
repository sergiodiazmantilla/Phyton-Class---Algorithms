"""
CASO PRACTICO Nº 01: 
Enunciado del caso propuesto: 

La empresa La Bodeguita requiere un sistema en Python para controlar su almacén. El Sistema 
debe registrar productos, mostrar el listado actual, identificar el producto más vendido y el menos 
vendido, verificar el stock disponible, permitir búsquedas por ID o nombre, registrar fecha y hora 
de búsqueda y mostrar la información en tablas ordenadas. Desarrolle una solución en Python 
que cumpla con estos requerimientos y explique la estrategia de programación utilizada. 

• dificultad para conocer el listado actualizado de productos  
• demora para identificar los productos más vendidos  
• poca claridad sobre cuál es el producto menos vendido  
• falta de control del stock disponible  
• dificultad para buscar productos rápidamente  
• ausencia de reportes organizados y fáciles de interpretar 

Además, la gerencia ha solicitado que toda búsqueda realizada por el usuario quede registrada 
con su fecha y hora, de manera que cada consulta pueda ser mostrada como parte de un reporte.
"""

from datetime import datetime

productos = [
    {"id":1, "nombre":"Arroz", "stock":20, "vendidos":50},
    {"id":2, "nombre":"Azúcar", "stock":15, "vendidos":30}
]
busquedas = []

# Registrar producto
def registrar_producto():
    id = int(input("ID: "))
    nombre = input("Nombre: ")
    stock = int(input("Stock: "))
    vendidos = int(input("Cantidad vendida: "))

    producto = {
        "id": id,
        "nombre": nombre,
        "stock": stock,
        "vendidos": vendidos
    }

    productos.append(producto)
    print("Producto registrado correctamente")

# Mostrar productos
def mostrar_productos():
    print("\nLISTA DE PRODUCTOS")
    print("ID\tNombre\tStock\tVendidos")

    for p in productos:
        print(f"{p['id']}\t{p['nombre']}\t{p['stock']}\t{p['vendidos']}")

# Producto más vendido
def mas_vendido():
    mayor = max(productos, key=lambda x: x["vendidos"])
    print("Producto más vendido:", mayor["nombre"])

# Producto menos vendido
def menos_vendido():
    menor = min(productos, key=lambda x: x["vendidos"])
    print("Producto menos vendido:", menor["nombre"])

# Buscar producto
def buscar_producto():
    dato = input("Ingrese ID o nombre: ")

    encontrado = False

    for p in productos:
        if str(p["id"]) == dato or p["nombre"].lower() == dato.lower():
            print("Encontrado:", p)

            fecha = datetime.now()
            busquedas.append({
                "busqueda": dato,
                "fecha": fecha.strftime("%d/%m/%Y %H:%M:%S")
            })

            encontrado = True

    if not encontrado:
        print("No encontrado")

# Ver búsquedas
def ver_busquedas():
    print("\nREPORTE DE BÚSQUEDAS")

    for b in busquedas:
        print(b["busqueda"], "-", b["fecha"])

# Menú
while True:
    print("""
1. Registrar producto
2. Mostrar productos
3. Producto más vendido
4. Producto menos vendido
5. Buscar producto
6. Ver reporte búsquedas
7. Salir
""")

    op = input("Opción: ")

    if op == "1":
        registrar_producto()
    elif op == "2":
        mostrar_productos()
    elif op == "3":
        mas_vendido()
    elif op == "4":
        menos_vendido()
    elif op == "5":
        buscar_producto()
    elif op == "6":
        ver_busquedas()
    elif op == "7":
        break
    else:
        print("Opción incorrecta")

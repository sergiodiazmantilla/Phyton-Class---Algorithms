"""
Caso práctico Nº02: 
Enunciado del caso propuesto: 

La farmacia total libertad maneja una gran variedad de medicamentos y productos 
farmacéuticos. Debido al aumento en la demanda, la empresa presenta dificultades para: 

• controlar el stock de medicamentos  
• identificar los medicamentos más vendidos  
• detectar productos próximos a vencerse  
• consultar información de manera rápida  
• organizar reportes de ventas  

Además, la farmacia requiere que cada búsqueda realizada registre la fecha y hora, para 
fines de control interno.
"""

from datetime import datetime

medicamentos = []
busquedas = []

# Registrar medicamento
def registrar():
    id = int(input("ID: "))
    nombre = input("Nombre: ")
    stock = int(input("Stock: "))
    vendidos = int(input("Cantidad vendida: "))
    vencimiento = input("Fecha de vencimiento (dd/mm/yyyy): ")

    med = {
        "id": id,
        "nombre": nombre,
        "stock": stock,
        "vendidos": vendidos,
        "vencimiento": vencimiento
    }

    medicamentos.append(med)
    print("Medicamento registrado")

# Mostrar lista
def mostrar():
    print("\nLISTA DE MEDICAMENTOS")
    print("ID\tNombre\tStock\tVendidos\tVencimiento")

    for m in medicamentos:
        print(f"{m['id']}\t{m['nombre']}\t{m['stock']}\t{m['vendidos']}\t{m['vencimiento']}")

# Más vendido
def mas_vendido():
    if medicamentos:
        m = max(medicamentos, key=lambda x: x["vendidos"])
        print("Más vendido:", m["nombre"])

# Próximos a vencer
def proximos_vencer():
    hoy = datetime.now()

    print("\nPRÓXIMOS A VENCER:")

    for m in medicamentos:
        fecha_v = datetime.strptime(m["vencimiento"], "%d/%m/%Y")
        dias = (fecha_v - hoy).days

        if dias <= 30:
            print(m["nombre"], "- vence en", dias, "días")

# Buscar
def buscar():
    dato = input("Buscar por ID o nombre: ")
    encontrado = False

    for m in medicamentos:
        if str(m["id"]) == dato or m["nombre"].lower() == dato.lower():
            print("Encontrado:", m)

            busquedas.append({
                "dato": dato,
                "fecha": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            })

            encontrado = True

    if not encontrado:
        print("No encontrado")

# Reporte de búsquedas
def reporte_busquedas():
    print("\nREPORTE DE BÚSQUEDAS")

    for b in busquedas:
        print(b["dato"], "-", b["fecha"])

# Menú
while True:
    print("""
1. Registrar medicamento
2. Mostrar lista
3. Más vendido
4. Próximos a vencer
5. Buscar
6. Reporte de búsquedas
7. Salir
""")

    op = input("Opción: ")

    if op == "1":
        registrar()
    elif op == "2":
        mostrar()
    elif op == "3":
        mas_vendido()
    elif op == "4":
        proximos_vencer()
    elif op == "5":
        buscar()
    elif op == "6":
        reporte_busquedas()
    elif op == "7":
        break
    else:
        print("Opción inválida")

    
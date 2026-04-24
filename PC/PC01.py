import json 
import os 
from datetime import datetime 
 
ARCHIVO = "abastecimiento.json" 
 
# ========================= 
# UTILIDADES DE ARCHIVO 
# ========================= 
def cargar_datos(): 
    if os.path.exists(ARCHIVO): 
        with open(ARCHIVO, "r", encoding="utf-8") as archivo: 
            return json.load(archivo) 
    return [] 
 
def guardar_datos(productos): 
    with open(ARCHIVO, "w", encoding="utf-8") as archivo: 
        json.dump(productos, archivo, indent=4, ensure_ascii=False) 
 
# ========================= 
# VALIDACIONES 
# ========================= 
def leer_entero(mensaje): 
    while True: 
        try: 
            return int(input(mensaje)) 
        except ValueError: 
            print("Error: ingrese un número entero válido.") 
 
def leer_decimal(mensaje): 
    while True: 
        try: 
            return float(input(mensaje)) 
        except ValueError: 
            print("Error: ingrese un número decimal válido.") 
 
def leer_fecha(mensaje): 
    while True: 
        fecha = input(mensaje).strip() 
        try: 
            datetime.strptime(fecha, "%Y-%m-%d") 
            return fecha 
        except ValueError: 
 
            print("Error: use el formato YYYY-MM-DD. Ejemplo: 2026-0406")
 
# ========================= 
# OPERACIONES CRUD 
# ========================= 
def generar_codigo(productos): 
    if not productos: 
        return 1 
    return max(p["codigo"] for p in productos) + 1 
 
def ingresar_producto(productos): 
    print("\n=== INGRESO DE PRODUCTO ===") 
    nombre = input("Nombre del producto: ").strip() 
    categoria = input("Categoría: ").strip() 
    proveedor = input("Proveedor: ").strip() 
    costo = leer_decimal("Costo unitario: ") 
    precio_venta = leer_decimal("Precio de venta: ") 
    stock = leer_entero("Stock inicial: ") 
    stock_minimo = leer_entero("Stock mínimo permitido: ") 
    fecha_ingreso = leer_fecha("Fecha de ingreso (YYYY-MM-DD): ") 
 
    producto = { 
        "codigo": generar_codigo(productos), 
        "nombre": nombre, 
        "categoria": categoria, 
        "proveedor": proveedor, 
        "costo": costo, 
        "precio_venta": precio_venta, 
        "stock": stock, 
        "stock_minimo": stock_minimo, 
        "fecha_ingreso": fecha_ingreso 
    } 
 
    productos.append(producto) 
    guardar_datos(productos) 
    print("Producto registrado correctamente.") 
 
def mostrar_productos(productos): 
    print("\n=== LISTA DE PRODUCTOS ===") 
    if not productos: 
        print("No hay productos registrados.") 
        return 
 
    encabezado = "{:<6} {:<20} {:<15} {:<18} {:<10} {:<10} {:<8} {:<12} {:<12}" 
 
    print(encabezado.format( 
        "COD", "NOMBRE", "CATEGORÍA", "PROVEEDOR", 
        "COSTO", "P.VENTA", "STOCK", "STK.MIN", "FECHA" 
    )) 
    print("-" * 120) 
 
    for p in productos: 
        print(encabezado.format( 
            p["codigo"], 
            p["nombre"][:20], 
            p["categoria"][:15], 
            p["proveedor"][:18], 
            f'{p["costo"]:.2f}', 
            f'{p["precio_venta"]:.2f}', 
            p["stock"], 
            p["stock_minimo"], 
            p["fecha_ingreso"] 
        )) 
 
def buscar_por_codigo(productos): 
    codigo = leer_entero("Ingrese código del producto: ") 
    for p in productos: 
        if p["codigo"] == codigo: 
            print("\nProducto encontrado:") 
            mostrar_productos([p]) 
            return 
    print("No se encontró el producto.") 
 
def buscar_por_nombre(productos): 
    texto = input("Ingrese nombre o parte del nombre: ").strip().lower() 
    encontrados = [p for p in productos if texto in p["nombre"].lower()] 
 
    if encontrados: 
        mostrar_productos(encontrados) 
    else: 
        print("No se encontraron productos con ese nombre.") 
 
def buscar_por_proveedor(productos): 
    texto = input("Ingrese nombre del proveedor: ").strip().lower() 
    encontrados = [p for p in productos if texto in 
p["proveedor"].lower()] 
 
    if encontrados: 
        mostrar_productos(encontrados) 
    else: 
        print("No se encontraron productos de ese proveedor.") 
 
 
def actualizar_producto(productos): 
    codigo = leer_entero("Ingrese el código del producto a actualizar: ") 
 
    for p in productos: 
        if p["codigo"] == codigo: 
            print("\nDeje vacío si no desea cambiar un campo.") 
 
            nuevo_nombre = input(f'Nombre [{p["nombre"]}]: ').strip() 
            nueva_categoria = input(f'Categoría [{p["categoria"]}]: ').strip() 
            nuevo_proveedor = input(f'Proveedor [{p["proveedor"]}]: ').strip() 
            nuevo_costo = input(f'Costo [{p["costo"]}]: ').strip() 
            nuevo_precio = input(f'Precio venta [{p["precio_venta"]}]: ').strip() 
            nuevo_stock = input(f'Stock [{p["stock"]}]: ').strip() 
            nuevo_stock_min = input(f'Stock mínimo [{p["stock_minimo"]}]: ').strip() 
            nueva_fecha = input(f'Fecha ingreso [{p["fecha_ingreso"]}] (YYYY-MM-DD): ').strip() 
  
            if nuevo_nombre: 
                p["nombre"] = nuevo_nombre 
            if nueva_categoria: 
                p["categoria"] = nueva_categoria 
            if nuevo_proveedor: 
                p["proveedor"] = nuevo_proveedor 
            if nuevo_costo: 
                p["costo"] = float(nuevo_costo) 
            if nuevo_precio: 
                p["precio_venta"] = float(nuevo_precio) 
            if nuevo_stock: 
                p["stock"] = int(nuevo_stock) 
            if nuevo_stock_min: 
                p["stock_minimo"] = int(nuevo_stock_min) 
            if nueva_fecha: 
                datetime.strptime(nueva_fecha, "%Y-%m-%d") 
                p["fecha_ingreso"] = nueva_fecha 
 
            guardar_datos(productos) 
            print("Producto actualizado correctamente.") 
            return 
 
    print("No se encontró el producto.") 
 
def eliminar_producto(productos): 
 
    codigo = leer_entero("Ingrese el código del producto a eliminar: ") 
 
    for p in productos: 
        if p["codigo"] == codigo: 
            productos.remove(p) 
            guardar_datos(productos) 
            print("Producto eliminado correctamente.") 
            return 
 
    print("No se encontró el producto.") 
 
# ========================= 
# ORDENAMIENTOS 
# ========================= 
def ordenar_por_nombre(productos): 
    ordenados = sorted(productos, key=lambda x: x["nombre"].lower()) 
    mostrar_productos(ordenados) 
 
def ordenar_por_costo(productos): 
    ordenados = sorted(productos, key=lambda x: x["costo"]) 
    mostrar_productos(ordenados) 
 
def ordenar_por_stock(productos): 
    ordenados = sorted(productos, key=lambda x: x["stock"], reverse=True) 
    mostrar_productos(ordenados) 
 
def ordenar_por_fecha(productos): 
    ordenados = sorted(productos, key=lambda x: x["fecha_ingreso"]) 
    mostrar_productos(ordenados) 
 
# ========================= 
# REPORTES 
# ========================= 
def productos_bajo_stock(productos): 
    bajos = [p for p in productos if p["stock"] <= p["stock_minimo"]] 
 
    print("\n=== PRODUCTOS CON BAJO STOCK ===") 
    if bajos: 
        mostrar_productos(bajos) 
    else: 
        print("No hay productos con bajo stock.") 
 
def reporte_valorizado(productos): 
    print("\n=== REPORTE VALORIZADO DE INVENTARIO ===") 
 
    if not productos: 
        print("No hay productos registrados.") 
        return 
 
    total_general = 0 
    print("{:<6} {:<20} {:<10} {:<8} {:<12}".format( 
        "COD", "NOMBRE", "COSTO", "STOCK", "TOTAL" 
    )) 
    print("-" * 65) 
 
    for p in productos: 
        total = p["costo"] * p["stock"] 
        total_general += total 
        print("{:<6} {:<20} {:<10.2f} {:<8} {:<12.2f}".format( 
            p["codigo"], p["nombre"][:20], p["costo"], p["stock"], total 
        )) 
 
    print("-" * 65) 
    print(f"VALOR TOTAL DEL INVENTARIO: {total_general:.2f}") 
 
# ========================= 
# MENÚS 
# ========================= 
def menu_busqueda(productos): 
    while True: 
        print("\n=== MENÚ DE BÚSQUEDA ===") 
        print("1. Buscar por código") 
        print("2. Buscar por nombre") 
        print("3. Buscar por proveedor") 
        print("4. Volver") 
 
        opcion = input("Seleccione una opción: ").strip() 
 
        if opcion == "1": 
            buscar_por_codigo(productos) 
        elif opcion == "2": 
            buscar_por_nombre(productos) 
        elif opcion == "3": 
            buscar_por_proveedor(productos) 
        elif opcion == "4": 
            break 
        else: 
            print("Opción inválida.") 
 
def menu_ordenamiento(productos): 
    while True: 
        print("\n=== MENÚ DE ORDENAMIENTO ===") 
 
        print("1. Ordenar por nombre") 
        print("2. Ordenar por costo") 
        print("3. Ordenar por stock") 
        print("4. Ordenar por fecha de ingreso") 
        print("5. Volver") 
 
        opcion = input("Seleccione una opción: ").strip() 
 
        if opcion == "1": 
            ordenar_por_nombre(productos) 
        elif opcion == "2": 
            ordenar_por_costo(productos) 
        elif opcion == "3": 
            ordenar_por_stock(productos) 
        elif opcion == "4": 
            ordenar_por_fecha(productos) 
        elif opcion == "5": 
            break 
        else: 
            print("Opción inválida.") 
 
def menu_reportes(productos): 
    while True: 
        print("\n=== MENÚ DE REPORTES ===") 
        print("1. Mostrar todos los productos") 
        print("2. Productos con bajo stock") 
        print("3. Reporte valorizado de inventario") 
        print("4. Volver") 
 
        opcion = input("Seleccione una opción: ").strip() 
 
        if opcion == "1": 
            mostrar_productos(productos) 
        elif opcion == "2": 
            productos_bajo_stock(productos) 
        elif opcion == "3": 
            reporte_valorizado(productos) 
        elif opcion == "4": 
            break 
        else: 
            print("Opción inválida.") 
 
def menu_principal(): 
    productos = cargar_datos() 
 
    while True: 
        print("\n" + "=" * 50) 
 
        print(" SISTEMA DE ABASTECIMIENTO DE PRODUCTOS ") 
        print("=" * 50) 
        print("1. Ingresar producto") 
        print("2. Buscar producto") 
        print("3. Actualizar producto") 
        print("4. Eliminar producto") 
        print("5. Ordenar productos") 
        print("6. Reportes") 
        print("7. Salir") 
 
        opcion = input("Seleccione una opción: ").strip() 
 
        if opcion == "1": 
            ingresar_producto(productos) 
        elif opcion == "2": 
            menu_busqueda(productos) 
        elif opcion == "3": 
            actualizar_producto(productos) 
        elif opcion == "4": 
            eliminar_producto(productos) 
        elif opcion == "5": 
            menu_ordenamiento(productos) 
        elif opcion == "6": 
            menu_reportes(productos) 
        elif opcion == "7": 
            print("Saliendo del sistema...") 
            break 
        else: 
            print("Opción inválida. Intente nuevamente.") 
 
# ========================= 
# EJECUCIÓN 
# ========================= 
if __name__ == "__main__": 
    menu_principal()
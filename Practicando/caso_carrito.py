def carrito_compras():
    carrito = []
    while True:
        producto = input("Ingrese el nombre del producto (o 'salir' para terminar): ")
        if producto.lower() == 'salir':
            break
        precio = float(input("Ingrese el precio del producto: "))
        carrito.append((producto, precio))
    
    total = sum(precio for _, precio in carrito)
    print("\nCarrito de compras:")
    for producto, precio in carrito:
        print(f"{producto}: ${precio:.2f}")
    print(f"Total a pagar: ${total:.2f}")

if __name__ == "__main__":    carrito_compras()


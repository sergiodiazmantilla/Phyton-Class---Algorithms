def menu_opciones():
    print("Menú de opciones:")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("4. Salir")
def ejecutar_opcion(opcion):
    if opcion == 1:
        print("Has seleccionado la Opción 1")
    elif opcion == 2:
        print("Has seleccionado la Opción 2")
    elif opcion == 3:
        print("Has seleccionado la Opción 3")
    elif opcion == 4:
        print("Saliendo del programa...")
    else:
        print("Opción no válida. Por favor, selecciona una opción del menú.")

def main1():
    while True:
        menu_opciones()
        try:
            opcion = int(input("Selecciona una opción: "))
            if opcion == 4:
                ejecutar_opcion(opcion)
                break
            ejecutar_opcion(opcion)
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número.")

if __name__ == "__main__":
    main1()

#Dibujar figuras con asteriscos con opción de elegir la figura a dibujar
def menu_opciones():
    print("Menú de opciones:")
    print("1. Cuadrado")
    print("2. Triángulo")
    print("3. Rectángulo")
    print("4. Rombo")
    print("5. Círculo")
    print("6. Triángulo invertido")
    print("7. Trapecio")
    print("8. Estrella")
    print("9. Salir")

def dibujar_figura(figura, tamaño):
    if figura == 1:  # Cuadrado
        for i in range(tamaño):
            print("* " * tamaño)
    elif figura == 2:  # Triángulo
        for i in range(1, tamaño + 1):
            print("* " * i)
    elif figura == 3:  # Rectángulo
        for i in range(tamaño // 2):
            print("* " * tamaño)
    elif figura == 4:  # Rombo
        for i in range(tamaño):
            print(" " * (tamaño - i - 1) + "* " * (i + 1))
        for i in range(tamaño - 1):
            print(" " * (i + 1) + "* " * (tamaño - i - 1))
    elif figura == 5:  # Círculo (aproximado)
        for i in range(tamaño):
            for j in range(tamaño):
                if (i - tamaño // 2) ** 2 + (j - tamaño // 2) ** 2 <= (tamaño // 2) ** 2:
                    print("* ", end="")
                else:
                    print("  ", end="")
            print()
    elif figura == 6:  # Triángulo invertido
        for i in range(tamaño, 0, -1):
            print("* " * i)
    elif figura == 7:  # Trapecio
        for i in range(tamaño):
            print(" " * (tamaño - i - 1) + "* " * (tamaño + i))
    elif figura == 8: # Estrella
        for i in range(tamaño):
            print(" " * (tamaño - i - 1) + "* " * (2 * i + 1))
        for i in range(tamaño - 1):
            print(" " * (i + 1) + "* " * (2 * (tamaño - i - 1) - 1))
    elif figura == 9:  # Salir
        print("Saliendo del programa.")
    else:
        print("Figura no válida. Por favor, elija una opción del 1 al 9.")

# Ejemplo de uso
def main():
    while True:
        menu_opciones()
        try:
            opcion = int(input("Selecciona una opción: "))
            if opcion == 9:
                dibujar_figura(opcion, 0)  # Llamar a la función para salir
                break
            tamaño = int(input("Ingrese el tamaño de la figura: "))
            dibujar_figura(opcion, tamaño)
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número.")

if __name__ == "__main__": main()

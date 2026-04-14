def calculadora(num1, num2, operacion):
    if operacion == "1":
        return num1 + num2
    elif operacion == "2":
        return num1 - num2
    elif operacion == "3":
        return num1 * num2
    elif operacion == "4":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: División por cero"
    else:
        return "Operación no válida"

# Ejemplo de uso
if __name__ == "__main__":
    numero1 = float(input("Ingrese el primer número: "))
    numero2 = float(input("Ingrese el segundo número: "))
    operacion = input("Ingrese la operación (" \
    "1. suma, " \
    "2. resta, " \
    "3. multiplicacion, " \
    "4. division): ")
    resultado = calculadora(numero1, numero2, operacion)
    print(f"El resultado es: {resultado}")


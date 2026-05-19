import random

ROJO = {1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36}
NEGRO = {2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35}


def crear_ruleta_americana():
    rueda = ["0", "00"]
    rueda += [str(n) for n in range(1, 37)]
    return rueda


def color_casilla(casilla):
    if casilla in ("0", "00"):
        return "Verde"
    numero = int(casilla)
    return "Rojo" if numero in ROJO else "Negro"


def evaluar_apuesta(tipo, valor, casilla):

    if tipo == "1":
        if casilla == valor:
            return 35
        return 0

    if tipo == "2":
        if color_casilla(casilla) == valor:
            return 1
        return 0

    if tipo == "3":
        if casilla not in ("0", "00") and (int(casilla) % 2 == 0) == (valor == "Par"):
            return 1
        return 0

    if tipo == "4":
        valor = int(valor)
        numero = int(casilla)

        if casilla not in ("0", "00") and 1 + 12 * (valor - 1) <= numero <= 12 * valor:
            return 2

        return 0
    return 0


def pedir_apuesta():
    print("\n--- Simulación Ruleta Las Vegas ---")
    print("Tipos de apuesta disponibles:")
    print("  1) Número exacto (paga 35:1)")
    print("  2) Color Rojo/Negro (paga 1:1)")
    print("  3) Par/Impar (paga 1:1)")
    print("  4) Docena (1-12, 13-24, 25-36) (paga 2:1)")

    tipo = input("Selecciona el tipo de apuesta (1-4): ").strip()
    while tipo not in {"1", "2", "3", "4"}:
        tipo = input("Opción inválida. Elige 1, 2, 3 o 4: ").strip()

    if tipo == "1":
        valor = input("Elige un número entre 0, 00 o 1-36: ").strip()
        while valor not in {"0", "00"} and not (valor.isdigit() and 1 <= int(valor) <= 36):
            valor = input("Número inválido. Escribe 0, 00 o 1-36: ").strip()
    elif tipo == "2":
        valor = input("Elige color Rojo o Negro: ").strip().capitalize()
        while valor not in {"Rojo", "Negro"}:
            valor = input("Color inválido. Elige Rojo o Negro: ").strip().capitalize()
    elif tipo == "3":
        valor = input("Elige Par o Impar: ").strip().capitalize()
        while valor not in {"Par", "Impar"}:
            valor = input("Opción inválida. Elige Par o Impar: ").strip().capitalize()
    else:
        valor = input("Elige docena 1, 2 o 3: ").strip()
        while valor not in {"1", "2", "3"}:
            valor = input("Docena inválida. Elige 1, 2 o 3: ").strip()

    apuesta = input("Cuánto quieres apostar? (cantidad numérica): ").strip()
    while not apuesta.isdigit() or int(apuesta) <= 0:
        apuesta = input("Cantidad inválida. Escribe un número mayor a 0: ").strip()

    return tipo, valor, int(apuesta)


def simular_ruleta():
    rueda = crear_ruleta_americana()
    tipo, valor, apuesta = pedir_apuesta()

    intentos = input("¿Cuántas tiradas quieres simular? (por ejemplo 10): ").strip()
    while not intentos.isdigit() or int(intentos) <= 0:
        intentos = input("Cantidad inválida. Escribe un número mayor a 0: ").strip()
    intentos = int(intentos)

    saldo = 0
    resultados = []

    for i in range(1, intentos + 1):
        casilla = random.choice(rueda)
        multiplicador = evaluar_apuesta(tipo, valor, casilla)
        if multiplicador > 0:
            ganancia = apuesta * multiplicador
            saldo += ganancia
        else:
            ganancia = 0
            saldo -= apuesta
        resultados.append((i, casilla, color_casilla(casilla), ganancia, saldo))

    print("\n--- Resultados de la simulación ---")
    for i, casilla, color, ganancia, saldo_actual in resultados:
        print(f"Tirada {i:>2}: cayó {casilla} ({color}) -> Ganancia: {ganancia} $  |  Saldo acumulado: {saldo_actual} $")

    print("\nResumen final:")
    print(f"  Tiradas: {intentos}")
    print(f"  Saldo neto: {saldo} $")
    print(f"  Retorno promedio por tirada: {saldo / intentos:.2f} $")
    if saldo > 0:
        print("  Resultado: Ganaste en la simulación")
    elif saldo < 0:
        print("  Resultado: Perdiste en la simulación")
    else:
        print("  Resultado: Empate exacto")


def ruleta_vegas():
    simular_ruleta()


if __name__ == "__main__":
    ruleta_vegas()

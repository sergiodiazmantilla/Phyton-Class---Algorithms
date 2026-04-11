## Ejercicio 1

def potencia_rapida(base, exponente):
    if exponente == 0:
        return 1
    
    mitad = potencia_rapida(base, exponente // 2)
    if exponente % 2 == 0:
        return mitad * mitad
    else:
        return mitad * mitad * base

base = 2
exponente = 10
resultado = potencia_rapida(base, exponente)
print(f"{base} elevado a la {exponente} es: {resultado}")

##Ejercicio 2

def potencia(base, exponente):
    resultado = 1
    while exponente > 0:
        if exponente % 2 == 1:  # Si el exponente es impar
            resultado *= base
        base *= base
        exponente //= 2
    return resultado
base = 2
exponente = 10
resultado = potencia(base, exponente)
print(f"{base} elevado a la {exponente} es: {resultado}")

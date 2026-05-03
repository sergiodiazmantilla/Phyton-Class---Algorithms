import random
import math

def estimar_pi(intentos):
    puntos_dentro=0

    for _ in range(intentos):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        
        distancia = x**2 + y**2

        if distancia <= 1:
            puntos_dentro += 1
    
    pi_estimado = 4 * puntos_dentro / intentos
    return pi_estimado

intentos = 100000
resultado = estimar_pi(intentos)
print("Caso 1: Estimacion de PI MONTE CARLO")
print("=" * 50)
print("Intentos realizados: ", intentos)
print("Valores estimados de PI: ", resultado)
print("Valor real aproximado: ", math.pi)
print("Error: ", abs(math.pi - resultado))

import random

def simulate_roulette():
    # Simulamos la ruleta (colores)
    outcomes = ["red", "black", "green"]
    return random.choice(outcomes)

# Simulamos 10 giros de ruleta
for _ in range(10):
    print("Resultado: ", simulate_roulette())

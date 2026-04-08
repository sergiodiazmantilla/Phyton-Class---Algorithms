def potencia(base, exp):
    if exp == 0:
        return 1
    return base * potencia(base, exp -1)
print(potencia(2, 7))
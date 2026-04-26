def potencia_rapida(base, exponente): 
    if exponente == 0: 
        return 1 
 
    mitad = potencia_rapida(base, exponente // 2) 
 
    if exponente % 2 == 0: 
        return mitad * mitad 
    else: 
        return base * mitad * mitad 
 
base = 2 
exponente = 10 
 
print("Resultado:", potencia_rapida(base, exponente))
def cambio_moneda(monto,monedas):
    monedas.sort(reverse=True)
    resultado =[]

    for moneda in monedas:
        while monto >= moneda:
            monto -= moneda
            resultado.append(moneda)
    return resultado

monedas = [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1] #Monedas Perú
monto = 67
print ("Cambio", cambio_moneda(monto, monedas))

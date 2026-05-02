def Amazon_promociones_dp(productos, presupuesto):
    n = len(productos)
    dp=[[0] * (presupuesto + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        costo = productos[i-1] ["costo"]
        ganancia = productos[i - 1] ["ganancia"]

        for p in range(presupuesto + 1):
            if costo <= p:
                dp[i][p] = max(
                    dp[i - 1][p],
                    dp[i - 1][p - costo]+ganancia
                )
            else:
                dp[i][p] = dp[i-1][p]
    
    seleccion = []
    p = presupuesto
    for i in range(n, 0, -1):
        if dp[i][p] != dp[i-p][p]:
            seleccion.append(productos[i-1]["nombre"])
            p -= productos[i-1]["costo"]
    seleccion.reverse()
    return dp[n][presupuesto], seleccion, dp


productos = [
    {"nombre":"TV", "costo":2, "ganancia":3},
    {"nombre":"Teclado", "costo":3, "ganancia":4},
    {"nombre":"Mouse", "costo":4, "ganancia":5},
    {"nombre":"Tableta", "costo":5, "ganancia":6},
    {"nombre":"Audifonos", "costo":6, "ganancia":7},
]

ganancia_max, seleccion, tabla = Amazon_promociones_dp(productos, 5)
print(" === AMAZON === ")
print("Ganancia Máxima: ", ganancia_max)
print("Poducto Seleccionado:", seleccion)

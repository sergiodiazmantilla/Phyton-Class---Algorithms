def mochila_dp(costo, ganancias, presupuesto):
    n = len(costo)
    dp = [[0 for _ in range(presupuesto + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for p in range(presupuesto + 1):
            if costo[i - 1] <= p:
                dp[i][p] = max(
                    dp[i - 1][p], 
                    dp[i - 1][p - costo[i - 1]] + ganancias[i - 1]
                )
            else:
                dp[i][p] = dp[i - 1][p]
    
    return dp
    
# Ejemplo de uso
costo = [2, 3, 4, 5]
ganancias = [3, 4, 5, 6]
presupuesto = 5

tabla = mochila_dp(costo, ganancias, presupuesto)

for fila in tabla:
    print(fila)

print("Ganancia máxima con presupuesto de 50:", tabla[len(costo)][presupuesto])

#Aplicaciones
#1. Selección de proyectos: Dado un conjunto de proyectos con costos y beneficios, determinar cuáles proyectos seleccionar para maximizar el beneficio sin exceder un presupuesto.
#2. Planificación de eventos: Dado un conjunto de actividades con costos y beneficios,
#3. Gestión de recursos: Dado un conjunto de recursos con costos y beneficios, determinar cómo asignar los recursos para maximizar el beneficio sin exceder un presupuesto.
#4. Optimización de inversiones: Dado un conjunto de oportunidades de inversión con costos y beneficios, determinar cuáles inversiones seleccionar para maximizar el retorno sin exceder un presupuesto.
#5. Selección de productos: Dado un conjunto de productos con costos y beneficios, determinar cuáles productos seleccionar para maximizar el beneficio sin exceder un presupuesto.

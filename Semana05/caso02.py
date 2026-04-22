# Este código implementa una función para calcular el costo mínimo total de completar una serie de etapas, donde cada etapa tiene varios costos asociados. La función utiliza programación dinámica para almacenar los costos mínimos en una matriz y luego encuentra el costo mínimo total al final.
def costo_minimo_etapas(costos):
    # La función toma una lista de listas, donde cada sublista representa los costos de una etapa. El objetivo es encontrar el costo mínimo total para completar todas las etapas.
    n = len(costos)
    dp = [0] * n
    dp[0] = costos[0] # Inicializa el costo para la primera etapa como el mínimo de los costos disponibles en esa etapa.

    # Calcula el costo mínimo para cada etapa utilizando los costos de la etapa anterior
    for i in range(1, n):
        dp[i] = costos[i] + dp[i-1]
        
    return dp

# Ejemplo de uso
costos = [10, 15, 8, 12, 6] # Cada número representa el costo de completar una etapa. El objetivo es encontrar el costo mínimo total para completar todas las etapas.
resultado = costo_minimo_etapas(costos)
print("Costo acumulado:", resultado)
print("Costo total mínimo:", resultado[-1])

#Aplicaciones
# Este tipo de problema es común en situaciones donde se deben tomar decisiones secuenciales, como en la planificación de proyectos, la gestión de recursos o la optimización de rutas. La función puede ser adaptada para resolver problemas similares en diferentes contextos, como la asignación de tareas, la programación de actividades o la minimización de costos en procesos industriales.
# En resumen, el código implementa una solución eficiente para encontrar el costo mínimo total de completar una serie de etapas, utilizando programación dinámica para almacenar y calcular los costos mínimos de manera iterativa.
# El resultado final se imprime al ejecutar el código, mostrando el costo acumulado mínimo para completar todas las etapas dadas en la matriz de costos.

from datetime import datetime

def costo_bloque(entregas, inicio, fin, costo_fijo, costo_km, ventana_horaria, penalizacion_retraso):
    distancia_total = 0
    tiempo_total = 0    

    for k in range(inicio, fin + 1):
        distancia_total += entregas[k]["distancia"]
        tiempo_total += entregas[k]["tiempo"]

    costo = costo_fijo + (distancia_total * costo_km)

    # Penalización si supera la ventana horaria
    if tiempo_total > ventana_horaria:
        costo += penalizacion_retraso
    
    return costo, distancia_total, tiempo_total

# Programación Dinámica
def fedex_dp(entregas, costo_fijo, costo_km, ventana_horaria, penalizacion_retraso):
    n  = len(entregas)

    # Crea un arreglo dp de tamaño n+1.Todos los valores empiezan en infinito (inf).
    dp = [float("inf")] * (n+1)
    
    # Arreglo para guardar decisiones. corte[i] indicará dónde empieza el último bloque de entregas.
    corte = [-1] * (n+1)

    # Si no hay entregas → costo = 0.
    dp[0] = 0

    for i in range(1, n+1):
        for j in range(1, i+1):
            
            # Cálculo del costo del bloque
            # Ignoramos los otros dos con _ ya que costo_bloque() nos devuelve 3 resultados y solo queremos costo, el primero.
            costo, _, _ = costo_bloque( 
                entregas,
                j-1,
                i-1,
                costo_fijo,
                costo_km,
                ventana_horaria,
                penalizacion_retraso
            )
            nuevo_costo = dp[j-1] + costo

            if nuevo_costo < dp[i]:
                dp[i] = nuevo_costo
                corte[i] = j - 1
    return dp, corte

# Reconstrucción de Solución
def reconstruccion_bloque(corte, n):
    bloques = []

    while n > 0:
        inicio = corte[n]
        bloques.append((inicio, n-1))
        n = inicio
    
    bloques.reverse()
    return bloques

# Mostrar datos de entrega
def mostrar_entregas(entregas):
    print("\n" + "=" * 90)
    print("       DATOS DE ENTREGA FEDEX")
    print("=" * 90)
    print("{:<10}{:<20}{:<20}".format("ENTREGA", "DISTANCIA {KM}", "TIEMPO {MIN}"))
    print("-" * 90)

    for i, e in enumerate(entregas, start=1):
        print("{:<10}{:<20}{:<20}".format(i, e["distancia"], e["tiempo"]))
    
    print("=" * 90)

# Mostrar Tabla DP
def mostrar_tabla_dp(dp):
    print("\n" + "-" * 800)
    print("       TABLA DP COSTO ACUMULADO MINIMO")
    print("=" * 80)
    print("{:<15}{:<20}".format("ENTREGAS", "COSTO MINIMO"))
    print("-" * 80)

    for i in range(len(dp)):
        if dp[i] == float("inf"):
            valor = "INF"
        else:
            valor = dp[i]
        print("{:<15}{:<20}".format(i, valor))
    print("-" * 80)

# Reporte Final
def mostrar_reporte_final(entregas, bloques, costo_fijo, costo_km, ventana_horaria, penalizacion_retraso, dp):
    print("\n" + "=" * 120)
    print("       REPORTE FINAL DE DESPACHO")
    print("=" * 120)
    print("{:<20}{:<20}{:<20}{:<20}{:<20}".format(
        "BLOQUE", 
        "DISTANCIA TOTAL",
        "TIEMPO TOTAL",
        "PENALIZACION",
        "COSTO TOTAL"
        ))
    print("-" * 120)

    for idx, (inicio, fin) in enumerate(bloques, start=1):
        costo, distancia_total, tiempo_total = costo_bloque(
            entregas,
            inicio,
            fin,
            costo_fijo,
            costo_km,
            ventana_horaria,
            penalizacion_retraso
        )
        penal = penalizacion_retraso if tiempo_total > ventana_horaria else 0

        print("{:<20}{:<20}{:<20}{:<20}{:<20}".format(
            f"{inicio+1} - {fin+1}",
            distancia_total,
            tiempo_total,
            penal,
            costo
        ))
    print("-" * 120)
    print(" Costo minimo del dia ", dp[len(entregas)])
    print("-" * 120)

entregas = [
    {"distancia": 10, "tiempo": 15},
    {"distancia": 15, "tiempo": 35},
    {"distancia": 8,  "tiempo": 20},
    {"distancia": 20, "tiempo": 40},
    {"distancia": 12, "tiempo": 25}
]

costo_fijo = 50
costo_km = 3
ventana_horaria = 60
penalizacion_retraso = 40

mostrar_entregas(entregas)

dp, corte = fedex_dp(
    entregas,
    costo_fijo,
    costo_km,
    ventana_horaria,
    penalizacion_retraso
)

mostrar_tabla_dp(dp)
bloques = reconstruccion_bloque(corte, len(entregas))
mostrar_reporte_final(
    entregas,
    bloques,
    costo_fijo,
    costo_km,
    ventana_horaria,
    penalizacion_retraso,
    dp
)

fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print("\nFecha de reporte: ", fecha)


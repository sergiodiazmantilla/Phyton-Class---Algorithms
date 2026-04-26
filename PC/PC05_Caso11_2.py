from datetime import datetime 
# ===================================================== 
# DATOS DE PRODUCCIÓN 
# ===================================================== 
turnos = [ 
    {"turno": "Mañana", "capacidad_maxima": 4, "costo_energetico": 12, "modelo": "Model 3"}, 
    {"turno": "Tarde", "capacidad_maxima": 5, "costo_energetico": 10, "modelo": "Model Y"}, 
    {"turno": "Noche", "capacidad_maxima": 6, "costo_energetico": 14, "modelo": "Model 3"} 
] 
demanda_objetivo = 8 
penalizacion_cambio_config = 15 
# ===================================================== 
# DATOS DE VENTAS 
# ===================================================== 
ventas = [ 
 
    {"año": 2024, "mes": "Enero", "modelo": "Model 3", "ventas": 120}, 
    {"año": 2024, "mes": "Enero", "modelo": "Model Y", "ventas": 150}, 
    {"año": 2024, "mes": "Febrero", "modelo": "Model 3", "ventas": 130}, 
    {"año": 2024, "mes": "Febrero", "modelo": "Model Y", "ventas": 140}, 
    {"año": 2024, "mes": "Marzo", "modelo": "Model 3", "ventas": 160}, 
    {"año": 2024, "mes": "Marzo", "modelo": "Model Y", "ventas": 155}, 
    {"año": 2025, "mes": "Enero", "modelo": "Model 3", "ventas": 180}, 
    {"año": 2025, "mes": "Enero", "modelo": "Model Y", "ventas": 170}, 
    {"año": 2025, "mes": "Febrero", "modelo": "Model 3", "ventas": 175}, 
    {"año": 2025, "mes": "Febrero", "modelo": "Model Y", "ventas": 190} 
] 
 
# ===================================================== 
# PROGRAMACIÓN DINÁMICA 
# ===================================================== 
def tesla_produccion_dp(turnos, demanda_objetivo, penalizacion_cambio_config): 
    n = len(turnos) 
    INF = float("inf") 
 
    dp = [[INF] * (demanda_objetivo + 1) for _ in range(n + 1)] 
    decision = [[0] * (demanda_objetivo + 1) for _ in range(n + 1)] 
 
    dp[0][0] = 0 
 
    for i in range(1, n + 1): 
        capacidad = turnos[i - 1]["capacidad_maxima"] 
        costo_energetico = turnos[i - 1]["costo_energetico"] 
        modelo_actual = turnos[i - 1]["modelo"] 
 
        for u in range(demanda_objetivo + 1): 
            for x in range(min(capacidad, u) + 1): 
                penalizacion = 0 
 
                if i > 1 and x > 0: 
                    modelo_anterior = turnos[i - 2]["modelo"] 
                    if modelo_actual != modelo_anterior: 
                        penalizacion = penalizacion_cambio_config 
 
                costo_actual = dp[i - 1][u - x] + (x * costo_energetico) + penalizacion 
 
                if costo_actual < dp[i][u]: 
                    dp[i][u] = costo_actual 
                    decision[i][u] = x 
 
    return dp, decision 
 
 
# ===================================================== 
# RECONSTRUCCIÓN DE SOLUCIÓN 
# ===================================================== 
def reconstruir_produccion(turnos, decision, demanda_objetivo): 
    produccion = [] 
    i = len(turnos) 
    u = demanda_objetivo 
 
    while i > 0: 
        x = decision[i][u] 
        produccion.append(x) 
        u -= x 
        i -= 1 
 
    produccion.reverse() 
    return produccion 
 
# ===================================================== 
# REPORTES DE PRODUCCIÓN 
# ===================================================== 
def mostrar_tabla_turnos(turnos): 
    print("\n" + "=" * 120) 
    print("                    DATOS DE PRODUCCIÓN - TESLA") 
    print("=" * 120) 
    print("{:<12} {:<20} {:<20} {:<20}".format( 
        "TURNO", "CAPACIDAD MÁXIMA", "COSTO ENERGÉTICO", "MODELO" 
    )) 
    print("-" * 120) 
 
    for t in turnos: 
        print("{:<12} {:<20} {:<20} {:<20}".format( 
            t["turno"], 
            t["capacidad_maxima"], 
            t["costo_energetico"], 
            t["modelo"] 
        )) 
 
    print("=" * 120) 
 
def mostrar_tabla_dp(dp): 
    print("\n" + "=" * 90) 
    print("                TABLA DP - COSTO MÍNIMO ACUMULADO") 
    print("=" * 90) 
    print("{:<10} {:<20}".format("UNIDADES", "COSTO MÍNIMO")) 
    print("-" * 90) 
 
    ultima_fila = dp[-1] 
 
    for i, valor in enumerate(ultima_fila): 
        texto = "INF" if valor == float("inf") else valor 
        print("{:<10} {:<20}".format(i, texto)) 
 
    print("=" * 90) 
 
def mostrar_reporte_final(turnos, produccion, dp, demanda_objetivo, penalizacion_cambio_config): 
    print("\n" + "=" * 140) 
    print("                     REPORTE FINAL DE PRODUCCIÓN ÓPTIMA") 
    print("=" * 140) 
    print("{:<12} {:<18} {:<18} {:<20} {:<25} {:<18}".format( 
        "TURNO", "MODELO", "UNIDADES", "COSTO ENERGÉTICO", "PENALIZACIÓN CONFIG.", "COSTO TOTAL" 
    )) 
    print("-" * 140) 
 
    total = 0 
 
    for i in range(len(turnos)): 
        turno = turnos[i] 
        unidades = produccion[i] 
        costo_energia = unidades * turno["costo_energetico"] 
 
        penalizacion = 0 
        if i > 0 and unidades > 0: 
            if turnos[i]["modelo"] != turnos[i - 1]["modelo"]: 
                penalizacion = penalizacion_cambio_config 
 
        costo_total = costo_energia + penalizacion 
        total += costo_total 
 
        print("{:<12} {:<18} {:<18} {:<20} {:<25} {:<18}".format( 
            turno["turno"], 
            turno["modelo"], 
            unidades, 
            costo_energia, 
            penalizacion, 
            costo_total 
        )) 
 
    print("-" * 140) 
    print("Demanda objetivo:", demanda_objetivo) 
    print("Costo mínimo total:", dp[len(turnos)][demanda_objetivo]) 
    print("=" * 140) 
 
# ===================================================== 
 
# ANÁLISIS DE VEHÍCULO MÁS VENDIDO 
# ===================================================== 
def vehiculo_mas_vendido_por_anio(ventas): 
    resumen = {} 
 
    for v in ventas: 
        año = v["año"] 
        modelo = v["modelo"] 
        cantidad = v["ventas"] 
 
        if año not in resumen: 
            resumen[año] = {} 
 
        if modelo not in resumen[año]: 
            resumen[año][modelo] = 0 
 
        resumen[año][modelo] += cantidad 
 
    print("\n" + "=" * 90) 
    print("              VEHÍCULO MÁS VENDIDO POR AÑO") 
    print("=" * 90) 
    print("{:<12} {:<20} {:<20}".format("AÑO", "MODELO", "VENTAS")) 
    print("-" * 90) 
 
    for año, modelos in resumen.items(): 
        modelo_top = max(modelos, key=modelos.get) 
        print("{:<12} {:<20} {:<20}".format(año, modelo_top, modelos[modelo_top])) 
 
    print("=" * 90) 
 
def vehiculo_mas_vendido_por_mes(ventas): 
    resumen = {} 
 
    for v in ventas: 
        clave = (v["año"], v["mes"]) 
        modelo = v["modelo"] 
        cantidad = v["ventas"] 
 
        if clave not in resumen: 
            resumen[clave] = {} 
 
        if modelo not in resumen[clave]: 
            resumen[clave][modelo] = 0 
 
        resumen[clave][modelo] += cantidad 
 
    print("\n" + "=" * 100) 
 
    print("               VEHÍCULO MÁS VENDIDO POR MES") 
    print("=" * 100) 
    print("{:<12} {:<15} {:<20} {:<20}".format("AÑO", "MES", "MODELO", "VENTAS")) 
    print("-" * 100) 
 
    for (año, mes), modelos in resumen.items(): 
        modelo_top = max(modelos, key=modelos.get) 
        print("{:<12} {:<15} {:<20} {:<20}".format(año, mes, modelo_top, modelos[modelo_top])) 
 
    print("=" * 100) 
 
# ===================================================== 
# EJECUCIÓN 
# ===================================================== 
mostrar_tabla_turnos(turnos) 
 
dp, decision = tesla_produccion_dp(turnos, demanda_objetivo, penalizacion_cambio_config) 
 
mostrar_tabla_dp(dp) 
 
produccion = reconstruir_produccion(turnos, decision, demanda_objetivo) 
 
mostrar_reporte_final(turnos, produccion, dp, demanda_objetivo, penalizacion_cambio_config) 
 
vehiculo_mas_vendido_por_anio(ventas) 
vehiculo_mas_vendido_por_mes(ventas) 
 
fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
print("\nFecha del reporte:", fecha)
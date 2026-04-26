import matplotlib.pyplot as plt 
 
# ===================================================== 
# DATOS DEL CASO MICROSOFT AZURE 
# ===================================================== 
# Cada lista representa el beneficio obtenido al asignar 
# 0, 1, 2, 3, ..., unidades de presupuesto a cada área. 
beneficios = { 
    "Cómputo":        [0, 4, 7, 9, 10, 11, 12], 
    "Almacenamiento": [0, 2, 5, 7, 8, 9, 10], 
    "Bases de datos": [0, 3, 6, 8, 11, 12, 13], 
    "Observabilidad": [0, 1, 4, 6, 9, 10, 11] 
} 
 
presupuesto_total = 6 
 
# ===================================================== 
# PROGRAMACIÓN DINÁMICA 
# ===================================================== 
def azure_presupuesto_dp(beneficios, presupuesto_total): 
    areas = list(beneficios.keys()) 
    n = len(areas) 
 
    # dp[i][p] = beneficio máximo usando primeras i áreas y presupuesto p 
    dp = [[0] * (presupuesto_total + 1) for _ in range(n + 1)] 
    decision = [[0] * (presupuesto_total + 1) for _ in range(n + 1)] 
 
    for i in range(1, n + 1): 
        area = areas[i - 1] 
        curva = beneficios[area] 
 
        for p in range(presupuesto_total + 1): 
            mejor_valor = -1 
            mejor_x = 0 
 
            for x in range(p + 1):  # presupuesto asignado a la área actual 
                valor_actual = dp[i - 1][p - x] + curva[x] 
 
                if valor_actual > mejor_valor: 
                    mejor_valor = valor_actual 
                    mejor_x = x 
 
            dp[i][p] = mejor_valor 
            decision[i][p] = mejor_x 
 
    return areas, dp, decision 
 
# ===================================================== 
# RECONSTRUCCIÓN DE LA SOLUCIÓN ÓPTIMA 
# ===================================================== 
def reconstruir_asignacion(areas, decision, presupuesto_total): 
    asignacion = {} 
    i = len(areas) 
    p = presupuesto_total 
 
    while i > 0: 
        x = decision[i][p] 
        asignacion[areas[i - 1]] = x 
        p -= x 
        i -= 1 
 
    return dict(reversed(asignacion.items())) 
 
# ===================================================== 
# MOSTRAR DATOS DEL CASO 
# ===================================================== 
def mostrar_curvas_beneficio(beneficios): 
    print("\n" + "=" * 110) 
    print("                CURVAS DE BENEFICIO POR ÁREA - MICROSOFT AZURE") 
    print("=" * 110) 
 
    print("{:<18}".format("Presupuesto"), end="") 
    for p in range(len(next(iter(beneficios.values())))): 
        print("{:<10}".format(p), end="") 
    print() 
 
    print("-" * 110) 
 
    for area, curva in beneficios.items(): 
 
        print("{:<18}".format(area), end="") 
        for valor in curva: 
            print("{:<10}".format(valor), end="") 
        print() 
 
    print("=" * 110) 
 
# ===================================================== 
# MOSTRAR TABLA DP 
# ===================================================== 
def mostrar_tabla_dp(areas, dp, presupuesto_total): 
    print("\n" + "=" * 110) 
    print("                     TABLA DP - BENEFICIO MÁXIMO ACUMULADO") 
    print("=" * 110) 
 
    print("{:<18}".format("Área/Presupuesto"), end="") 
    for p in range(presupuesto_total + 1): 
        print("{:<10}".format(p), end="") 
    print() 
 
    print("-" * 110) 
 
    for i in range(len(dp)): 
        if i == 0: 
            etiqueta = "0" 
        else: 
            etiqueta = areas[i - 1] 
 
        print("{:<18}".format(etiqueta), end="") 
        for valor in dp[i]: 
            print("{:<10}".format(valor), end="") 
        print() 
 
    print("=" * 110) 
 
# ===================================================== 
# REPORTE FINAL 
# ===================================================== 
def mostrar_reporte_final(asignacion, beneficios): 
    print("\n" + "=" * 120) 
    print("                      REPORTE FINAL DE ASIGNACIÓN ÓPTIMA") 
    print("=" * 120) 
    print("{:<20} {:<20} {:<20}".format("ÁREA", "PRESUPUESTO ASIGNADO", 
"BENEFICIO OBTENIDO")) 
    print("-" * 120) 
 
    total_beneficio = 0 
 
 
    for area, monto in asignacion.items(): 
        beneficio = beneficios[area][monto] 
        total_beneficio += beneficio 
 
        print("{:<20} {:<20} {:<20}".format(area, monto, beneficio)) 
 
    print("-" * 120) 
    print("Beneficio total máximo:", total_beneficio) 
    print("=" * 120) 
 
# ===================================================== 
# GRÁFICOS 
# ===================================================== 
def graficar_asignacion(asignacion): 
    areas = list(asignacion.keys()) 
    montos = list(asignacion.values()) 
 
    plt.figure(figsize=(10, 5)) 
    plt.bar(areas, montos) 
    plt.title("Presupuesto asignado por área en Azure") 
    plt.xlabel("Áreas") 
    plt.ylabel("Presupuesto") 
    plt.grid(axis="y") 
    plt.show() 
 
def graficar_beneficios(asignacion, beneficios): 
    areas = list(asignacion.keys()) 
    valores = [beneficios[area][monto] for area, monto in 
asignacion.items()] 
 
    plt.figure(figsize=(10, 5)) 
    plt.bar(areas, valores) 
    plt.title("Beneficio obtenido por área") 
    plt.xlabel("Áreas") 
    plt.ylabel("Beneficio") 
    plt.grid(axis="y") 
    plt.show() 
 
def graficar_curvas(beneficios): 
    plt.figure(figsize=(10, 6)) 
 
    for area, curva in beneficios.items(): 
        presupuestos = list(range(len(curva))) 
        plt.plot(presupuestos, curva, marker="o", label=area) 
 
 
    plt.title("Curvas de beneficio por área") 
    plt.xlabel("Presupuesto asignado") 
    plt.ylabel("Beneficio") 
    plt.legend() 
    plt.grid(True) 
    plt.show() 
 
# ===================================================== 
# EJECUCIÓN 
# ===================================================== 
mostrar_curvas_beneficio(beneficios) 
 
areas, dp, decision = azure_presupuesto_dp(beneficios, presupuesto_total) 
 
mostrar_tabla_dp(areas, dp, presupuesto_total) 
 
asignacion = reconstruir_asignacion(areas, decision, presupuesto_total) 
 
mostrar_reporte_final(asignacion, beneficios) 
 
# Gráficos 
graficar_asignacion(asignacion) 
graficar_beneficios(asignacion, beneficios) 
graficar_curvas(beneficios) 
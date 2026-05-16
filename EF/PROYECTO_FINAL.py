import time 
import os
import matplotlib.pyplot as plt

def knapsack_dynamic_programming(weights, values, capacity):
    """
    Resuelve el problema de la mochila usando Programación Dinámica.
    Complejidad: O(n * W)
    """
    n = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    start_time = time.time()
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w-weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    
    end_time = time.time()
    
    # Reconstrucción de los elementos seleccionados
    res = dp[n][capacity]
    w = capacity
    items_selected = []
    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res != dp[i-1][w]:
            items_selected.append(i-1)
            res -= values[i-1]
            w -= weights[i-1]
            
    return dp[n][capacity], items_selected, end_time - start_time

def knapsack_greedy(weights, values, capacity):
    """
    Resuelve el problema de la mochila usando un enfoque Voraz (Greedy) basado en valor/peso.
    Nota: No siempre garantiza la solución óptima para la mochila 0/1.
    """
    n = len(weights)
    items = []
    for i in range(n):
        items.append({
            'id': i,
            'weight': weights[i],
            'value': values[i],
            'ratio': values[i] / weights[i]
        })
    
    # Ordenar por ratio valor/peso de forma descendente
    items.sort(key=lambda x: x['ratio'], reverse=True)
    
    total_value = 0
    current_weight = 0
    items_selected = []
    
    start_time = time.time()
    for item in items:
        if current_weight + item['weight'] <= capacity:
            current_weight += item['weight']
            total_value += item['value']
            items_selected.append(item['id'])
    end_time = time.time()
    
    return total_value, items_selected, end_time - start_time

def run_experiment():
    # Datos de ejemplo: Pesos y valores de productos en un almacén
    weights = [10, 20, 30, 15, 25, 50, 10, 5, 35, 40]
    values = [60, 100, 120, 75, 90, 200, 50, 30, 150, 180]
    capacity = 100
    
    print("--- Problema de Optimización de Carga (Mochila 0/1) ---")
    print(f"Capacidad de la mochila: {capacity}")
    print(f"Número de elementos: {len(weights)}")
    print("-" * 50)
    
    # Ejecución Programación Dinámica
    val_dp, items_dp, time_dp = knapsack_dynamic_programming(weights, values, capacity)
    print(f"Programación Dinámica:")
    print(f"  Valor Total: {val_dp}")
    print(f"  Elementos: {items_dp}")
    print(f"  Tiempo: {time_dp:.6f} segundos")
    
    # Ejecución Algoritmo Voraz
    val_greedy, items_greedy, time_greedy = knapsack_greedy(weights, values, capacity)
    print(f"\nAlgoritmo Voraz (Ratio Valor/Peso):")
    print(f"  Valor Total: {val_greedy}")
    print(f"  Elementos: {items_greedy}")
    print(f"  Tiempo: {time_greedy:.6f} segundos")
    
    # Comparación de eficiencia
    print("\nAnálisis de Resultados:")
    if val_dp > val_greedy:
        print(f"  La Programación Dinámica encontró una mejor solución (+{val_dp - val_greedy}).")
    else:
        print("  Ambos algoritmos encontraron la misma solución óptima.")
        
    # Generar gráfico comparativo de tiempos (simulado con más datos para visualización)
    sizes = [10, 50, 100, 200, 500]
    times_dp = []
    times_greedy = []
    
    for s in sizes:
        w_test = [i % 50 + 1 for i in range(s)]
        v_test = [i % 100 + 1 for i in range(s)]
        cap_test = s * 5
        
        _, _, t_dp = knapsack_dynamic_programming(w_test, v_test, cap_test)
        _, _, t_greedy = knapsack_greedy(w_test, v_test, cap_test)
        
        times_dp.append(t_dp)
        times_greedy.append(t_greedy)
    
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times_dp, label='Programación Dinámica', marker='o')
    plt.plot(sizes, times_greedy, label='Algoritmo Voraz', marker='s')
    plt.xlabel('Número de elementos (n)')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.title('Comparación de Complejidad Temporal: DP vs Voraz')
    plt.legend()
    plt.grid(True)
    plt.savefig('comparacion_tiempos.png')
    print("\nGráfico 'comparacion_tiempos.png' generado.")
    os.startfile("comparacion_tiempos.png" )

if __name__ == "__main__":
    run_experiment()

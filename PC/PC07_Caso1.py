import heapq 
from collections import defaultdict 
from concurrent.futures import ThreadPoolExecutor 
import operator 
from dataclasses import dataclass, field 
from typing import Optional 

# ============================================================ 
# 1. ÁRBOL BINARIO COMPLETO 
# ============================================================ 

class CompleteBinaryTree: 
    """ 
    Un árbol binario completo se llena por niveles, 
    de izquierda a derecha. 
    """ 
 
    def __init__(self): 
        self.nodes = [] 
 
    #def insert(self, value): 
    #    self.nodes.insert(0, value) 
    def insert(self, value):
        self.nodes.append(value)

    def parent(self, index): 
         
        if index == 0: 
            return None 
        return self.nodes[(index - 1) // 2]  
 
    def left_child(self, index): 
        child_index = 2 * index + 1 
        if child_index < len(self.nodes): 
            return self.nodes[child_index] 
        return None 
 
    def right_child(self, index): 
        child_index = 2 * index + 2 
        if child_index < len(self.nodes): 
            return self.nodes[child_index] 
        return None 
 
    def show_tree(self): 
        print("\nEstructura del Árbol Binario:") 
        for index, node in enumerate(self.nodes): 
            print(f"Índice {index}: {node}") 
 
# ============================================================ 
# 2. DUPLICACIÓN DE PUNTEROS / REFERENCIAS 
# ============================================================ 
 
@dataclass 
class Patient: 
    """Clase para representar los pacientes en la emergencia.""" 
    name: str 
    emergency_type: str 
    priority: int 
    arrival_order: int 
    cost: float 
    record: Optional["Patient"] = None   
 
    def duplicate_record(self): 
        """Duplica el registro de un paciente.""" 
        return Patient(self.name, self.emergency_type, self.priority, self.arrival_order, self.cost, self) 
 
# ============================================================ 
# 3. TEORÍA DE GRAFOS 
# ============================================================ 
 
class WeightedGraph: 
    def __init__(self): 
        self.graph = defaultdict(list) 
 
    def add_edge(self, origin, destination, weight): 
        """Agrega una conexión ponderada entre dos nodos""" 
        self.graph[origin].append((destination, weight)) 
        self.graph[destination].append((origin, weight)) 
 
    def dijkstra(self, start): 
        """Calcula las distancias más cortas desde el nodo de inicio usando Dijkstra""" 
        distances = {node: float("inf") for node in self.graph} 
        previous = {node: None for node in self.graph} 
 
        distances[start] = 0 
        queue = [(0, start)]   
        while queue: 
            current_distance, current_node = heapq.heappop(queue)   
 
            for neighbor, weight in self.graph[current_node]: 
                distance = current_distance + weight 
 
                if distance < distances[neighbor]: 
                    distances[neighbor] = distance 
                    previous[neighbor] = current_node 
                    heapq.heappush(queue, (distance, neighbor)) 
 
        return distances, previous 
 
    def shortest_path(self, previous, destination): 
        """Reconstruye el camino más corto desde el destino hacia el origen""" 
        path = [] 
        current = destination 
        while current is not None: 
            path.append(current) 
            current = previous[current] 
        return path[::-1]   
 
# ============================================================ 
# 4. EVALUACIÓN DE EXPRESIONES EN PARALELO 
# ============================================================ 
 
OPERATORS = { 
    "+": operator.add, 
    "-": operator.sub, 
    "*": operator.mul, 
    "/": operator.truediv 
} 
 
def evaluate_expression(expr): 
    """Evalúa una expresión aritmética representada como un árbol.""" 
    if isinstance(expr, (int, float)): 
        return expr 
 
    op, left, right = expr 

    if op not in OPERATORS:
        raise ValueError(f"Operador inválido: {op}")
    
    left_value = evaluate_expression(left) 
    right_value = evaluate_expression(right) 
 
    #if op == "/" and right_value == 0: 
    if op == "/" and abs(right_value) < 1e-9:
        raise ZeroDivisionError("No se puede dividir entre cero.") 
    
    return OPERATORS[op](left_value, right_value) 
 
def evaluate_expression_parallel(expr): 
    """Evalúa la expresión en paralelo utilizando hilos.""" 
    if isinstance(expr, (int, float)): 
        return expr 
 
    op, left, right = expr 
 
    if op not in OPERATORS:
        raise ValueError("Operador inválido")
    
    with ThreadPoolExecutor(max_workers=2) as executor: 
        #future_left = executor.submit(evaluate_expression, left) 
        #future_right = executor.submit(evaluate_expression, right)
        future_left = executor.submit(evaluate_expression_parallel, left)
        future_right = executor.submit(evaluate_expression_parallel, right) 
 
        left_value = future_left.result() 
        right_value = future_right.result() 
 
    if op == "/" and right_value == 0: 
        raise ZeroDivisionError("No se puede dividir entre cero.") 
    
    return OPERATORS[op](left_value, right_value) 
 
# ============================================================ 
# IMPLEMENTACIÓN DEL CASO : GESTIÓN DE RUTAS DE AMBULANCIA 
# ============================================================ 
 
def case_real_scenario(): 
    print("\nCASO REAL: Gestión de Rutas de Ambulancia y Atención Médica") 
 
    # Crear un árbol binario para almacenar emergencias 
    emergency_tree = CompleteBinaryTree() 
 
    # Crear pacientes 
    patient1 = Patient("Ana", "Accidente vehicular", 1, 1, 150.0) 
    patient2 = Patient("Luis", "Problema respiratorio", 2, 2, 120.0) 
    patient3 = Patient("Rosa", "Fractura", 1, 3, 180.0) 
    patient4 = Patient("Carlos", "Dolor abdominal", 3, 4, 100.0) 
 
    # Insertar pacientes en el árbol binario 
    emergency_tree.insert(patient1) 
    emergency_tree.insert(patient2) 
    emergency_tree.insert(patient3) 
    emergency_tree.insert(patient4) 
 
    # Duplicación de registros de pacientes 
    patient1_duplicate = patient1.duplicate_record()   
    #patient1.record = patient1_duplicate   
    print(f"\nRegistro duplicado de {patient1.name}: {patient1_duplicate}") 
 
    # Mostrar el árbol binario 
    emergency_tree.show_tree() 
 
    # Crear un grafo ponderado para las rutas de ambulancia 
    city_graph = WeightedGraph() 
    city_graph.add_edge("Hospital", "Av. Central", 4) 
    city_graph.add_edge("Hospital", "Av. Norte", 2) 
    city_graph.add_edge("Av. Norte", "Zona Industrial", 7) 
    city_graph.add_edge("Av. Central", "Zona Industrial", 3) 
    city_graph.add_edge("Av. Central", "Accidente", 6) 
    city_graph.add_edge("Zona Industrial", "Accidente", 2) 
 
    # Ejecutar Dijkstra para encontrar la ruta más corta 
    distances, previous = city_graph.dijkstra("Hospital")  
    path = city_graph.shortest_path(previous, "Accidente") 
 
    print(f"\nRuta más corta hacia Accidente: {' -> '.join(path)}") 
    print(f"Tiempo estimado para llegar: {distances['Accidente']} minutos") 
 
    # Evaluación del costo de atención para pacientes 
    patient_costs = [ 
        ("Ana", 150.0), 
        ("Luis", 120.0), 
        ("Rosa", 180.0), 
        ("Carlos", 100.0) 
    ] 
 
    print("\nEvaluación del costo total de atención médica:") 
    expressions = [] 
    for name, cost in patient_costs: 
        total_cost_expr = ("+", cost, 20)   
        expressions.append(total_cost_expr) 
 
    with ThreadPoolExecutor(max_workers=4) as executor: 
        results = list(executor.map(evaluate_expression_parallel, expressions)) 
 
    for i, result in enumerate(results): 
        name = patient_costs[i][0] 
        print(f"Paciente {name}: Costo total de atención = S/ {result:.2f}") 
 
# Llamar a la función del caso real 
case_real_scenario()
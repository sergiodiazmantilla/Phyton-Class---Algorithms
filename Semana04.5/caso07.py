from datetime import datetime

#Busqueda binaria recursiva
def busqueda_recursiva(lista, objetivo, campo, izq, der, pasos):
    if izq > der:
        return -1, pasos

    mid = (izq + der) // 2
    pasos += 1

    if lista[mid][campo] == objetivo:
        return mid, pasos
    elif lista[mid][campo] < objetivo:
        return busqueda_recursiva(lista, objetivo, campo, mid + 1, der, pasos)
    else:
        return busqueda_recursiva(lista, objetivo, campo, izq, mid - 1, pasos)
    
#Ejemplo de uso
if __name__ == "__main__":
    #Lista de diccionarios ordenada por 'nombre'
    personas = [
        {"nombre": "Ana", "edad": 30},
        {"nombre": "Carlos", "edad": 25},
        {"nombre": "David", "edad": 35},
        {"nombre": "Elena", "edad": 28},
        {"nombre": "Juan", "edad": 22}
    ]

    #Ordenar la lista por el campo 'nombre'
    personas.sort(key=lambda x: x['nombre'])

    objetivo = "David"
    inicio = datetime.now()
    indice, pasos = busqueda_recursiva(personas, objetivo, 'nombre', 0, len(personas) - 1, 0)
    fin = datetime.now()

    if indice != -1:
        print(f"Encontrado: {personas[indice]} en {pasos} pasos.")
    else:
        print("No encontrado.")
    
    print(f"Tiempo de ejecución: {(fin - inicio).total_seconds()} segundos.")

    
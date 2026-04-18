def variaciones(elementos, k, actual =[], resultado = None):
    if resultado is None:
        resultado = []
    if len(actual) == k:
        resultado.append(actual[:])
        return resultado
    for i in range(len(elementos)):
        if elementos[i] not in actual:
            actual.append(elementos[i])
            variaciones(elementos, k, actual, resultado)
            actual.pop()
    return resultado

simbolos = ['A', 'B', 'C', 'D']
resultado = variaciones(simbolos, 2)

for variacion in resultado:
    print(variacion)

#Apliaciones de las variaciones:
#1. En la generación de contraseñas seguras, donde se pueden utilizar diferentes caracteres y el orden es importante.
#2. En la planificación de eventos, donde se pueden organizar diferentes actividades en un orden específico.
#3. En la asignación de tareas, donde se pueden asignar diferentes tareas a diferentes personas en un orden específico.

#Diferencia entre variaciones y permutaciones:
#Las variaciones son arreglos de elementos donde el orden importa y no se permiten repeticiones. Por ejemplo, si tenemos los elementos A, B y C, las variaciones de 2 elementos serían AB, AC, BA, BC, CA y CB.
#Las permutaciones, por otro lado, son arreglos de elementos donde el orden importa y se permiten repeticiones. Por ejemplo, si tenemos los elementos A, B y C, las permutaciones de 2 elementos serían AA, AB, AC, BA, BB, BC, CA, CB y CC.

#En resumen, las variaciones no permiten repeticiones, mientras que las permutaciones sí lo hacen.

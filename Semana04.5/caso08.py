def permutaciones(lista):
    if len(lista) == 0:
        return [[]]
    else:
        resultado = []
        
    for i in range(len(lista)):
        actual = lista[i]
        resto = lista[:i] + lista[i+1:]

        for perm in permutaciones(resto):
            resultado.append([actual] + perm)
    return resultado

# Ejemplo de uso
sede = ["Lima", "Arequipa", "Trujillo"]
rutas = permutaciones(sede)

print("Permutaciones de visita:")
for ruta in rutas:
    print(ruta)

#Aplicación: En este caso, se generan todas las permutaciones posibles de las sedes de la empresa para planificar rutas de visita. Esto puede ser útil para optimizar el orden de las visitas y reducir costos de transporte.
#1. Se define la función `permutaciones` que toma una lista como argumento.
#2. Si la lista está vacía, se devuelve una lista que contiene una lista vacía.
#3. Se inicializa una lista `resultado` para almacenar las permutaciones.
#4. Se itera sobre cada elemento de la lista, seleccionando el elemento actual y el resto de la lista.
#5. Se llama recursivamente a la función `permutaciones` con el resto de la lista para obtener las permutaciones de los elementos restantes.
#6. Se agrega el elemento actual al inicio de cada permutación obtenida y se agrega a la lista de resultados.
#7. Finalmente, se devuelve la lista de permutaciones.

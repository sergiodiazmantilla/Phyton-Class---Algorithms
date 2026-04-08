def mayor_corriendo(lista):
    mayor = lista[0]
    for x in lista:
        if x > mayor:
            mayor = x
    return mayor

def mayor_ordenadas(lista):
    copia = lista[:]
    copia. sort()
    return copia[-1]

datos =[12, 7, 35, 11, 7]
print ("Mayor recorrido:", mayor_corriendo(datos))
print ("Mayor ordenado:", mayor_ordenadas(datos))

#Competidor que tiene el recorrido (Km) mayor o mas extenso

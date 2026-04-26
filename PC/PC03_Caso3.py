def quicksort(lista): 
    if len(lista) <= 1: 
        return lista 
 
    pivote = lista[len(lista) // 2] 
    menores = [x for x in lista if x < pivote] 
    iguales = [x for x in lista if x == pivote] 
    mayores = [x for x in lista if x > pivote] 
 
    return quicksort(menores) + iguales + quicksort(mayores) 
 
ventas = [320, 150, 800, 450, 210, 900, 120, 670] 
ranking = quicksort(ventas) 
 
print("Ventas ordenadas:", ranking)
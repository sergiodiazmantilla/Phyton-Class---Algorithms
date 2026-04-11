def quick_sort(lista):
    if len(lista) <= 1:
        return lista

    pivote = lista[len(lista) // 2]
    menor = [x for x in lista if x < pivote] #izquierda
    igual = [x for x in lista if x == pivote] #centro
    mayor = [x for x in lista if x > pivote] #derecha

    return quick_sort(menor) + igual + quick_sort(mayor)

ventas = [500, 200, 800, 100, 300, 400, 700, 600, 900, 1000]
ranking = quick_sort(ventas)
print("Ranking de ventas:", ranking)



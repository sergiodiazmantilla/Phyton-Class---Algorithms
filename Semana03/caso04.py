def mochila(items, capacidad):
    items.sort(key = lambda x: x[1]/x[0], reverse = True)

    total = 0

    for peso, valor in items:
        if capacidad >= peso:
            capacidad -= peso
            total += valor
    return total

items = [(10, 60), (20, 100), (30, 120)]
print("valor maximo", mochila(items, 50))
def maximo_divide_y_venceras(lista):
    if len(lista) == 1:
        return lista[0]

    medio = len(lista) // 2
    max_izquierda = maximo_divide_y_venceras(lista[:medio])
    max_derecha = maximo_divide_y_venceras(lista[medio:])

    return max(max_izquierda, max_derecha)

beneficios = [1000, 2000, 1500, 3000, 2500, 4000, 3500, 4500, 5000, 6000]
max_beneficio = maximo_divide_y_venceras(beneficios)
print("El máximo beneficio es:", max_beneficio)
def maximo_divide_y_venceras(lista): 
    if len(lista) == 1: 
        return lista[0] 
 
    medio = len(lista) // 2 
    max_izquierda = maximo_divide_y_venceras(lista[:medio]) 
    max_derecha = maximo_divide_y_venceras(lista[medio:]) 
 
    return max(max_izquierda, max_derecha) 
 
beneficios = [12000, 18500, 9700, 22300, 15600, 19800, 25000, 17400] 
mayor_beneficio = maximo_divide_y_venceras(beneficios) 
 
print("Mayor beneficio encontrado:", mayor_beneficio)
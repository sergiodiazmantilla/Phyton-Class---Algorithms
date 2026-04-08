def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    
    medio = len(lista) // 2
    izquierda = merge_sort(lista[:medio])
    derecha = merge_sort(lista[:medio])
    
    return merge(izquierda,derecha)

def merge(a, b):
    resultado=[]
    i = j = 0

    while i < len(a) and j < len (b):
        if a[i] < b[j]:
            resultado.append(a[i])
            i+=1
        else:
            resultado.append(b[j])
            j+=1
    resultado.extend(a[i:])
    resultado.extend(b[j:])
    return resultado


pila=[38, 27, 43, 3, 9]
print(merge_sort(pila))
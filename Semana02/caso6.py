#Contador de elementos
def contar_manual(lista):
    contador = 0
    for _ in lista:
        contador += 1
    return contador

def contar_python(lista):
    return len(lista)

datos = [5, 10, 20, 15, 8]
print("Manual:", contar_manual(datos))
print("Con len:", contar_python(datos))

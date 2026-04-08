def valor_maximo(lista):
    maximo = lista [0]
    for numero in lista:
        if numero > maximo:
         maximo = numero

    return maximo
datos = [8,3,15,2,20,7,10]
print("valor maximo:", valor_maximo(datos))

# Fusión en paralelo usando multiprocessing
# Explicacion
'''
Este ejemplo divide la fusión en subprocesos, 
combinando listas en paralelo para aumentar la eficiencia...
'''
from multiprocessing import Pool

#marge_pair fuera del parallel
'''
multiprocessing necesita serializar (pickle) las funciones que envía a otros procesos, 
y las funciones definidas dentro de otra función (funciones locales) no pueden serializarse.
'''
def merge_pair(l1, l2):
    return sorted(l1 + l2)

def merge_parallel(lists):
    with Pool(2) as pool:
        merged = pool.starmap(merge_pair, [(lists[0], lists[1]), (lists[2], lists[3])])
    
    return merge_pair(merged[0], merged[1])

# Importante:
'''
multiprocessing crea nuevos procesos reutilizando el archivo principal. 
Sin eso, pueden ocurrir errores o ejecuciones infinitas.
'''
if __name__ == "__main__":
    lists = [[1, 4], [2, 5], [3, 6], [7, 8]]
    print(merge_parallel(lists))
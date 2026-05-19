# Fusión en paralelo
# Concepto
'''
Combina dos o más listas ordenadas en una sola lista ordenada.
Ejemplo en Python: Fusión Simple
'''

# Explicacion
'''
Se combinan dos listas ordenadas comparando elemento por elemento, 
formando una lista ordenada final.
'''

def merge_sorted_lists(l1, l2):
    i = j = 0
    merged = []
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            merged.append(l1[i])
            i += 1
        else:
            merged.append(l2[j])
            j += 1
    return merged + l1[i:] + l2[j:]
print(merge_sorted_lists([1, 4, 6], [2, 3, 5]))
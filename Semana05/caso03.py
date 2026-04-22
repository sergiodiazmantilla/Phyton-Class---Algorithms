def lcs(a, b):
    m = len(a)
    n = len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp

def mostrar_tabla_lcs(dp, a, b):
    print("\n" + "-" * 80)
    print("    Tabla dp - subsecuencias comunes más largas(lcs)")
    print("-" * 80)

    print("    ", end="")
    for letra in b:
        print(f"{letra:>4}", end="")
    print()
    print("    " + "-" * (4*len(b)))

    for i in range(len(dp)):
        if i == 0:
            print("    ", end="")
        else:
            print(f"{a[i-1]:>4}", end="")
        for j in range(len(dp[0])):
            print(f"{dp[i][j]:>4}", end="")
        print()
        print("-" * 80)

def reconstruir_lcs(dp, a, b):
    i, j = len(a), len(b)
    resultado = []

    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:
            resultado.append(a[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return ''.join(reversed(resultado))

a = "AMAZON"
b = "AZON"

tabla = lcs(a, b)
mostrar_tabla_lcs(tabla, a, b)

longitud = tabla[len(a)][len(b)]
secuencia = reconstruir_lcs(tabla, a, b)

print(f"\nLa longitud de la subsecuencia común más larga es: {longitud}")
print(f"La subsecuencia común más larga es:", secuencia)

#Aplicaciones
#1. 
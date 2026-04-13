texto = "Programación en Python"
contador = 0

for caracter in texto.lower():
    if caracter in "aeiou":
        contador += 1
print("Cantidad de vocales encontradas:", contador)

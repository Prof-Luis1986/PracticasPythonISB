# Solicitar al usuario que ingrese una cadena
cadena = input("Ingresa una cadena: ")

# Definir las vocales
vocales = "aeiouAEIOU"

# Inicializar el contador de vocales
contador = 0

# Contar las vocales en la cadena
for letra in cadena:
    if letra in vocales:
        contador += 1

# Imprimir el número de vocales
print("El número de vocales en la cadena es:", contador)

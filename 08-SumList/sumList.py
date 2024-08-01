# Solicitar al usuario que ingrese una lista de números separados por espacios
numeros = list(map(int, input("Ingresa números separados por espacios: ").split()))

# Calcular la suma de los números en la lista
suma = sum(numeros)

# Imprimir la suma
print("La suma de la lista es:", suma)

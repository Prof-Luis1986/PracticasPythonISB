# Solicitar al usuario que ingrese una lista de números separados por espacios
numeros = list(map(int, input("Ingresa números separados por espacios: ").split()))

# Encontrar el número mayor
mayor = max(numeros)

# Imprimir el número mayor
print("El número mayor es:", mayor)

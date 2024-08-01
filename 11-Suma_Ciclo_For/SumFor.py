# Solicitar al usuario que ingrese un número
n = int(input("Ingresa un número: "))

# Inicializar la suma
suma = 0

# Usar un ciclo for para calcular la suma
for i in range(1, n + 1):
    suma += i

# Imprimir la suma
print("La suma de los primeros", n, "números naturales es:", suma)

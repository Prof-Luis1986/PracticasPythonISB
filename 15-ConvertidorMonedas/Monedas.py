# Define las tasas de cambio fijas
exchange_rates = {
    'USD': 0.053,  # 1 MXN a USD
    'EUR': 0.046,  # 1 MXN a EUR
    'GBP': 0.039,  # 1 MXN a GBP
    'MXN': 1       # 1 MXN a MXN (valor base)
}

def convertir_moneda(cantidad, de_moneda, a_moneda):
    if de_moneda != 'MXN':
        # Convertir de otra moneda a MXN primero
        cantidad = cantidad / exchange_rates[de_moneda]
    
    # Convertir de MXN a la moneda deseada
    cantidad_convertida = cantidad * exchange_rates[a_moneda]
    return cantidad_convertida

def mostrar_menu():
    print("Convertidor de Monedas")
    print("1. Pesos a Dólar")
    print("2. Pesos a Euro")
    print("3. Pesos a Libra Esterlina")
    print("4. Dólar a Pesos")
    print("5. Euro a Pesos")
    print("6. Libra Esterlina a Pesos")
    print("7. Salir")

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == '7':
        break

    cantidad = float(input("Ingrese la cantidad: "))
    de_moneda = ''
    a_moneda = ''

    if opcion == '1':
        de_moneda = 'MXN'
        a_moneda = 'USD'
    elif opcion == '2':
        de_moneda = 'MXN'
        a_moneda = 'EUR'
    elif opcion == '3':
        de_moneda = 'MXN'
        a_moneda = 'GBP'
    elif opcion == '4':
        de_moneda = 'USD'
        a_moneda = 'MXN'
    elif opcion == '5':
        de_moneda = 'EUR'
        a_moneda = 'MXN'
    elif opcion == '6':
        de_moneda = 'GBP'
        a_moneda = 'MXN'
    else:
        print("Opción no válida")
        continue

    resultado = convertir_moneda(cantidad, de_moneda, a_moneda)
    print(f"{cantidad} {de_moneda} es igual a {resultado:.2f} {a_moneda}")
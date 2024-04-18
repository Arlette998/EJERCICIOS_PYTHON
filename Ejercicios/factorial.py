def factorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

# Ingresa el número para calcular su factorial
numero = int(input("Ingresa un número para calcular su factorial: "))

# Calcula el factorial usando la función factorial
resultado = factorial(numero)

print("El factorial de", numero, "es:", resultado)

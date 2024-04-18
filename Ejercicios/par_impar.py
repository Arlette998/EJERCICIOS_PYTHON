def es_par_o_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"

# Ingresa el número para verificar si es par o impar
numero = int(input("Ingresa un número para verificar si es par o impar: "))

# Verifica si el número es par o impar
resultado = es_par_o_impar(numero)

print("El número", numero, "es", resultado)

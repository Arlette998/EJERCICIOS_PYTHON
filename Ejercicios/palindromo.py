def es_palindromo(frase):
    # Eliminar espacios en blanco y convertir a minúsculas
    frase = frase.replace(" ", "").lower()
    # Comparar la frase original con su reverso
    return frase == frase[::-1]

# Solicitar al usuario que ingrese una palabra o frase
entrada = input("Ingresa una palabra o frase para verificar si es un palíndromo: ")

# Verificar si la entrada es un palíndromo
if es_palindromo(entrada):
    print("¡La palabra o frase es un palíndromo!")
else:
    print("La palabra o frase no es un palíndromo.")

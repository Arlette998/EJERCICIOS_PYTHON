import math

def calcular_volumen_esfera(radio):
    volumen = (4/3) * math.pi * radio**3
    return volumen

# Ingresa el radio de la esfera
radio = float(input("Ingresa el radio de la esfera: "))

# Calcula el volumen
volumen = calcular_volumen_esfera(radio)

print("El volumen de la esfera con radio", radio, "es:", volumen)

def calcular_tiempo(distancia, velocidad):
    tiempo = distancia / velocidad
    return tiempo

# Solicitar la distancia y la velocidad al usuario
distancia = float(input("Ingresa la distancia que tiene que recorrer el carro (en kilómetros): "))
velocidad = float(input("Ingresa la velocidad del carro (en kilómetros por hora): "))

# Calcular el tiempo necesario para recorrer la distancia
tiempo = calcular_tiempo(distancia, velocidad)

# Mostrar el resultado
print("El tiempo necesario para recorrer", distancia, "kilómetros a una velocidad de", velocidad, "kilómetros por hora es de", tiempo, "horas.")

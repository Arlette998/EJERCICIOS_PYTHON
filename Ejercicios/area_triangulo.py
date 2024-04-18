def calcular_area_triangulo(base, altura):
    area = (base * altura) / 2
    return area

# Solicitar la base y la altura del triángulo al usuario
base = float(input("Ingresa la longitud de la base del triángulo: "))
altura = float(input("Ingresa la altura del triángulo: "))

# Calcular el área del triángulo
area = calcular_area_triangulo(base, altura)

# Mostrar el resultado
print("El área del triángulo es:", area)

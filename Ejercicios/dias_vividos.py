from datetime import datetime

def calcular_dias_vividos(fecha_nacimiento):
    # Obtener la fecha actual
    fecha_actual = datetime.now()

    # Convertir la fecha de nacimiento a un objeto datetime
    nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")

    # Calcular la diferencia entre la fecha actual y la fecha de nacimiento
    diferencia = fecha_actual - nacimiento

    # Obtener el número de días de la diferencia
    dias_vividos = diferencia.days

    return dias_vividos

# Solicitar la fecha de nacimiento al usuario
fecha_nacimiento = input("Ingresa tu fecha de nacimiento (en formato YYYY-MM-DD): ")

# Calcular los días vividos
dias_vividos = calcular_dias_vividos(fecha_nacimiento)

# Mostrar el resultado
print("Has vivido aproximadamente", dias_vividos, "días.")

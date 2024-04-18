from datetime import datetime

# Definir las fechas objetivo (Día de los Difuntos y Navidad)
dia_de_muertos = datetime(datetime.now().year, 11, 2)
navidad = datetime(datetime.now().year, 12, 25)

# Obtener la fecha actual
fecha_actual = datetime.now()

# Calcular los días que faltan para el Día de los Difuntos y Navidad
dias_para_dia_de_muertos = (dia_de_muertos - fecha_actual).days
dias_para_navidad = (navidad - fecha_actual).days

# Mostrar los resultados
print("Días que faltan para el Día de los Difuntos en Ecuador:", dias_para_dia_de_muertos)
print("Días que faltan para Navidad:", dias_para_navidad)

def es_bisiesto(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Solicitar al usuario que ingrese un año
year = int(input("Ingresa un año para verificar si es bisiesto: "))

# Verificar si el año es bisiesto
if es_bisiesto(year):
    print(year, "es un año bisiesto.")
else:
    print(year, "no es un año bisiesto.")

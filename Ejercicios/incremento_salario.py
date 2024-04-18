def calcular_incremento_salarial(salario):
    if salario < 15000:
        incremento = salario * 0.20
    else:
        incremento = salario * 0.15
    nuevo_salario = salario + incremento
    return nuevo_salario

# Solicitar el salario actual de la persona
salario_actual = float(input("Ingresa tu salario actual: "))

# Calcular el incremento salarial
nuevo_salario = calcular_incremento_salarial(salario_actual)

# Mostrar el resultado
print("Tu nuevo salario post incremento es:", nuevo_salario)

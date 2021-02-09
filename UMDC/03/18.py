"""
Ejercicio18

Suponiendo que el primer día del año fuese un lunes, escribir una función que reciba un número con el día del año,
y devuelva le día de la semana que le toca.

"""

def dia_semana(dia):
    semana = dia % 7
    if semana == 0:
        return "domingo"
    elif semana == 1:
        return "lunes"
    elif semana == 2:
        return "martes"
    elif semana == 3:
        return "miércoles"
    elif semana == 4:
        return "jueves"
    elif semana == 5:
        return "viernes"
    else:
        return "sabado"


print(dia_semana(3), dia_semana(9), dia_semana(0))
# Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celcius
#Recordar que la fórmula para la conversión es F= 9/5 * C + 32


def celcius(f):
    return (f - 32) * 5/9

leyendo = True
while leyendo:
    try:
        f = float(input("Introduzca temperatura en grados Fahrenheit: "))
        leyendo = False
    except ValueError:
        print("Introduzca un valor numérico\n")

print("La temperatura equivalente en grados Celcius es:", celcius(f))

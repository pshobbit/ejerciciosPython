"""

Ejercicio 10

Escribir un programa que le pida al usuario que ingrese una suceción de números naturales. Al final, el programa debe imprimir
cuántos números fueron ingresados, la suma total de los valores y el promedio.

"""

i = 0
total = 0

while True:
    leyendo = True
    while leyendo:
        try:
            n = float(input("Introduzca un número (ingrese el -1 para salir): "))
            leyendo = False
        except ValueError:
            print("Introduzca un valor numérico (ingrese el -1 para salir)  :")

    if  n == -1:
        break
    else:
        total += n
        i += 1

print("Se ingresaron ", i, " números que suman", total)
print("El promedio es de: ", total / i)
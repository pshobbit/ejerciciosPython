#Escribir un programa que imprima todos lo números pares entre dos números que se le pidan al usuario

leyendo = True
while leyendo:
    try:
        x = int(input("Introduce un número inicial: "))
        y = int(input("Introduce un valor final: "))
        leyendo = False
    except ValueError:
        print("Introduzca un solo valor numérico entero\n")


x = x % 2
for i in range(x, y +1, 2):
    print(i)
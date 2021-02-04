#Escribir un programa que tome una cantidad "m" de valores ingresados por el usuario,
#a cada uno le calcule el factorial e imprima el resultado
# junto con el número de orden correspondiente

def sucecion(n):
    resultado = 0
    for i in range(1, n + 1):
        resultado += i
    return resultado

def triangular(n):
    return int(n * (n +1) / 2)

leyendo = True
while leyendo:
    try:
        n = int(input("Introduzca un número: "))
        leyendo = False
    except ValueError:
        print("Introduzca solo valores numéricos enteros\n")

for i in range(1, n + 1):
    print (i,"  -  ",sucecion(i))
    sucecion(i)

print("====================================================")

for i in range(1, n + 1):
    print(i, "  -  ", triangular(i))
    triangular(i)


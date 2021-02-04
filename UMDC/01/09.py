#Modificar el programa anterior para que pueda generar fichas de un juego que puede tener númeos de 0 a m




leyendo = True
while leyendo:
    try:
        n = int(input("Introduzca número máximo del dominó (n <= 6): "))
        leyendo = False
    except ValueError:
        print("Introduzca solo valores numéricos enteros\n")

for i in range(n+1):
    for j in range(i, n+1):
        print(i, j)
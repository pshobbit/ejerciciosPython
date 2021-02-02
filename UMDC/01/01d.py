#Escribir un programa que use un ciclo definido con rango numérico,
# que averigüe a cuantos amigos quieren saludar, les pregunte los nombre y salude.

leyendo = True
while leyendo:
    numero = input("Introduce cuántos amigos tienes: ")
    try:
        numero = int(numero)
        leyendo = False
    except ValueError:
        print(numero, " no es un número, prueba de nuevo.")

for n in range(numero):
    nombre = input ("Introduce tu amigo: ")
    print("Hola", nombre);


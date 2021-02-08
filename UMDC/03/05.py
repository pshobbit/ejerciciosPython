"""
Ejercicio 05
Manejo de contraseñas
Escribir un programa que contenga una contraseña inventada, que le pregunte
al usuario la contraseña, y no le permita continuar hasta que la haya
ingresado correctamente.
"""
from time import sleep

"""
contrasena = "contra"
while True:
    con = input("Contraseña : ")
    if con == contrasena:
        print("Contraseña correcta")
        break
    else:
        print("Contraseña errónea")
Modificar el programa anterior para que solamente permita una cantidad fija de
intentos.
contrasena = "contra"
intentos = 3
while intentos:
    con = input("Contraseña : ")
    if con == contrasena:
        print("Contraseña correcta")
        break
    else:
        print("Contraseña errónea")
        intentos -= 1
Modificar el programa anterior para que después de cada intento agregue una
pausa cada vez mayor, utilizando la función sleep del módulo time.

"""


contrasena = "contra"
maxIntentos = 5
intentos = maxIntentos

while intentos != 0:
    con = input("Contraseña: ")
    if con == contrasena:
        print("Contraseña Correcta:")
        break
    else:
        print("Contraseña Incorrecta:")
        intentos -= 1
        if intentos > 0:
            sleep((10 - int (10/maxIntentos * intentos)))
            print(10 - int(10 / maxIntentos * intentos))

def passwords():
    from time import sleep
    contrasena = "contra"
    maxIntentos = 5
    intentos = maxIntentos
    while intentos != 0:
        con = input("Contraseña: ")
        if con == contrasena:
            print("Contraseña Correcta: ")
            return True
        else:
            print("Contraseña Incorrecta: ")
            intentos -= 1
            if  intentos > 0:
                sleep(10-int(10/maxIntentos*intentos))
    return False



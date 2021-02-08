"""
Ejercicio 02

Escribir una implementación propia de la función abs, que devuelva el valor absoluto de cualquier valor que reciba.

"""



def abs2(n):
    if  n< 0:
        n = -n
    return n


n = int(input("Dime un número"))

print(abs2(n))

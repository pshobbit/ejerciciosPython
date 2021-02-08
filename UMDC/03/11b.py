"""

Ejercicio 11b

Escribir una función que reciba dos números cómo parámetros, y devuelva cuántos múltiplos dle primero hay, que sean menores que el sgundo

"""

def numMul(m,n):
    i = 0
    mul = m
    while mul <= n:
        i += 1
        mul *= i
    return (i - 1)

print(numMul(12, 360))


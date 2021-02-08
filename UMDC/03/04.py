"""
Ejercicio 04
Escribir una función que reciba un número entero e imprima su descomposición en factores primos.
>>> factoresPrimos(24)
1
2
2
2
3
>>> factoresPrimos(100)
1
2
2
5
5
>>> factoresPrimos(12)
1
2
2
3
>>> factoresPrimos(11)
1
11
>>> factoresPrimos(1)
1
>>> factoresPrimos(0)
1
"""

def factoresPrimos(n):
    if n < 2:
        print(1)
    else:
        i = 2
        print(1)
        while (n / 2 + 1) > i:
            if n % i == 0:
                print(i)
                n //= i
            else:
                i += 1
        print(n)

if __name__ == '__main__':
    import doctest
    doctest.testmod()

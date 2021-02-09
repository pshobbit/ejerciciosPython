"""

Escribir una función que reciba dos vectores y devuelva si son o no octogonales.

>>> octogonal((1, 4), (6, 2))
False
>>> octogonal((1, 4, 5), (6, 2, 3))
False
>>> octogonal((1, 0, 0), (0, 1, 1))
True
"""


def scalar(x, y):
    p = list()
    for i in range(len(x)):
        p.append(x[i]*y[i])
    return sum(p)


def octogonal(x, y):
    return scalar(x, y) == 0


if __name__ == "__main__":
    import doctest
    doctest.testmod()
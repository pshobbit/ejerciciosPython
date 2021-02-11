"""
Ejercicio 01e

Escribir funciones que dada una cadena de caractareres:

Imprima la cadena en un sentido y en sentido inverso.

 ### TESTS

>>> cad = "En un lugar de la Mancha"
>>> reflejo(cad)
'En un lugar de la ManchaahcnaM al ed ragul nu nE'
>>> reflejo('reflejo')
'reflejoojelfer'
>>> reflejo_2('reflejo')
'reflejoojelfer'

"""

def reflejo(cad):
    salida = cad
    for i in range(len(cad)-1, -1, -1):
        salida += cad[i]
    return (salida)

def reflejo_2(cad):
    return (cad + cad[::-1])


cad = "En un lugar de la Mancha de cuyo nombre no quiero acordarme"
print(reflejo(cad))
print(reflejo("reflejo-->"))
print(reflejo_2("reflejo"))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
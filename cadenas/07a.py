"""

Ejercicio 7a
Escribir funciones que dadas dos cadenas de caracteres:
Indique si la segunda cadena es una subcadena de la primera. Por ejemplo,
"cadena" es una subcadena de "subcadena".

### TESTS
>>> subcadena("subcadena", "cadena")
True
>>> subcadena("subcalena", "cadena")
False
>>> subcadena_2("subcadena", "cadena")
True
>>> subcadena_2("subcalena", "cadena")
False

"""

def subcadena(cad, subcad):
    return cad.find(subcad) != -1

def subcadena_2(cad, subcad):
    return subcad in cad

print(subcadena("subcadena", "cadena"))
print(subcadena_2("subcadena", "cadena"))
print()
print(subcadena_2("hola", "adios"))
print(subcadena("hola", "adios"))



if __name__ == '__main__':
    import doctest
    doctest.testmod()
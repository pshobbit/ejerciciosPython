"""
Ejercicio 01

Escribe una función que reciba un nombre de fichero, lo abra, lo lea y visualice el contenido en mayúsculas.
Usar los ficheros "words.txt y test.txt"

"""

def file_cap(file_name):
    try:
        file_handle = open(file_name)
    except IOError:
        return -1
    text = ''
    for line in file_handle:
        text += line.upper()
    return text

file_cap("words.txt")
file_cap("test.txt")

if __name__ == '__main__':
    import doctest
    doctest.testmod()
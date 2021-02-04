# Escribir dos funciones que permitan calcular:
# -> La cantidad de segundos en un tiempo dado en horas, minutos y segundos.
# -> La cantidad de horas, minutos y segundos dados en segundos.


def aSegundos(h, m, s):
    return ((h * 60) + m)* 60 + s

def aHoras(s):
    horas = s/3600
    s = s % 3600
    minutos = s//60
    segundos = s % 60
    return (horas, minutos, segundos)

if __name__ == '__m':
    import doctest
    doctest.testmod()
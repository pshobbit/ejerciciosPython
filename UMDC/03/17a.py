"""
Ejercicio 17a

Escribir funciones que resuelvan los siguientes problemas:

Dado un año indicar si es Bisiesto o no.


"""

def bisiesto(anno):
    if anno % 4:
        return False
    else:
        if anno % 100:
            return True
        else:
            if  anno % 400:
                return False
            else:
                return True
            
print(bisiesto(2017), bisiesto(2016), bisiesto(2020), bisiesto(1800))
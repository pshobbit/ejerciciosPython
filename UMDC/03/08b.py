"""
Ejercicio 08b

Escribir una función que, dados dos números naturales pasados cómo parámetros, devuelva la suma de todaslas potencias de 2, que hay en el rango
formado por esos números (0 si no hay ninguna potencia de 2 entre los dos).
Utilizar la función es_potencia-de_dos, descrita en el punto anterior.

"""

def es_potencia_de_dos(n):
    while n != 1:
        if (n % 2) == 0:
            n = n / 2
        else:
            return False
    return True

def suma_potencias_dos(a,b):
    suma = 0
    for n in range(a , b + 1):
        if es_potencia_de_dos(n):
            suma += n
    return suma

print(suma_potencias_dos(6,15))
print(suma_potencias_dos(17,30))




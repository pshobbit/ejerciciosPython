"""
Ejercicio 17e

Escribir funciones que resuelvan los siguientes problemas:
Dada una fecha, indicar los dias que faltan hasta fin de año.

"""

def bisiesto(anno):
    if anno % 4:
        return False
    else:
        if anno % 100:
            return True
        else:
            if anno % 400:
                return False
            else:
                return True


def dias_mes(mes, anno):
    if mes in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif mes in (4, 6, 9, 11):
        return 30
    elif mes == 2:
        if bisiesto(anno):
            return 29
        else:
            return 28
    else:
        return -1


def validar_fecha(dia, mes, anno):
    dm = dias_mes(mes, anno)
    if dm == -1:
        return -1
    if dm < dia:
        return False
    elif mes > 12:
        return False
    else:
        return True


def dias_faltan(dia, mes, anno):
    if validar_fecha(dia, mes, anno):
        return dias_mes(mes, anno)-dia
    else:
        return -1


print(dias_faltan(1, 1, 2000))


def dias_fin_anno(dia, mes, anno):
    if validar_fecha(dia, mes, anno):
        dias = 0
        for m in range(mes+1, 12+1):
            dias += dias_mes(m, anno)
        dias += dias_faltan(dia, mes, anno)
        return dias
    else:
        return -1


print(dias_fin_anno(31, 12, 2000), dias_fin_anno(30, 11, 2000),
      dias_fin_anno(1, 1, 2015), dias_fin_anno(1, 1, 2016))
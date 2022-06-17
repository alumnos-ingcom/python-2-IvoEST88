################
# Nombre - @IvoEST88
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
1. Pares e impares
"""
# Escribir una función que retorne `True` cuando un número entero es par
# `False` cuando no lo sea, sin utilizar módulo. (`%`)


def es_par(numero):
    """
    Funcion que determina si un numero es par o impar
    """
    if numero < 0:
        numero *= -1
        signo = -1
    else:
        signo = 1
    while numero > 0:
        numero -= 2
    if numero != 0:
        resultado = False
        numero *= signo
    else:
        resultado = True
        numero *= signo
    return resultado


def principal():
    """
    Programa
    """
    numero = int(input("Ingrese un número: "))
    resultado_es_par = es_par(numero)
    if resultado_es_par is True:
        print(f"El número {numero} es Par")
    else:
        print(f"El número {numero} es Impar")


if __name__ == "__main__":
    principal()

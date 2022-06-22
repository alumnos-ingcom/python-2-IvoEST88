################
# Nombre - @IvoEST88
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
5. Corchetes balanceados
"""
# Implementar una función que determine si una cadena con corchetes
# está balanceada.


def es_balanceado(cadena):
    """
    Funcion con corchetes, llaves y parentesis
    """
    contador = 0
    corchete_abierto = "["
    corchete_cerrado = "]"
    if cadena[0] == corchete_cerrado:
        resultado = False
        contador -= 1
    else:
        for i in cadena:
            if i == corchete_abierto:
                contador += 1
            if i == corchete_cerrado:
                contador += 1
    if contador % 2 != 0:
        resultado = False
    if contador % 2 == 0:
        resultado = True
    return resultado


def principal():
    """
    Programa fachero facherito
    """
    cadena = input("Ingrese cadena: ")
    resultado = es_balanceado(cadena)
    print(resultado)


if __name__ == "__main__":
    principal()

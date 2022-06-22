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
    contador_abiertos = 0
    contador_cerrados = 0
    corchete_abierto = ["[", "(", "{"]
    corchete_cerrado = ["]", ")", "}"]
    vueltas = 0
    while vueltas != 3:
        if cadena[0] == corchete_cerrado:
            resultado = False
            contador -= 1
        else:
            for i in cadena:
                if i == corchete_abierto[vueltas]:
                    contador_abiertos += 1
                if i == corchete_cerrado[vueltas]:
                    contador_cerrados += 1
        vueltas += 1
    if contador_abiertos - contador_cerrados == 0:
        resultado = True
    else:
        resultado = False
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

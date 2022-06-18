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
    abierto = ["{", "[", "("]
    long_abierto = len(abierto)
    cerrado = ["}", "]", ")"]
    long_cerrado = len(cerrado)
    contador = 0
    vueltas = 0
    long_cadena = len(cadena)
    while vueltas < long_cadena:
        abierto_vueltas = 0
        cerrado_vueltas = 0
        while abierto_vueltas < long_abierto:
            if cadena[vueltas] == abierto[abierto_vueltas]:
                contador += 1
                abierto_vueltas += 1
            else:
                abierto_vueltas += 1
        while cerrado_vueltas < long_cerrado:
            if cadena[vueltas] == cerrado[cerrado_vueltas]:
                contador -= 1
                cerrado_vueltas += 1
            else:
                cerrado_vueltas += 1
        if contador < 0:
            resultado = False
            break
        vueltas += 1
    if contador != 0:
        resultado = False
    else:
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

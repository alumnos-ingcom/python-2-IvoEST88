################
# Nombre - @IvoEST88
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
4. Fibonacci
"""
# Implementar una función que permita obtener el n-esimo termino de la
# sucesión de Fibonacci. Siendo este número un entero positivo mayor a 2.


def fibonacci(limite):
    """
    Función de la sucesion fibonacci
    """
    num_uno = 0
    num_dos = 1
    if limite <= 2:
        resultado = "Error"
    else:
        for i in range(limite):
            num_tres = num_uno + num_dos
            num_uno = num_dos
            num_dos = num_tres
            resultado = num_tres
    return resultado


def principal():
    """
    Programa donde ingresa el n-esimo numero a mostrar
    """
    limite = int(input("Ingrese el termino que quiere ver: "))
    resultado = (fibonacci(limite))
    print(resultado)


if __name__ == "__main__":
    principal()

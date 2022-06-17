################
# Nombre - @IvoEST88
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def min_max_promedio(secuencia):
    """
    Funcion que determina el valor minimo, maximo y el promedio
    los numeros ingresados
    """
    long_secuencia = len(secuencia)
    mayor = secuencia[0]
    menor = secuencia[0]
    promedio = 0
    vueltas = 0
    while vueltas < long_secuencia:
        promedio += secuencia[vueltas]
        if secuencia[vueltas] < menor:
            menor = secuencia[vueltas]
        if secuencia[vueltas] > mayor:
            mayor = secuencia[vueltas]
        vueltas += 1
    promedio = (promedio // long_secuencia)
    lista = [menor, mayor, promedio]
    tupla = tuple(lista)
    return tupla


def principal():
    """
    Programa
    """
    limite_secuencia = int(input("¿Cuántos números desea ingresar?: "))
    secuencia = []
    print("Ingrese: ")
    while limite_secuencia > 0:
        numero = int(input())
        secuencia.append(numero)
        limite_secuencia -= 1
    print(min_max_promedio(secuencia))


if __name__ == "__main__":
    principal()

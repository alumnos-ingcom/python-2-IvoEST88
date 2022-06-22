################
# Nombre - @IvoEST88
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Tests de los ejercicios en la carpeta src
"""
from src.ejercicio2 import min_max_promedio


def test_basico():
    """
    Test con tres valores positivos
    """
    secuencia = (9, 10, 11)
    resultado = min_max_promedio(secuencia)
    assert isinstance(resultado, tuple), "El resultado debe ser (9, 11, 10)"
    assert resultado == (9, 11, 10), "El resultado no es el esperado"


def test_negativos():
    """
    Test con tres valores negativos
    """
    secuencia = (-9, -10, -11)
    resultado = min_max_promedio(secuencia)
    assert isinstance(resultado, tuple), "El resultado debe ser (-11, -9, -10)"
    assert resultado == (-11, -9, -10), "El resultado no es el esperado"


def test_negativo_primero():
    """
    Test con el primer valor negativo
    """
    secuencia = (-9, 10, 11)
    resultado = min_max_promedio(secuencia)
    assert isinstance(resultado, tuple), "El resultado debe ser (-9, 11, 4)"
    assert resultado == (-9, 11, 4), "El resultado no es el esperado"


def test_negativo_segundo():
    """
    Test con el segundo valor ingresado siendo negativo
    """
    secuencia = (9, -10, 11)
    resultado = min_max_promedio(secuencia)
    assert isinstance(resultado, tuple), "El resultado debe ser (-10, 11, 3)"
    assert resultado == (-10, 11, 3), "El resultado no es el esperado"


def test_negativo_tercero():
    """
    Test con el tercer valor ingresado siendo negativo
    """
    secuencia = (9, 10, -11)
    resultado = min_max_promedio(secuencia)
    assert isinstance(resultado, tuple), "El resultado debe ser (-11, 10, 2)"
    assert resultado == (-11, 10, 2), "El resultado no es el esperado"


def test_negativo_primeros():
    """
    Test con los primeros dos valores ingresados negativos
    """
    secuencia = (-9, -10, 11)
    resultado = min_max_promedio(secuencia)
    assert isinstance(resultado, tuple), "El resultado debe ser (-10, 11, -3)"
    assert resultado == (-10, 11, -3), "El resultado no es el esperado"


def test_negativos_ultimos():
    """
    Test con los ultimos dos valores ingresados negativos
    """
    secuencia = (9, -10, -11)
    resultado = min_max_promedio(secuencia)
    assert isinstance(resultado, tuple), "El resultado debe ser (-11, 9, -4)"
    assert resultado == (-11, 9, -4), "El resultado no es el esperado"


def test_negativo_primero_ultimo():
    """
    Test con el primer y el ultimo valor negativo
    """
    secuencia = (-9, 10, -11)
    resultado = min_max_promedio(secuencia)
    assert isinstance(resultado, tuple), "El resultado debe ser (-11, 10, -4)"
    assert resultado == (-11, 10, -4), "El resultado no es el esperado"

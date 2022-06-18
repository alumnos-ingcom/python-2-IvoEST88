################
# Nombre - @IvoEST88
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Tests de los ejercicios en la carpeta src
"""
from src.ejercicio4 import fibonacci


def test_fibonacci():
    """
    Obtener el termino nº4 de la sucesion
    """
    limite = 4
    resultado = fibonacci(limite)
    assert isinstance(resultado, int), "El resultado debe ser 34"
    assert resultado == 34, "El resultado no es el esperado"


def test_fibonacci_lim1():
    """
    Obtener el termino nº1 de la sucesion
    """
    limite = 1
    resultado = fibonacci(limite)
    assert isinstance(resultado, int), "El resultado debe ser 2"
    assert resultado == 2, "El resultado no es el esperado"


def test_fibonacci_lim0():
    """
    Obtener el termino nº0 de la sucesion
    """
    limite = 0
    resultado = fibonacci(limite)
    assert isinstance(resultado, str), "El resultado debe ser 2"
    assert resultado == "Error", "El resultado no es el esperado"


def test_fibonacci_lim10():
    """
    Obtener el termino nº10 de la sucesion
    """
    limite = 10
    resultado = fibonacci(limite)
    assert isinstance(resultado, int), "El resultado debe ser 2"
    assert resultado == 10946, "El resultado no es el esperado"


def test_fibonacci_lim100():
    """
    Obtener el termino nº10 de la sucesion
    """
    limite = 100
    resultado = fibonacci(limite)
    assert isinstance(resultado, int), "El resultado debe ser 2"
    assert resultado == 453973694165307953197296969697410619233826, "El resultado no es el esperado"
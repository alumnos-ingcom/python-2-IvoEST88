################
# Nombre - @IvoEST88
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Tests de los ejercicios en la carpeta src
"""
from src.ejercicio1 import es_par


def test_es_par_true_cero():
    """
    Test con valor 0
    """
    numero = 0
    resultado = es_par(numero)
    assert isinstance(resultado, bool), "El resultado esperado es True"
    assert resultado is True, "El resultado no es el esperado"


def test_es_par_positivotrue():
    """
    Test con valor 2
    """
    numero = 2
    resultado = es_par(numero)
    assert isinstance(resultado, bool), "El resultado esperado es True"
    assert resultado is True, "El resultado no es el esperado"


def test_es_par_positivofalse():
    """
    Test con valor 1
    """
    numero = 1
    resultado = es_par(numero)
    assert isinstance(resultado, bool), "El resultado esperado es False"
    assert resultado is False, "El resultado no es el esperado"


def test_es_par_negativotrue():
    """
    Test con valor -2
    """
    numero = -2
    resultado = es_par(numero)
    assert isinstance(resultado, bool), "El resultado esperado es True"
    assert resultado is True, "El resultado no es el esperado"


def test_es_par_negativofalse():
    """
    Test con valor 0
    """
    numero = -1
    resultado = es_par(numero)
    assert isinstance(resultado, bool), "El resultado esperado es False"
    assert resultado is False, "El resultado no es el esperado"

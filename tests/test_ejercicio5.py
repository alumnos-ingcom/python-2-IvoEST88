################
# Nombre - @IvoEST88
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Tests de los ejercicios en la carpeta src
"""
from src.ejercicio5 import es_balanceado


def test_es_balanceado_corchetes_true1():
    """
    Test con corchetes
    """
    cadena = "[]"
    resultado = es_balanceado(cadena)
    assert isinstance(resultado, bool), "El resultado esperado es True"
    assert resultado is True, "El resultado no es el esperado"


def test_es_balanceado_corchetes_true2():
    """
    Test con corchetes colocados de forma variada
    """
    cadena = "[[]]"
    resultado = es_balanceado(cadena)
    assert isinstance(resultado, bool), "El resultado esperado es True"
    assert resultado is True, "El resultado no es el esperado"


def test_es_balanceado_corchetes_true3():
    """
    Test con corchetes colocados de forma variada
    """
    cadena = "[][]"
    resultado = es_balanceado(cadena)
    assert isinstance(resultado, bool), "El resultado esperado es True"
    assert resultado is True, "El resultado no es el esperado"


def test_es_balanceado_corchetes_false1():
    """
    Test con corchetes colocados de forma variada
    """
    cadena = "[[]"
    resultado = es_balanceado(cadena)
    assert isinstance(resultado, bool), "El resultado esperado es False"
    assert resultado is False, "El resultado no es el esperado"


def test_es_balanceado_corchetes_false2():
    """
    Test con corchetes colocados de forma variada
    """
    cadena = "[]]"
    resultado = es_balanceado(cadena)
    assert isinstance(resultado, bool), "El resultado esperado es False"
    assert resultado is False, "El resultado no es el esperado"


def test_es_balanceado_corchetes_false3():
    """
    Test con corchetes colocados de forma variada
    """
    cadena = "][]"
    resultado = es_balanceado(cadena)
    assert isinstance(resultado, bool), "El resultado esperado es False"
    assert resultado is False, "El resultado no es el esperado"


def test_es_balanceado_corchetes_false4():
    """
    Test con corchetes colocados de forma variada
    """
    cadena = "[]["
    resultado = es_balanceado(cadena)
    assert isinstance(resultado, bool), "El resultado esperado es False"
    assert resultado is False, "El resultado no es el esperado"

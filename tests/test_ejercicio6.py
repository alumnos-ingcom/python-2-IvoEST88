################
# Nombre - @IvoEST88
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Tests de los ejercicios en la carpeta src
"""
from src.ejercicio6 import codificar, decodificar


def test_codificar_hola():
    """
    Test de codificar con texto minuscula
    """
    texto = "hola"
    ajuste = 13
    resultado = codificar(texto, ajuste)
    assert isinstance(resultado, list), "El resultado debe ser ['u', '1', 'y', 'n']"
    assert resultado == ['u', '1', 'y', 'n'], "El resultado no es el esperado"


def test_codificar_numeros():
    """
    Test de codificar con numeros
    """
    texto = "123"
    ajuste = 13
    resultado = codificar(texto, ajuste)
    assert isinstance(resultado, list), "El resultado debe ser ['>', '?', '@']"
    assert resultado == ['>', '?', '@'], "El resultado no es el esperado"


def test_codificar_HOLA():
    """
    Test de codificar con texto mayuscula
    """
    texto = "HOLA"
    ajuste = 13
    resultado = codificar(texto, ajuste)
    assert isinstance(resultado, list), "El resultado debe ser ['U', '\\', 'Y', 'N']"
    assert resultado == ['U', '\\', 'Y', 'N'], "El resultado no es el esperado"


def test_codificar_iV0():
    """
    Test de codificar con texto mixto
    """
    texto = "iV0"
    ajuste = 13
    resultado = codificar(texto, ajuste)
    assert isinstance(resultado, list), "El resultado debe ser ['v', 'c', '=']"
    assert resultado == ['v', 'c', '='], "El resultado no es el esperado"


def test_decodificar_hola():
    """
    Test de decodificar con texto minuscula
    """
    resultado = ['u', '1', 'y', 'n']
    ajuste = 13
    resultado_final = decodificar(resultado, ajuste)
    assert isinstance (resultado_final, list), "El resultado debe ser ['h', 'o', 'l', 'a']"
    assert resultado_final == ['h', 'o', 'l', 'a'], "El resultado no es el esperado"


def test_decodificar_numeros():
    """
    Test de decodificar con numero
    """
    resultado = ['>', '?', '@']
    ajuste = 13
    resultado_final = decodificar(resultado, ajuste)
    assert isinstance (resultado_final, list), "El resultado debe ser ['1', '2', '3']"
    assert resultado_final == ['1', '2', '3'], "El resultado no es el esperado"


def test_decodificar_HOLA():
    """
    Test de decodificar con texto mayuscula
    """
    resultado = ['U', '\\', 'Y', 'N']
    ajuste = 13
    resultado_final = decodificar(resultado, ajuste)
    assert isinstance(resultado_final, list), "El resultado debe ser ['H', 'O', 'L', 'A']"
    assert resultado_final == ['H', 'O', 'L', 'A'], "El resultado no es el esperado"


def test_decodificar_iV0():
    """
    Test de decodificar con texto mixto
    """
    resultado = ['v', 'c', '=']
    ajuste = 13
    resultado_final = decodificar(resultado, ajuste)
    assert isinstance(resultado_final, list), "El resultado debe ser ['i', 'V', '0']"
    assert resultado_final == ['i', 'V', '0'], "El resultado no es el esperado"
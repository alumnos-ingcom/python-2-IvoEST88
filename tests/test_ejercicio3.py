################
# Nombre - @IvoEST88
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Tests de los ejercicios en la carpeta src
"""
from src.ejercicio3 import superposicion


def test_superposicion():
    """
    test con dos palabras basicas
    """
    frase1 = "hola"
    frase2 = "casa"
    resultado = superposicion(frase1, frase2)
    assert isinstance(resultado, int), "El resultado debe ser 1"
    assert resultado == 1, "El resultado no es el esperado"


def test_superposicion_2():
    """
    test con una frase y una palabra
    """
    frase1 = "hola mundo"
    frase2 = "hola"
    resultado = superposicion(frase1, frase2)
    assert isinstance(resultado, int), "El resultado debe ser 4"
    assert resultado == 4, "El resultado no es el esperado"


def test_superposicion_3():
    """
    test con dos palabras sin ninguna letra en común
    """
    frase1 = "perro"
    frase2 = "casa"
    resultado = superposicion(frase1, frase2)
    assert isinstance(resultado, int), "El resultado debe ser 0"
    assert resultado == 0, "El resultado no es el esperado"

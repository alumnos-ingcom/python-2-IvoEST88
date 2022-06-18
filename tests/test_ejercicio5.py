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


def test_es_balanceado_parentesis_true1():
    """
    Test con parentesis
    """
    cadena = "()"
    resultado = es_balanceado(cadena)
    assert isinstance(resultado, bool), "El resultado esperado es True"
    assert resultado is True, "El resultado no es el esperado"


def test_es_balanceado_parentesis_true2():
    """
    Test con parentesis colocados de forma variada
    """
    cadena = "(())"
    resultado = es_balanceado(cadena)
    assert isinstance(resultado, bool), "El resultado esperado es True"
    assert resultado is True, "El resultado no es el esperado"


def test_es_balanceado_parentesis_true3():
    """
    Test con parentesis colocados de forma variada
    """
    cadena = "()()"
    resultado = es_balanceado(cadena)
    assert isinstance(resultado, bool), "El resultado esperado es True"
    assert resultado is True, "El resultado no es el esperado"


def test_es_balanceado_parentesis_false1():
    """
    Test con parentesis colocados de forma variada
    """
    cadena = "(()"
    resultado = es_balanceado(cadena)
    assert isinstance(resultado, bool), "El resultado esperado es False"
    assert resultado is False, "El resultado no es el esperado"


def test_es_balanceado_parentesis_false2():
    """
    Test con parentesis colocados de forma variada
    """
    cadena = "())"
    resultado = es_balanceado(cadena)
    assert isinstance(resultado, bool), "El resultado esperado es False"
    assert resultado is False, "El resultado no es el esperado"


def test_es_balanceado_parentesis_false3():
    """
    Test con parentesis colocados de forma variada
    """
    cadena = ")()"
    resultado = es_balanceado(cadena)
    assert isinstance(resultado, bool), "El resultado esperado es False"
    assert resultado is False, "El resultado no es el esperado"


def test_es_balanceado_parentesis_false4():
    """
    Test con parentesis colocados de forma variada
    """
    cadena = "()("
    resultado = es_balanceado(cadena)
    assert isinstance(resultado, bool), "El resultado esperado es False"
    assert resultado is False, "El resultado no es el esperado"


def test_es_balanceado_llaves_true1():
    """
    Test con llaves
    """
    cadena = "{}"
    resultado = es_balanceado(cadena)
    assert isinstance(resultado, bool), "El resultado esperado es True"
    assert resultado is True, "El resultado no es el esperado"


def test_es_balanceado_llaves_true2():
    """
    Test con llaves colocados de forma variada
    """
    cadena = "{{}}"
    resultado = es_balanceado(cadena)
    assert isinstance(resultado, bool), "El resultado esperado es True"
    assert resultado is True, "El resultado no es el esperado"


def test_es_balanceado_llaves_true3():
    """
    Test con llaves colocados de forma variada
    """
    cadena = "{}{}"
    resultado = es_balanceado(cadena)
    assert isinstance(resultado, bool), "El resultado esperado es True"
    assert resultado is True, "El resultado no es el esperado"


def test_es_balanceado_llaves_false1():
    """
    Test con llaves colocados de forma variada
    """
    cadena = "{{}"
    resultado = es_balanceado(cadena)
    assert isinstance(resultado, bool), "El resultado esperado es False"
    assert resultado is False, "El resultado no es el esperado"


def test_es_balanceado_llaves_false2():
    """
    Test con llaves colocados de forma variada
    """
    cadena = "{}}"
    resultado = es_balanceado(cadena)
    assert isinstance(resultado, bool), "El resultado esperado es False"
    assert resultado is False, "El resultado no es el esperado"


def test_es_balanceado_llaves_false3():
    """
    Test con llaves colocados de forma variada
    """
    cadena = "}{}"
    resultado = es_balanceado(cadena)
    assert isinstance(resultado, bool), "El resultado esperado es False"
    assert resultado is False, "El resultado no es el esperado"


def test_es_balanceado_llaves_false4():
    """
    Test con llaves colocados de forma variada
    """
    cadena = "{}{"
    resultado = es_balanceado(cadena)
    assert isinstance(resultado, bool), "El resultado esperado es False"
    assert resultado is False, "El resultado no es el esperado"


def test_es_balanceado_mixto_true1():
    """
    Test mixto
    """
    cadena = "[]{}()"
    resultado = es_balanceado(cadena)
    assert isinstance(resultado, bool), "El resultado esperado es True"
    assert resultado is True, "El resultado no es el esperado"


def test_es_balanceado_mixto_true2():
    """
    Test mixto
    """
    cadena = "[{}]()"
    resultado = es_balanceado(cadena)
    assert isinstance(resultado, bool), "El resultado esperado es True"
    assert resultado is True, "El resultado no es el esperado"


def test_es_balanceado_mixto_true3():
    """
    Test mixto
    """
    cadena = "[()]{}"
    resultado = es_balanceado(cadena)
    assert isinstance(resultado, bool), "El resultado esperado es True"
    assert resultado is True, "El resultado no es el esperado"


def test_es_balanceado_mixto_true4():
    """
    Test mixto
    """
    cadena = "([]){}"
    resultado = es_balanceado(cadena)
    assert isinstance(resultado, bool), "El resultado esperado es True"
    assert resultado is True, "El resultado no es el esperado"


def test_es_balanceado_mixto_true5():
    """
    Test mixto
    """
    cadena = "({})[]"
    resultado = es_balanceado(cadena)
    assert isinstance(resultado, bool), "El resultado esperado es True"
    assert resultado is True, "El resultado no es el esperado"


def test_es_balanceado_mixto_true6():
    """
    Test mixto
    """
    cadena = "{()}[]"
    resultado = es_balanceado(cadena)
    assert isinstance(resultado, bool), "El resultado esperado es True"
    assert resultado is True, "El resultado no es el esperado"


def test_es_balanceado_mixto_true7():
    """
    Test mixto
    """
    cadena = "{[]}()"
    resultado = es_balanceado(cadena)
    assert isinstance(resultado, bool), "El resultado esperado es True"
    assert resultado is True, "El resultado no es el esperado"


def test_es_balanceado_mixto_true8():
    """
    Test mixto
    """
    cadena = "[({})]"
    resultado = es_balanceado(cadena)
    assert isinstance(resultado, bool), "El resultado esperado es True"
    assert resultado is True, "El resultado no es el esperado"


def test_es_balanceado_mixto_true9():
    """
    Test mixto
    """
    cadena = "[{()}]"
    resultado = es_balanceado(cadena)
    assert isinstance(resultado, bool), "El resultado esperado es True"
    assert resultado is True, "El resultado no es el esperado"


def test_es_balanceado_mixto_true10():
    """
    Test mixto
    """
    cadena = "{[()]}"
    resultado = es_balanceado(cadena)
    assert isinstance(resultado, bool), "El resultado esperado es True"
    assert resultado is True, "El resultado no es el esperado"


def test_es_balanceado_mixto_true11():
    """
    Test mixto
    """
    cadena = "{([])}"
    resultado = es_balanceado(cadena)
    assert isinstance(resultado, bool), "El resultado esperado es True"
    assert resultado is True, "El resultado no es el esperado"


def test_es_balanceado_mixto_true12():
    """
    Test mixto
    """
    cadena = "([{}])"
    resultado = es_balanceado(cadena)
    assert isinstance(resultado, bool), "El resultado esperado es True"
    assert resultado is True, "El resultado no es el esperado"


def test_es_balanceado_mixto_true13():
    """
    Test mixto
    """
    cadena = "({[]})"
    resultado = es_balanceado(cadena)
    assert isinstance(resultado, bool), "El resultado esperado es True"
    assert resultado is True, "El resultado no es el esperado"


def test_es_balanceado_mixto_false_mequieromorir():
    """
    Test mixto
    """
    cadena = "[]({)(}"
    resultado = es_balanceado(cadena)
    assert isinstance(resultado, bool), "El resultado esperado es False"
    assert resultado is False, "El resultado no es el esperado"


def test_es_balanceado_mixto_false_estoyalpedo():
    """
    Test mixto
    """
    cadena = "({}}][)"
    resultado = es_balanceado(cadena)
    assert isinstance(resultado, bool), "El resultado esperado es False"
    assert resultado is False, "El resultado no es el esperado"

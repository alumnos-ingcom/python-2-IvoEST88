################
# Nombre - @IvoEST88
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
1. El Cifrado del Cesar (que grande cesar)
"""
# Implementar una funcion que codifique un texto rotandolo
# una cantidad de posiciones ajustable.
# Implementar la funcion que decodifique el texto rotado una
# cantidad de posiciones ajustable.


def codificar(texto, ajuste):
    """
    Funcion para codificar una frase
    """
    vueltas = 0
    long_texto = len(texto)
    letras_codificadas = []
    ajuste_orig = ajuste
    if ajuste == 0:
        resultado = "No seas malo, no pongas 0"
    else:
        while vueltas < long_texto:
            codificado = ord(texto[vueltas])
            if codificado >= 48 and codificado <= 122:
                minimo = 48
                maximo = 122
            else:
                print("Valor fuera de los limites establecidos")
            if ajuste < 0:
                while ajuste < 0:
                    if codificado < minimo:
                        codificado = minimo
                    codificado -= 1
                    ajuste += 1
            elif ajuste > 0:
                while ajuste > 0:
                    if codificado > maximo:
                        codificado = minimo
                    codificado += 1
                    ajuste -= 1
            codificado = chr(codificado)
            letras_codificadas.append(codificado)
            vueltas += 1
            ajuste = ajuste_orig
        resultado = letras_codificadas
    return resultado


def decodificar(resultado, ajuste):
    """
    Funcion para descodificar un texto
    """
    vuelta = 0
    lista = []
    ajuste = ajuste * -1
    minimo = 48
    maximo = 122
    ajuste_orig = ajuste
    long_por_descodificar = len(resultado)
    while vuelta < long_por_descodificar:
        valor = resultado[vuelta]
        descodificado = ord(valor)
        while ajuste != 0:
            if ajuste < 0:
                descodificado = descodificado - 1
                if descodificado < minimo:
                    descodificado = maximo
                ajuste += 1
            else:
                descodificado = descodificado + 1
                if descodificado > maximo:
                    descodificado = minimo
                ajuste -= 1
        ajuste = ajuste_orig
        descodificado = chr(descodificado)
        lista.append(descodificado)
        vuelta = vuelta + 1
    return lista


def principal():
    """
    Programa
    """
    texto = input("Ingrese la palabra o frase: ")
    print("¿Qué desea hacer con el texto ingresado?")
    print("1. Codificar.")
    print("2. Decodificar.")
    eleccion = int(input("Elección: "))
    ajuste = int(input("Cuantas posiciones desea ajustarlo?\n"))
    if eleccion == 1:
        resultado = codificar(texto, ajuste)
        print(f"El texto ingresado: {texto}\nSe convirtió a: {resultado}")
    elif eleccion == 2:
        resultado = codificar(texto, ajuste)
        resultado_decod = decodificar(resultado, ajuste)
        print(resultado_decod)
    else:
        print("Ingresaste un valor fuera del rango establecido")


if __name__ == "__main__":
    principal()

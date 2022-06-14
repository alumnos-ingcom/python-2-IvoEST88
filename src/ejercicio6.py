################
# Nombre - @IvoEST88
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
6. Cifrado Cesar (que grande Cesar)
"""

def codificar(texto, ajuste):
    ajuste_orig = ajuste
    letras_codificadas = []
    vueltas = 0
    vueltas_dec = 0
    letras_descod = []
    long_texto = len(texto)
    while vueltas < long_texto:
        codificado = ord(texto[vueltas])
        vueltas += 1
        while ajuste > 0:
            codificado += 1
            ajuste -=1
            if codificado < 48:
                codificado = 48
            elif codificado > 57 and codificado < 65:
                codificado = 65
            elif codificado > 90 and codificado < 97:
                codificado = 97
            elif codificado >122:
                codificado = 48
        letras_codificadas.append(codificado)
        ajuste = ajuste_orig
    while vueltas_dec < long_texto:
        descodif = chr(letras_codificadas[vueltas_dec])
        letras_descod.append(descodif)
        vueltas_dec += 1
    return letras_codificadas, letras_descod


def principal():
    texto = list(input("Ingresar mensaje: "))
    ajuste = int(input("Ingresar cantidad de posiciones a ajustar: "))
    resultado = codificar(texto, ajuste)[0]
    resultado_des = codificar(texto, ajuste)[1]
    
    print (f"{texto} + {ajuste} posiciones es igual a:\n{resultado}\nEsto al descodificar: {resultado_des}")
    
if __name__ == "__main__":
    principal()

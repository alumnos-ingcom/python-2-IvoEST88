################
# Nombre - @IvoEST88
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
3. Súper-puestos
"""
#Desarrollar una función que indique el grado de superposición entre dos listas.
#Siendo 0 sin superposición y uno para cada elemento superpuesto.
def superposicion(frase1, frase2):
    """
    Funcion que indica cuales letras se repiten en ambas frases
    """
    vueltas = 0
    vueltas2 = 0
    long_frase1 = len(frase1)
    long_frase2 = len(frase2)
    en_comun = 0
    if long_frase1 > long_frase2:
        frase_larga = long_frase1
    elif long_frase1 < long_frase2:
        frase_larga = long_frase2
    else:
        frase_larga = long_frase1
    while vueltas < frase_larga:
        while vueltas2 < long_frase2:
            vueltas1 = 0
            while vueltas1 < long_frase1:
                if frase1[vueltas1] == frase2[vueltas2]:
                    en_comun += 1
                vueltas1 += 1
            vueltas2 += 1
        vueltas += 1
    return en_comun


def principal():
    """
    Programa
    """
    frase1 = input("Ingrese la primera frase o palabra: ")
    frase2 = input("Ingrese la segunda frase o palabra: ")
    resultado_superposicion = superposicion(frase1, frase2)
    print(resultado_superposicion)


if __name__ == "__main__":
    principal()

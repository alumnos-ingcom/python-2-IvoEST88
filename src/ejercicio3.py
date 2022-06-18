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
    long_frase1 = len(frase1)
    long_frase2 = len(frase2)
    en_comun = 0
    if long_frase1 > long_frase2:
        frase_corta = long_frase2
    else:
        frase_corta = long_frase1
    while vueltas < frase_corta:
        if frase1[vueltas] == frase2[vueltas]:
            en_comun += 1
            vueltas += 1
        else:
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

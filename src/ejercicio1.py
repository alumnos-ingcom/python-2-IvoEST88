################
# Nombre - @IvoEST88
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def es_par(numero):
    if numero <0:
        numero *= -1
        signo = -1
    else:
        signo = 1
    while numero >0:
        numero -= 2
    if numero != 0:
        resultado = False
        numero *= signo
    else:
        resultado = True
        numero *= signo
    return resultado
def principal():
    numero = int(input("Ingrese un número: "))
    resultado_es_par = es_par(numero)
    if resultado_es_par == True:
        print (f"El número {numero} es Par")
    else:
        print (f"El número {numero} es Impar")
if __name__ == "__main__":
    principal()
            
################
# Nombre - @IvoEST88
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
5. Corchetes balanceados
"""
#Implementar una función que determine si una cadena con corchetes
#está balanceada.
def corchetes_balanceados(corchetes):
    abierto = "["
    contador_abierto = 0
    cerrado = "]"
    contador_cerrado = 0
    vueltas = 0
    long_corchetes = len(corchetes)
    while vueltas < long_corchetes:
        if corchetes[vueltas] == abierto:
            contador_abierto += 1
        elif corchetes[vueltas] == cerrado:
            contador_cerrado += 1
        vueltas += 1
    if contador_abierto == 0 or contador_cerrado == 0:
        resultado = False
    else:
        if contador_abierto == contador_cerrado:
            resultado = True
        else:
            resultado = False
    return resultado

def parentesis_balanceados(parentesis):
    abierto = "("
    contador_abierto = 0
    cerrado = ")"
    contador_cerrado = 0
    vueltas = 0
    long_parentesis = len(parentesis)
    while vueltas < long_parentesis:
        if parentesis[vueltas] == abierto:
            contador_abierto += 1
        elif parentesis[vueltas] == cerrado:
            contador_cerrado += 1
        vueltas += 1
    if contador_abierto == 0 or contador_cerrado == 0:
        resultado = False
    else:
        if contador_abierto == contador_cerrado:
            resultado = True
        else:
            resultado = False
    return resultado

def llaves_balanceadas(llaves):
    abierto = "{"
    contador_abierto = 0
    cerrado = "}"
    contador_cerrado = 0
    vueltas = 0
    long_llaves = len(llaves)
    while vueltas < long_llaves:
        if llaves[vueltas] == abierto:
            contador_abierto += 1
        elif llaves[vueltas] == cerrado:
            contador_cerrado += 1
        vueltas += 1
    if contador_abierto == 0 or contador_cerrado == 0:
        resultado = False
    else:
        if contador_abierto == contador_cerrado:
            resultado = True
        else:
            resultado = False
    return resultado
def mixto_balanceado(mixto):
    abierto = ["{", "[", "("]
    long_abierto = len(abierto)
    contador_abierto = 0
    cerrado = ["}", "]", ")"]
    long_cerrado = len(cerrado)
    contador_cerrado = 0
    vueltas = 0
    long_mixto = len(mixto)
    while vueltas < long_mixto:
        abierto_vueltas = 0
        cerrado_vueltas = 0
        while abierto_vueltas < long_abierto:
            if mixto[vueltas] == abierto[abierto_vueltas]:
                contador_abierto += 1
                abierto_vueltas += 1
            else:
                abierto_vueltas += 1
        while cerrado_vueltas < long_cerrado:
            if mixto[vueltas] == cerrado[cerrado_vueltas]:
                contador_cerrado += 1
                cerrado_vueltas += 1
            else:
                cerrado_vueltas += 1
        vueltas += 1
    if contador_abierto == 0 or contador_cerrado == 0:
        resultado = False
    else:
        if contador_abierto == contador_cerrado:
            resultado = True
        else:
            resultado = False
    return resultado


def principal():
    print("¿Qué desea verificar?\n1. Corchetes.\n2. Paréntesis.\n3. Llaves.\n4. Mixto")
    eleccion = int(input("Ingrese su elección: "))
    if eleccion == 1:
        corchetes = input("Corchetes ---> ")
        print(corchetes_balanceados(corchetes))
    elif eleccion == 2:
        parentesis = input("Paréntesis ---> ")
        print(parentesis_balanceados(parentesis))
    elif eleccion == 3:
        llaves = input("Llaves ---> ")
        print(llaves_balanceadas(llaves))
    elif eleccion == 4:
        mixto = input("Ingrese los carácteres ---> ")
        print(mixto_balanceado(mixto))
        
if __name__ == "__main__":
    principal()
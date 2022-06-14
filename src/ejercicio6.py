################
# Nombre - @IvoEST88
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
6. Cifrado Cesar (que grande Cesar)
"""
def codificar(texto):
    ajuste = int(input("¿Cuántas posiciones desea ajustar?: "))
    ajuste_orig = ajuste
    letras_codificadas = []
    vueltas = 0
    long_texto = len(texto)
    if ajuste == 0:
        resultado = "No seas malo, no pongas 0"
    else:
        while vueltas < long_texto:
            codificado = ord(texto[vueltas])
            if codificado > 48 and codificado < 57:
                minimo = 48
                maximo = 57
            elif codificado > 65 and codificado < 90:
                minimo = 65
                maximo = 90
            elif codificado > 97 and codificado < 122:
                minimo = 97
                maximo = 122
            else:
                print ("para capo, ingresaste algo fuera de los limites establecidos")
            if ajuste < 0:
                while ajuste < 0:
                    if codificado < minimo:
                        codificado = minimo
                    elif codificado > maximo:
                        codificado = minimo
                    codificado -= 1
                    ajuste += 1
            elif ajuste > 0:
                while ajuste > 0:
                    if codificado < minimo:
                        codificado = minimo
                    elif codificado > maximo:
                        codificado = minimo
                    codificado += 1
                    ajuste -= 1
            letras_codificadas.append(codificado)
            vueltas += 1
            ajuste = ajuste_orig
        resultado = letras_codificadas
    return resultado
def descodificador(codificados):
    lista_codificados = []
    lista_descodificados = []
    while codificados > 0:
        print(" Los valores deben estar entre '48-57, 65-90 y 97-122'") 
        num_cod = int(input("Ingrese valores uno por uno: "))
        if num_cod > 48 and num_cod < 57:
            lista_codificados.append(num_cod)
        elif num_cod > 65 and num_cod < 90:
            lista_codificados.append(num_cod)
        elif num_cod >97 and num_cod < 122:
            lista_codificados.append(num_cod)
        else:
            print("Oye tranquilo viejo, estas ingresando valores fueras de los limites establecidos")
            num_cod = int(input("Ingrese valores uno por uno: "))
        codificados -= 1
        long_lista_cod = len(lista_codificados)
    ajuste = int(input("¿Cuántas posiciones desea ajustar?: "))
    ajuste_orig = ajuste
    vuelta = 0
    while long_lista_cod > 0:
        while vuelta < long_lista_cod:
            if ajuste > 0: 
                while ajuste > 0: 
                    ajustado = lista_codificados[vuelta] + 1
                    lista_codificados[vuelta] = ajustado
                    ajuste -= 1
            else:
                while ajuste < 0:
                    ajustado = lista_codificados[vuelta] - 1
                    lista_codificados[vuelta] = ajustado
                    ajuste += 1
            ajuste = ajuste_orig
            vuelta += 1
            lista_descodificados.append(ajustado)
        long_lista_cod -= 1
    return lista_descodificados
            
            

def principal():
    empezar = True
    while empezar is True:
        print("Elija una de las opciones:\n1.Codificar\n2.Descodificar.\n3.Salir")
        eleccion = int(input("Elección: "))
        if eleccion == 1:
            texto = input("Ingrese los caracteres: ")
            resultado = codificar(texto)
            print(resultado)
        elif eleccion == 2:
            codificados = int(input("cantidad de valores a decodificar: "))
            resultado2 = descodificador(codificados)
            print(resultado2)
        elif eleccion == 3:
            empezar = False
        else:
            print("Valor fuera del rango establecido")
            empezar = False
    
if __name__ == "__main__":
    principal()

import sys
from ensamblador import ensambladorabinario
from datos import instrucciones, tipoR, tipoI, tipoJ, registros

def principal():
    g = "10008000"  # Dirección del gp en hexadecimal
    gp = int(g, 16)  # Convierte gp a entero
    s = "7ffffffc"  # Dirección del sp en hexadecimal
    sp = int(s, 16)  # Convierte sp a entero
    pc = 0  # Contador del programa inicializado a 0
    memini = "0x00400000"  # Dirección inicial de memoria en hexadecimal
    instrucciones_lista = []  # Lista para almacenar las instrucciones
    ramas = {}  # Diccionario para almacenar etiquetas y sus direcciones
    lista_temporal = []  # Lista temporal para datos intermedios

    # Lee las instrucciones desde la entrada estándar
    for partes in sys.stdin:
        partes = partes.strip().split()  # Elimina espacios en blanco y divide la línea en partes
        if not partes:  # Si la línea está vacía, rompe el bucle
            break
        for x in range(len(partes) - 1):  # Itera sobre las partes de la línea
            if x != 0:
                partes[x] = partes[x][:-1]  # Elimina el último carácter de cada parte
        instrucciones_lista.append(partes)  # Añade las partes a la lista de instrucciones

    # Procesa las instrucciones
    for j in range(len(instrucciones_lista)):
        if instrucciones_lista[j][0][-1] == ":":  # Si la instrucción es una etiqueta
            lista_temporal.append(memini)  # Añade la dirección de memoria a la lista temporal
            lista_temporal.append(pc)  # Añade el contador de programa a la lista temporal
            cad = instrucciones_lista[j][0][:-1]  # Elimina el ':' de la etiqueta
            ramas[cad] = lista_temporal  # Añade la etiqueta y la lista temporal al diccionario de ramas
            lista_temporal = []  # Resetea la lista temporal
            memini = int(memini, 16)  # Convierte la dirección de memoria a entero
            memini = memini - 4  # Resta 4 a la dirección de memoria
            memini = hex(memini)  # Convierte la dirección de memoria de nuevo a hexadecimal
            memini = str(memini)  # Convierte la dirección de memoria a cadena
        elif instrucciones_lista[j][0] != 'j' or instrucciones_lista[j][0] != 'jal':  # Si la instrucción no es 'j' o 'jal'
            pc += 4  # Incrementa el contador de programa en 4
        memini = int(memini, 16)  # Convierte la dirección de memoria a entero
        memini = memini + 4  # Suma 4 a la dirección de memoria
        memini = hex(memini)  # Convierte la dirección de memoria de nuevo a hexadecimal
    
    #procesamiento de funciones asm
    
    for i in range(len(instrucciones_lista)):
        if len(instrucciones_lista[i]) == 1:
            pass
        elif instrucciones_lista[i][0] == "beq" or instrucciones_lista[i][0] == "bne":
            rama = ramas[instrucciones_lista[i][3]]
            codigo_binario = ensambladorabinario(instrucciones_lista[i], instrucciones, registros, tipoR, tipoI, tipoJ, rama, gp, sp)
            print(codigo_binario)
        elif instrucciones_lista[i][0] in tipoR or instrucciones_lista[i][0] in tipoI or instrucciones_lista[i][0] in tipoJ:
            codigo_binario = ensambladorabinario(instrucciones_lista[i], instrucciones, registros, tipoR, tipoI, tipoJ, ramas, gp, sp)
            if codigo_binario:
                print(codigo_binario)
            else:
                print("Instrucción no válida o no soportada.")
        else:
            print("Instrucción no válida.")

if __name__ == "__main__":
    principal()
import sys
from ensamblador import ensambladorabinario
from datos import instrucciones, tipoR, tipoI, tipoJ, registros

def principal():
    g = "10008000"
    gp = int(g, 16)
    s = "7ffffffc"
    sp = int(s, 16)
    pc = 0
    memini = "0x00400000"
    instrucciones_lista = []
    ramas = {}
    lista_temporal = []
    for partes in sys.stdin:
        partes = partes.strip().split()
        if not partes:
            break
        for x in range(len(partes) - 1):
            if x != 0:
                partes[x] = partes[x][:-1]
        instrucciones_lista.append(partes)
    for j in range(len(instrucciones_lista)):
        if instrucciones_lista[j][0][-1] == ":":
            lista_temporal.append(memini)
            lista_temporal.append(pc)
            cad = instrucciones_lista[j][0][:-1]
            ramas[cad] = lista_temporal
            lista_temporal = []
            memini = int(memini, 16)
            memini = memini - 4
            memini = hex(memini)
            memini = str(memini)
        elif instrucciones_lista[j][0] != 'j' or instrucciones_lista[j][0] != 'jal':
            pc += 4
        memini = int(memini, 16)
        memini = memini + 4
        memini = hex(memini)
        memini = str(memini)
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
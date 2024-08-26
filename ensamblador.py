def ensambladorabinario(partes, instrucciones, registros, tipoR, tipoI, tipoJ, rama, gp, sp):
    if partes[0] in instrucciones:
        instruccion = instrucciones[partes[0]]
        if partes[0] in tipoR:
            if partes[1] == '$gp' or partes[1] == '$sp' or partes[1] == '$0' or partes[1] == '$zero':
                return False
            elif len(partes) == 4 and partes[0] == 'sll' or partes[0] == 'srl' or partes[0] == 'sra':
                print("D")
                if partes[3][0] == '0' and partes[3][1] == 'x':
                    num = bin(int(partes[3], 16))[2:]
                    a = num[-5:].zfill(5)
                else:
                    num = bin(int(partes[3]))[2:]
                    a = num[-5:].zfill(5)
                instruccion[3] = registros[partes[1]]
                instruccion[2] = registros[partes[2]]
                instruccion[4] = a
            elif len(partes) == 4:
                instruccion[1] = registros[partes[2]]
                instruccion[2] = registros[partes[3]]
                instruccion[3] = registros[partes[1]]
            elif len(partes) == 3:
                instruccion[1] = registros[partes[1]]
                instruccion[2] = registros[partes[2]]
            elif len(partes) == 2:
                instruccion[3] = registros[partes[1]]
            else:
                return False

        elif partes[0] in tipoI:
            if partes[1] == '$gp' or partes[1] == '$sp' or partes[1] == '$0' or partes[1] == '$zero':
                return False
            elif len(partes) == 4:
                if partes[0] == "beq" or partes[0] == "bne":
                    etiqueta = (int(rama[0], 16))
                    etiqueta = rama[1] + 4 + etiqueta
                    etiqueta = etiqueta * 4
                    instruccion[1] = registros[partes[1]]
                    instruccion[2] = registros[partes[2]]
                    if len(bin(etiqueta)) > 16:
                        instruccion[3] = bin(etiqueta)[-16:]
                    else:
                        instruccion[3] = bin(etiqueta)[2:].zfill(16)

                elif partes[3][-1] != ')' or partes[3][1] != 'x':
                    if partes[0] == "andi":
                        if partes[3][0] == '0' and partes[3][1] == 'x':
                            entero = int(partes[3], 16)
                        else:
                            entero = int(partes[3])
                        instruccion[2] = registros[partes[2]]
                        instruccion[1] = registros[partes[1]]
                        instruccion[3] = bin(entero)[2:].zfill(16)

                    else:
                        if partes[3][0] == '0' and partes[3][1] == 'x':
                            entero = int(partes[3], 16)
                        else:
                            entero = int(partes[3])
                        instruccion[2] = registros[partes[1]]
                        instruccion[1] = registros[partes[2]]
                        instruccion[3] = bin(entero)[2:].zfill(16)

                else:
                    entero = int(partes[3])
                    instruccion[2] = registros[partes[2]]
                    instruccion[1] = registros[partes[1]]
                    instruccion[3] = bin(entero)[2:].zfill(16)

            elif len(partes) == 3:
                if partes[2][-1] == ')':
                    instruccion[2] = registros[partes[1]]
                    i = 0
                    bandera = False
                    entero = ""
                    while i < len(partes[2]) and bandera == False:
                        if partes[2][i] != '(':
                            entero += partes[2][i]
                            i += 1
                        else:
                            bandera = True
                    bandera = False
                    x = ""
                    i = i + 1
                    while i < len(partes[2]) and bandera == False:
                        if partes[2][i] != ')':
                            x += partes[2][i]
                        else:
                            bandera = True
                        i += 1
                    instruccion[1] = registros[x]
                    c = int(entero)
                    instruccion[3] = bin(c)[2:].zfill(16)
                elif partes[2][1] == 'x':
                    instruccion[2] = registros[partes[1]]
                    entero = int(partes[2], 16)
                    instruccion[3] = bin(entero)[2:].zfill(16)
                else:
                    instruccion[2] = registros[partes[1]]
                    entero = int(partes[2])
                    instruccion[3] = bin(entero)[2:].zfill(16)

            else:
                return False
        elif partes[0] in tipoJ:
            if len(partes) == 2:
                if partes[1][1] != "x" and partes[1][0] != "0":
                    entero = (int(rama[partes[1]][0], 16)) / 4
                    instruccion[1] = bin(entero)[2:].zfill(26)
                else:
                    entero = (int(partes[1], 16)) / 4
                    instruccion[1] = bin(entero)[2:].zfill(26)
            else:
                return False
        else:
            return False

        if partes[0] in tipoR:
            codigo_binario = instruccion[0] + instruccion[1] + instruccion[2] + instruccion[3] + instruccion[4] + instruccion[5]

        elif partes[0] in tipoI:
            codigo_binario = instruccion[0] + instruccion[1] + instruccion[2] + instruccion[3]
        elif partes[0] in tipoJ:
            codigo_binario = instruccion[0] + instruccion[1]
        return codigo_binario
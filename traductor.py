import sys

def assemblertobinary(parts, instructions, registers, tipoR, tipoI, tipoJ,branch, gp, sp):
    if parts[0] in instructions:
        instruction = instructions[parts[0]]
        if parts[0] in tipoR:
            if parts[1] == '$gp' or parts[1] == '$sp' or parts[1] == '$0' or parts[1] == '$zero':
                return False
            elif len(parts) == 4  and parts[0] == 'sll' or parts[0] == 'srl' or parts[0] == 'sra':
                print("D")
                if parts[3][0] == '0' and parts[3][1] == 'x':
                    num = bin(int(parts[3],16))[2:]
                    a = num[-5:].zfill(5)
                else:
                    num = bin(int(parts[3]))[2:]
                    a = num[-5:].zfill(5)
                instruction[3] = registers[parts[1]]
                instruction[2] = registers[parts[2]]
                instruction[4] = a
            elif len(parts) == 4:
                instruction[1] = registers[parts[2]]
                instruction[2] = registers[parts[3]]
                instruction[3] = registers[parts[1]]
            elif len(parts) == 3:
                instruction[1] = registers[parts[1]]
                instruction[2] = registers[parts[2]]
            elif len(parts) == 2:    
                instruction[3] = registers[parts[1]]        
            else:
                return False
        
        elif parts[0] in tipoI:
            if parts[1] == '$gp' or parts[1] == '$sp' or parts[1] == '$0' or parts[1] == '$zero':
                return False
            elif len(parts) == 4:
                if parts[0] == "beq" or parts[0] == "bne":
                        label = (int(branch[0],16))
                        label = branch[1] + 4 + label
                        label = label * 4
                        instruction[1] = registers[parts[1]]
                        instruction[2] = registers[parts[2]]
                        if len(bin(label)) > 16:
                            instruction[3] = bin(label)[-16:]
                        else:   
                            instruction[3] = bin(label)[2:].zfill(16)

                elif parts[3][-1] !=')' or parts[3][1] != 'x':
                    if parts[0] == "andi":
                        if parts[3][0] == '0' and parts[3][1] == 'x':
                            entero = int(parts[3],16)
                        else:
                            entero = int(parts[3])
                        instruction[2] = registers[parts[2]]
                        instruction[1] = registers[parts[1]] 
                        instruction[3] = bin(entero)[2:].zfill(16)
                        
                    else:
                        if parts[3][0] == '0' and parts[3][1] == 'x':
                            entero = int(parts[3],16)
                        else:
                            entero = int(parts[3])
                        instruction[2] = registers[parts[1]]
                        instruction[1] = registers[parts[2]]
                        instruction[3] = bin(entero)[2:].zfill(16)
                
                else:
                    entero = int(parts[3])
                    instruction[2] = registers[parts[2]]
                    instruction[1] = registers[parts[1]]
                    instruction[3] = bin(entero)[2:].zfill(16)

            elif len(parts) == 3:
                if parts[2][-1] == ')':
                    instruction[2] = registers[parts[1]]
                    i = 0
                    flag = False
                    entero = ""
                    while i < len(parts[2]) and flag == False:
                        if parts[2][i] != '(':
                            entero += parts[2][i]
                            i+=1
                        else:
                            flag = True
                    flag = False
                    x = ""
                    i = i+1
                    while i < len(parts[2]) and flag == False:
                        if parts[2][i] != ')':
                            x += parts[2][i]
                        else:
                            flag = True
                        i+=1
                    instruction[1] = registers[x]
                    c = int(entero)
                    instruction[3] = bin(c)[2:].zfill(16)
                elif parts[2][1] == 'x':
                    instruction[2] = registers[parts[1]]
                    entero = int(parts[2], 16)
                    instruction[3] = bin(entero)[2:].zfill(16) 
                else:
                    instruction[2] = registers[parts[1]]
                    entero = int(parts[2])
                    instruction[3] = bin(entero)[2:].zfill(16)
                    
            else:
                return False
        elif parts[0] in tipoJ:
            if len(parts) == 2:
                if parts[1][1] != "x" and parts[1][0] != "0":
                    entero = (int(branch[parts[1]][0], 16))/4
                    instruction[1] = bin(entero)[2:].zfill(26)
                else:
                    entero = (int(parts[1], 16))/4
                    instruction[1] = bin(entero)[2:].zfill(26)
            else:
                return False
        else:
            return False
        
        if parts[0] in tipoR:
            binary_code = instruction[0] + instruction[1] + instruction[2] + instruction[3] + instruction[4] + instruction[5]

        elif parts[0] in tipoI: 
            binary_code = instruction[0] + instruction[1] + instruction[2] + instruction[3]
        elif parts[0] in tipoJ:
            binary_code = instruction[0] + instruction[1]
        return binary_code

def main():
    instructions = {
        'add': ['000000', '', '', '', '00000', '100000'],
        'sub': ['000000', '', '', '', '00000', '100010'],
        'and': ['000000', '', '', '', '00000', '100100'],
        'or': ['000000', '', '', '', '00000', '100101'],
        'xor': ['000000', '', '', '', '00000', '100110'],
        'nor': ['000000', '', '', '', '00000', '100111'],
        'slt': ['000000', '', '', '', '00000', '101010'],
        'jr': ['000000', '', '', '', '000000000000000', '001000'],
        'div': ['000000', '', '', '00000', '00000', '011010'],
        'divu': ['000000', '', '', '00000', '00000', '011011'],
        'mult': ['000000', '', '','00000', '00000',  '011000'],
        'mfhi': ['000000', '00000', '00000', '','00000',  '010000'],
        'mflo': ['000000', '00000', '00000', '','00000',  '010010'],    
        'multu': ['000000', '', '', '00000','00000' ,'011001'],
        'lw': ['100011', '', '', ''],
        'sw': ['101011', '', '', ''],
        'addi': ['001000', '', '', ''],
        'beq': ['000100', '', '', ''],
        'bne': ['000101', '', '', ''],
        'andi': ['001100', '', '', ''],
        'ori': ['001101', '', '', ''],
        'xori': ['001110', '', '', ''],
        'lb': ['100000', '', '', ''],
        'sb': ['101000', '', '', ''],
        'lh': ['100001', '', '', ''],
        'sh': ['101001', '', '', ''],
        'subi': ['001001', '', '', ''],
        'slti': ['001010', '', '', ''],
        'sll': ['000000', '00000', '', '', '', '000000'],
        'srl': ['000000', '00000', '', '', '', '000010'],
        'sra': ['000000', '00000', '', '', '', '000011'],
        'lui': ['001111', '00000', '', ''],
        'sltiu': ['001011', '', '', ''],
        '$gp': ['10008000'],

        'j': ['000010', ''],
        'jal': ['000011', '']
    }

    tipoR = ["add", "sub", "and", "or", "xor", "nor", "slt", "jr", "div", "divu", "sll", "srl", "sra", "mult", "mfhi", "mflo", "multu"]
    tipoI = ["lw", "sw", "lb", "sb", "lh", "sh", "addi", "subi", "andi",
             "ori", "xori", "slti", "beq", "bne", "lui", "sltiu"]
    tipoJ = ["j", "jal"]
    registers = {'$0': '00000','$zero': '00000','$at': '00001','$v0': '00010','$v1': '00011','$a0': '00100','$a1': '00101',
        '$a2': '00110','$a3': '00111','$t0': '01000','$t1': '01001','$t2': '01010','$t3': '01011','$t4': '01100',
        '$t5': '01101','$t6': '01110','$t7': '01111','$0': '00000','$s0': '10000','$s1': '10001','$s2':
'10010','$s3': '10011',
        '$s4': '10100','$s5': '10101','$s6': '10110','$s7': '10111','$t8': '11000','$t9': '11001','$k0': '11010',
        '$k1': '11011','$gp': '11100','$sp': '11101','$fp': '11110','$ra': '11111'
    }
    g = "10008000"
    gp = int(g,16)
    s = "7ffffffc"
    sp = int(s,16)
    pc = 0
    memini = "0x00400000"
    instruct = []
    branchs = {}
    listica = []
    for parts in sys.stdin:
        parts = parts.strip().split()
        if not parts:
            break
        for x in range(len(parts)-1):
            if x != 0:
                parts[x] = parts[x][:-1]
        instruct.append(parts)
    for j in range(len(instruct)):
        if instruct[j][0][-1] == ":":
            listica.append(memini)
            listica.append(pc)
            cad = instruct[j][0][:-1]
            branchs[cad] = listica
            listica = [] 
            memini = int(memini, 16)
            memini = memini - 4
            memini = hex(memini)
            memini = str(memini)
        elif instruct[j][0] != 'j' or instruct[j][0] != 'jal':
            pc += 4
        memini = int(memini, 16)
        memini = memini + 4
        memini = hex(memini)
        memini = str(memini)
    for i in range(len(instruct)):
        if len(instruct[i]) == 1:
            pass
        elif instruct[i][0] == "beq" or instruct[i][0] == "bne":
            branch = branchs[instruct[i][3]] 
            binarycode = assemblertobinary(instruct[i], instructions, registers, tipoR, tipoI, tipoJ,branch, gp, sp)
            print(binarycode)
        elif instruct[i][0] in tipoR or instruct[i][0] in tipoI or instruct[i][0] in tipoJ:
            binarycode = assemblertobinary(instruct[i], instructions, registers, tipoR, tipoI, tipoJ,branchs, gp, sp)
            if binarycode:
                print(binarycode)
            else:
                print("Instrucción no válida o no soportada.")  
        else:
            print("Instrucción no válida.")

main()
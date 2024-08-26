# Traductor de Lenguaje ensamblador a binario

## Creado Por 
#### 26/08/2024 <br> <br>Sergio Ponce <br> Felipe Moncada
---
## Modo de uso
Se debe ingresar un archivo .txt de la siguiente manera:
`python3 main.py <archivo.txt> salida.out`

El archivo de entrada debe estar en el siguiente formato:<br>
* Cada instruccion debe tener un espacio de separación entre cada palabra así: `beq $t1, $t2, etiqueta`
* Al nombrar una etiqueta hay que declararla con dos puntos en una linea solo con esa instrucción: <br>`add $t1, $t2, $t3`<br>
`sub $t4, $t5, $t6`<br>
`beq $t1, $t2, etiqueta`<br>
`etiqueta:` <br>`lw $t1, 0($t2)`

* La carpeta entregada incluye un archivo in.txt y un archivo exit.out de ejemplo que se puede probar con el siguiente comando: `python3 main.py <in.txt> salida.out` <br> el nombre de la salida debe ser diferente al original para compararlo.
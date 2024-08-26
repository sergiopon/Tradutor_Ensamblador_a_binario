# Ensamblador a Binario

Este proyecto es un ensamblador que convierte instrucciones en lenguaje ensamblador a código binario. Está dividido en varios archivos para una mejor organización y modularidad.

## Estructura del Proyecto

El proyecto está dividido en los siguientes archivos:

- `ensamblador.py`: Contiene la función `ensambladorabinario` que realiza la conversión de instrucciones a código binario.
- `datos.py`: Contiene los datos de instrucciones, tipos de instrucciones y registros.
- `principal.py`: Contiene la función `principal` que maneja la entrada y salida del programa y coordina la conversión de instrucciones.

## Archivos

### ensamblador.py

Este archivo contiene la función `ensambladorabinario` que toma una lista de partes de una instrucción y la convierte en código binario basado en las instrucciones y registros definidos.

### datos.py

Este archivo contiene los datos necesarios para la conversión, incluyendo:

- `instrucciones`: Un diccionario que mapea las instrucciones a sus representaciones binarias.
- `tipoR`, `tipoI`, `tipoJ`: Listas que categorizan las instrucciones en diferentes tipos.
- `registros`: Un diccionario que mapea los registros a sus representaciones binarias.

### principal.py

Este archivo contiene la función `principal` que:

1. Lee las instrucciones desde la entrada estándar.
2. Procesa las etiquetas y calcula las direcciones de memoria.
3. Convierte cada instrucción a código binario utilizando la función `ensambladorabinario`.
4. Imprime el código binario resultante.

## Ejecución

Para ejecutar el programa, asegúrate de tener todos los archivos en el mismo directorio y ejecuta el archivo `principal.py`:


python principal.py

El programa leerá las instrucciones desde la entrada estándar, las procesará y imprimirá el código binario correspondiente.

Ejemplo de Uso
Supongamos que tienes el siguiente conjunto de instrucciones en un archivo llamado instrucciones.txt:

add $t1, $t2, $t3
sub $t4, $t5, $t6
beq $t1, $t2, etiqueta
etiqueta: lw $t1, 0($t2)

Puedes ejecutar el programa y pasarle el archivo de instrucciones de la siguiente manera:

python principal.py < instrucciones.txt
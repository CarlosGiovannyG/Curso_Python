"""
PAQUETE: es un directorio (carpeta) donde se almacenan módulos relacionados entre si.

PARA QUE SIRVEN?: sirven para organizar mejor el código y poder reutilizarlo mejor.
        (MODULACIÓN Y REUTILIZACIÓN.)
        De esta manera podemos hacer el código mas sostenible y podemos reutilizar y
        estará mas organizado
COMO SE CREA UN PAQUETE: Crear una carpeta o directorio con un archivo llamado
        __init__.py .Este lo que hace es convertir un directorio en un módulo
        (paquete) que contiene otros módulos, y esto lo hace para pode importarlos
"""
"""Para poder hacer uso de un modulo primero lo debemos importar con la 
        palabra reservada FROM seguido del nombre del paquete (carpeta) seguido de
        un punto y dando el nombre del archivo, seguido de la palabra reservada 
        IMPORT y por ultimo la función a usar.
        Con el * asterisco podemos importar todo de este archivo; cabe resaltar que si el archivo 
        es demasiado grande esto ocupará demasiado espacio de MEMORIA RAM"""

from Paquete_1.funciones_cadena import contar_letras
from Paquete_1.funciones_numericas import *

print(multiplicar(5, 6))
print(potenciar(5, 6))
print(contar_letras("Carlos Giovanny"))

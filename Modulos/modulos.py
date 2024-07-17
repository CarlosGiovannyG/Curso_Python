"""
MODULO: es un archivo con exención  .py o .pyc (PYTHON COMPILADO), es un modulo que posee
        su propio espacio de nombres osea que contiene su propio contexto; el
        cual puede contener variables, funciones,clases o incluso otros módulos
PARA QUE SIRVEN?: sirven para organizar mejor el código y poder reutilizarlo mejor.
        Lo anterior viene ligado a dos principios que son: LA MODULACIÓN Y REUTILIZACIÓN.
        De esta manera podemos hacer el código mas mantenible y podemos reutilizar y
        estará mas organizado
"""
"""Para poder hacer uso de un modulo primero lo debemos importar con la palabra reservada IMPORT
    ademas al usarla debemos nombrar el archivo donde se encuentra y a traves de un punto
    nombramos la función o clase que vamos a usar"""

import Funciones_matematicas

print(Funciones_matematicas.sumar(5, 6))
print(Funciones_matematicas.multiplicar(5, 6))
print(" ")
print(" ")

"""Para hacerlo mas simple usamos la palabra reservada FROM e indicamos 
    la ruta (carpeta.carpeta2.archivo IMPORT) donde se encuentra el archivo 
    que vamos a usar y luego la palabra IMPORT y luego la función o clase a usar"""

from curso.Modulos.Funciones_matematicas import sumar,multiplicar

print(sumar(5, 6))
print(multiplicar(5, 6))
print(" ")
print(" ")
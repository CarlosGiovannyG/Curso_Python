""" Es una estructura de datos propia de python que permite almacenar distinto
    tipo de datos; no cambia una vez inicializada porque son inmutables
    La función COUNT funciona igual que en una lista contando cuantas veces se 
    repite un caracter dentro de la TUPLA basta nombrar el elemento dentro del elemento
    parentesis.
    La función INDEX nos da posición que ocupa un elemento dentro de una tupla basta contando
    nombrar el elemento dentro del parentesis
    la función MAX cuando la TUPLA es númerica nos da el maximo
    La función MIN nos dará el minimo
    El metdo TUPLE nos sirve para convertir una variable en tupla basta con nombrar la variables
    dentro del parentesis
"""
tupla = (1,2,3)
print(tupla)
print(" ")
print(" ")
"""En una tupla podemos almacenar cualquier tipo de dato"""
tupla2 = (7, "Carlos", True, 450.1,16+7j)
print(tupla2)
print(" ")
print(" ")
"""si queremos acceder a cualquier dato de una tupla solo basta con agregar la 
posicion de este entre las CORCHETES"""
print(tupla2[2])
print(" ")
print(" ")
"""Podemos tener una tupla dentro de otra tupla basta con generar nuevos parentesis"""
tupla3 = (9,3,(4,5,6))
print(tupla3)
print(" ")
print(" ")
""" Para acceder a una parte de la TUPLA cotamos con la función SLICE la cual nos da 
    la versatilidad de accerder a una parte de la TUPLA, solo basta con fijar las 
    posiciones dentro del [0:0:0] así
    [:0] desde el inicio hasta cierta posición
    [0:0] desde cierta posición hasta cierta posición
    [: :-1] comienza de atras hacia adelante
    [0:0] dando la misma posición no incluira el caracter
"""
"""PARA ACCEDER AL ULTIMO ELEMENTO DE UNA TUPLA PONEMOS DENTRO DE LAS LLAVES -1"""
print(tupla2[-1])
print(" ")
print(" ")
"""Tambien podemos acceder a varios elementoas de una tupla indicando desde
la posicion que inicia dos puntos y la posicion que termina"""
print(tupla2[0:3])
print(" ")
print(" ")
"""Para acceder al penultimo elemento de una tupla se hace con el -2"""
print(tupla2[-2])
print(" ")
print(" ")
"""Podemos generar variables para asignarles los elementos de una tupla, y
se comportarian como variable en adelante"""
a,b,c = tupla
print(a)
print(b)
print(c)
print(" ")
print(" ")
"""Podemos generar una nueva tupla para concatenar dos tuplas anteriores"""
tuplaFinal = tupla + tupla3
print(tuplaFinal, "Final")
print(" ")
print(" ")
"""Con esta funcion .count podemos contar las veces que esta un elemento
dentro de una tupla"""
print(tuplaFinal.count(3))
print(" ")
print(" ")
"""Con esta funcion .index sabemos en que posicion se encuentra un elemento dentro
de una tupla"""
print(tuplaFinal.index(9))
print(" ")
print(" ")
"""Si queremnos repetir el contenido de una TUPLA lo podemos hacer asignando un signo *"""
tuplaFinal1 = tuplaFinal * 2
print(tuplaFinal1)
print(" ")
print(" ")
print(tuplaFinal * 2)
print(" ")
print(" ")
"""Tambien podemos usar un FOR  para asignar los valores que queramos a unas variable, de esta
    manera podemos decidir que valores asignarle a cada variable
"""
tupla5 = (11, 9, -2, 3, 8, 5)
var1, var2, var3 = (tupla5[i] for i in (1, 3, 5))
print("var1 =", var1, ", var2 =", var2, ", var3 =", var3)
print(" ")
print(" ")

"""podemos definir una función para calcular variaos valores dentro de una tuplaFinal
"""

def minmax(a, b): 
    if a < b: 
        return a, b
    else:
        return b, a 

x, y = minmax(5,13)
print ('min =', x, ",", 'max =', y)
x, y = minmax(12, -4)
print ('min =', x, ",", 'max =', y)
print(" ")
print(" ")




"""
1. recibir datos pr1 == pr2 === operacion
2. crear los contadores 

"""
newTupla = tuple([1,2,3])
print(newTupla)
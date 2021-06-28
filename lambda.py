""" La función LAMBDA es una función anonima que sirve para abreviar o resumir 
    una función normal para convertirla en una expresión simple.
    Toda función LAMBDA se puede convertir en una función normal, no viceversa
    Tambien podemos guardar el valor de la función LAMBDA en una variable como 
    se hace con una función normal.
            SINTAXIS = LAMBDA RECIBE PARAMETROS : RETORNO
    
"""

def suma (n1, n2):
    return n1 + n2

print(end = ' \n ')
print(suma(12, 15))
print(end = ' \n ')

sumar = lambda n1, n2 : n1 + n2
print(sumar(12, 15))
print(end = ' \n ')

sumar1 = sumar(12,15)
print(sumar1)
print(end = ' \n ')

# ElevarAlCuadrado

cuadrado = lambda n: n * n
print('El cuadrado es:',cuadrado(5))
print(end = ' \n ')
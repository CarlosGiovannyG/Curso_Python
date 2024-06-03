"""Nos prmiten extraer valores de una funcion y almacenarlos de uno en uno en objetos iterables
    sin la nesecidad de almacenar todos a la vez en la memoria RAM"""
# ASÍ SERIA UNA LISTA NORMAL

def genrador_multiplos(limite):
    numero = 1
    lista_numeros = []

    while numero <= limite:
        lista_numeros.append(numero * 7)
        numero += 1
    return lista_numeros
print(genrador_multiplos(10))
print(" ")
print(" ")
print(" ")

"""La funcion yield nos permite generar un objeto iterable. y podremos alamcenar los datos de la funcion 
    en una variable, la cual al imprimirla vemos un objeto.
    1. Para poder visualizar los ebjetos almacenados en el generador aplicamos un for"""

def generador_multiplos1(limite):
    numero = 1
    while numero <= limite:
        yield numero * 7
        numero += 1

obtiene_multiplos1 = generador_multiplos1(10)
print(obtiene_multiplos1)

for n in obtiene_multiplos1:
    print(n)
print(" ")
print(" ")
print(" ")

"""2.Podemos usar la funcion next() la cual nos retorna el siguiente elemento de un objeto iterable"""

def generador_multiplos2(limite):
    numero = 1
    while numero <= limite:
        yield numero * 7
        numero += 1

obtiene_multiplos2 = generador_multiplos2(10)
print(next(obtiene_multiplos2))
print(next(obtiene_multiplos2))
print(next(obtiene_multiplos2))
print(next(obtiene_multiplos2))
print(next(obtiene_multiplos2))
print(" ")
print(" ")
print(" ")

"""Cada vez que llamemos el generador sin importar donde estemos nos da el valor siguiente
    habiendo entrado en una pausa o suspensión desde la llamada anterior"""

print(next(obtiene_multiplos2))
print("hay muchas lineas de código")
print(next(obtiene_multiplos2))
print("hay muchas lineas de código")
print(next(obtiene_multiplos2))
print("hay muchas lineas de código")
print(next(obtiene_multiplos2))
print("hay muchas lineas de código")
print(next(obtiene_multiplos2))
print("hay muchas lineas de código")
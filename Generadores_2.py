"""Cuando indicamos un * adelante del parametro de unafunción, estamos indicando
    que se va a recibir un número indeterminado de argumentos.
    Ademas, esos parametros se recibirán en forrma de Tupla"""

def devuelve_lenguajes(*lenguajes):
    for leng in lenguajes:
        yield leng

lenguajes_obtenidos = devuelve_lenguajes("Python", "Java", "PHP", "Ruby", "Java Script")
print(next(lenguajes_obtenidos))
print(next(lenguajes_obtenidos))
print(next(lenguajes_obtenidos))
print(next(lenguajes_obtenidos))
print(" ")
print(" ")

"""Si queremos recorrer las letras de cada palabra debemos crear un FOR anidado para obtenerlas"""

def devuelve_lenguajes(*lenguajes):
    for leng in lenguajes:
        for n in leng:
            yield n

lenguajes_obtenidos = devuelve_lenguajes("Python", "Java", "PHP", "Ruby", "Java Script")
print(next(lenguajes_obtenidos))
print(next(lenguajes_obtenidos))
print(next(lenguajes_obtenidos))
print(next(lenguajes_obtenidos))
print(" ")
print(" ")

"""Para SIMPLIFICAR este FOR anidado usamos la instruccion YIELD FROM, el cual nos permite crear un 
    objeto iterable dentro de otro objeto iterable"""

def devuelve_lenguajes(*lenguajes):
    for leng in lenguajes:
        yield from leng

lenguajes_obtenidos = devuelve_lenguajes("Python", "Java", "PHP", "Ruby", "Java Script")
print(next(lenguajes_obtenidos))
print(next(lenguajes_obtenidos))
print(next(lenguajes_obtenidos))
print(next(lenguajes_obtenidos))
print(" ")
print(" ")
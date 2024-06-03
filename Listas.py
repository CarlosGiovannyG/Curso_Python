

"""son estructura de datos que nos permiten alacenar distintos tipos de
datos (estas equivalen a los arrays en otros leguajes). Son estructuras dinamicas
las cuales pueden mutar"""

lista1 = ["Carlos", 25, 98.3, True, "Giovanny", 56.3]
print(lista1)
# Si queremos imprimir toda la lista lo podemos hacer asi
print(lista1[:])
# Si queremos acceder a un elmento en especifico
print(lista1[2])
# Si queremos imprimir el ultimo elemento de la lista
print(lista1[-1])
# Si queremos imprimir una parte de la list
print(lista1[0:3])
# Asi podemos acceder desde el comienzo hasta cierta parte de la lista
print(lista1[:2])
# Asi accedemos desde cierta parte de la lista hasta el final
print(lista1[3:])
# Asi podemos acceder a los elementos pares
print('PARES', lista1[::2])
# Asi podemos acceder a los elementos pares
print('IMPARES', lista1[1::2])
# Para añadir un elemento a la lista
lista1.append("Gualtero")
print(lista1)
# Para insertar un elemento en cierta posicion
lista1.insert(2, "Londoño")
print(lista1)
# Para insertar un elemento en cierta posicion
lista1.insert(5, "Londoño")
print(lista1)
# Extender una lista, debemos agregar los elementos usando la funcion .extend
# y colocando los elementos entre brakets
lista1.extend(["Suba", "Bogota", "Colombia"])
print(lista1)
# Si queremos saber en que indice esta un elemento ponemos el elemento dentro del parentesis
print('INDICE DE UN ELEMENTO', lista1.index("Londoño"))
# Si queremos cuantas veces esta un elemento ponemos el elemento dentro del parentesis
print('conteo DE UN ELEMENTO', lista1.count("Londoño"))
# Con la funcion .remove podemos quitar un elemneto de la lista
# Si el elemento no esta en la lista nos dara una traza o error
lista1.remove(56.3)
print(lista1)
# Con la funcion .pop eliminamos el ultimo elemento de la lista
lista1.pop()
print(lista1)
"""Tambien podemos unir listas mediante la concatenacion con el signo 
de adicion creando una nueva lista"""
lista2 = ["Curso", "de", "Python"]
print('LISTA 2', lista2)
# ordenar una lista al reves
lista2.sort(reverse=True)
print('LISTA AL REVES', lista2)
# ordenar una lista
lista2O = sorted(lista2)
print('ORDENADA LISTA ', lista2O)
lista3 = lista1 + lista2
print(lista3)
"""Podemos multiplicar una lista para repetir sus valores"""
print(lista2 * 4)
"""Si queremos saber si un elemento esta dentro de una lista usamos el operador in;
este distingue de mayusculas y minusculas, devolviendo un valor true o false"""
print("Carlos" in lista1)

'''FUNCION ENUMERATE ME DEVUELVE UAN TUPA DE UNA LISTA CON INDICE Y VALOR DE LA POSICION '''

for list in enumerate(lista1):
    print(list)

for indice, list in enumerate(lista1):
    print(indice)
    print(list)

# con la palabra reservada del podemos quitar un elemneto de la lista pasandole el indice
# Si el elemento no esta en la lista nos dara una traza o error
del lista1[0]
print(lista1)

# con clear podemos limpiar una lista

lista1.clear()
print(lista1)

'''ORDENAR LISTAS COMPLEJAS'''
'''REVISAR FUNCION SORT'''

'''COMPRNSION DE LISTAS'''
usuarios = [
    ['carlos', 1],
    ['giovanny', 2],
    ['guatero', 3]
]

# 'MAP'
nombres = [usuario[0] for usuario in usuarios]
print(nombres)

# 'FILTER'
nombres = [usuario for usuario in usuarios if usuario[1]>2]
print(nombres)

# nombres = [usuario[0] for usuario in usuarios if usuario[1] > 2]
# print(nombres)

# nombres = list(map(lambda usuario: usuario[0], usuarios))
# nombres = list(filter(lambda usuario: usuario, usuarios))
# print(nombres)

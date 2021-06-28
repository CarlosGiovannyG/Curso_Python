

"""son estructura de datos que nos permiten alacenar distintos tipos de
datos (estas equivalen a los arrays en otros leguajes). Son estructuras dinamicas
las cuales pueden mutar"""

lista1 = ["Carlos", 25, 98.3,True,"Giovanny",56.3]
print(lista1)
#Si queremos imprimir toda la lista lo podemos hacer asi
print(lista1[:])
#Si queremos acceder a un elmento en especifico
print(lista1[2])
#Si queremos imprimir el ultimo elemento de la lista
print(lista1[-1])
#Si queremos imprimir una parte de la list
print(lista1[0:3])
#Asi podemos acceder desde el comienzo hasta cierta parte de la lista
print(lista1[:2])
#Asi accedemos desde cierta parte de la lista hasta el final
print(lista1[3:])
#Para añadir un elemento a la lista
lista1.append("Gualtero")
print(lista1)
#Para insertar un elemento en cierta posicion
lista1.insert(2, "Londoño")
print(lista1)
#Extender una lista, debemos agregar los elementos usando la funcion .extend
#y colocando los elementos entre brakets
lista1.extend(["Suba", "Bogota", "Colombia"])
print(lista1)
#Si queremos saber en que indice esta un elemento ponemos el elemento dentro del parentesis
print(lista1.index("Londoño"))
#Con la funcion .remove podemos quitar un elemneto de la lista
#Si el elemento no esta en la lista nos dara una traza o error
lista1.remove(56.3)
print(lista1)
#Con la funcion .pop eliminamos el ultimo elemento de la lista
lista1.pop()
print(lista1)
"""Tambien podemos unir listas mediante la concatenacion con el signo 
de adicion creando una nueva lista"""
lista2 = ["Curso", "de", "Python"]

lista3 = lista1 + lista2
print(lista3)
"""Podemos multiplicar una lista para repetir sus valores"""
print(lista2 * 4)
"""Si queremos saber si un elemento esta dentro de una lista usamos el operador in;
este distingue de mayusculas y minusculas, devolviendo un valor true o false"""
print("Carlos" in lista1)

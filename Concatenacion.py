"""
Por ahora hay cuatros formas para concatenar en python,
las cuales son las mas usadas
"""
texto1 = "Hola"
texto2 = "Mundo"

"""
la primera solo basta con agregar un signo de adicion entre las variables
siempre y cuando estas sean str
"""
textoFinal = texto1 + " " + texto2
print(textoFinal)

"""
la segunda en concatenando con el uso de comodines %s a los cuales se les
asigna entre parentesis las variables a concatenar 
"""

print("El saludo es: %s %s " % (texto1, texto2))
"""
la tercera es con el uso de la funcion format para la cual en llaves se
asigna un valor a cada variable a concatenar, con esta funcion se puede
cambiar el orden de las variables, si no se asigna un numero las llaves
toman por defecto la posicion de las variables 
"""

saludoFinal = "Saludo: {0} {1}".format(texto1, texto2)
print(saludoFinal)
"""
la cuarta forma es con el uso de la funcion format y entre las llaves
asignar unas variables las cuales almacenaran las variables a concatenar

"""

saludoFinal2 = "Saludo: {x} {y}".format(x=texto1, y=texto2)
print(saludoFinal2)
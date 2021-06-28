"""
Para trabajar con texto  existen muchas funciones que nos permiten hacer
diferentes cosas como cambiarlo, contarlo, transformarlo,etc.
"""
texto = "bienvenidos a mi sitio Web---+---"
print(texto)
"""con la funcion lower convertimos todo el texto en minusculas"""
print(texto.lower())
"""Con la funcion upper convertimos todo el texto en mayusculas"""
print(texto.upper())
"""Con la funcion tittle convertimos todo el texto en formato titulo"""
print(texto.title())
"""Con la funcion find sabemos la posicion que una porcion de texto se encuentra
dentro de la cadena"""
print(texto.find("mi"))
"""Con esta funcion sabemos cuantas veces se repite una porcion o caracter
dentro de una cadena"""
print(texto.count("e"))
"""Con esta funcion podemos reemplazar un caracter por otro que necesitemos"""
textoFinal = texto.replace("e", "2")
print(textoFinal)
"""Con la función .is sabemos que tipo de texto hay en la cadena devolviendo 
una respuesta True o False; esta funcion nos proporciona varios factores a evaluar
numerico, digital, alpha, lower, etc, las cuales podemos usar  """
valor = texto.isnumeric()
print(valor)
"""Con la funcion split podemos convertir una cadena en un array, basta con dejar
 un espacio entre las comillas del parentesis"""
cadenaSeparada = texto.split(" ")
print(cadenaSeparada)
""" Podemos acceder a un caracter de una cadena de texto colocando la posicion
 dentro de unos brakeds     """
print(texto[5])
print(texto[10])
"""Para acceder a un caracter de una cadena de atras hacia adelante
anteponemos el signo - al numero"""
print(texto[-8])
print(texto[-9])
"""Con la funcion len contamos la cantidad de caracteres que contiene
   una cadena, este conteo tambien agraga los espacios"""
print(len(texto))
"""Con la funcion capitalizer ponemos la primera letra de una cadena en mayuscula"""
print(texto.capitalize())
"""Con el metodo wwapcase tranformamos las letras de una cadena
    de mayus a minus y visceversa"""
print(texto.swapcase())
"""con el metodo strip eliminamos los espacios en blanco y/o caracteres especiales,
    estos ultimos encionandolos dentro del parentesis"""
print(texto.strip('-+'))
"""Eliminamos de la parte izquierda de una cadena"""
print(texto.lstrip('-+'))
"""Eliminamos de la parte derecha de una cadena"""
print(texto.rstrip('-+'))
"""Completamos una cadena en la izquierda hasta alcanzar
    la cantidad de caracteres que querramos con un caracter especial"""
print(texto.ljust(45, "#"))
"""Completamos una cadena en la derecha hasta alcanzar
    la cantidad de caracteres que querramos con un caracter especial"""
print(texto.rjust(45, "#"))
"""Completamos una cadena al centro hasta alcanzar
    la cantidad de caracteres que querramos con un caracter especial"""
print(texto.center(45, "#"))

sdate = "01-06-2021"
sp = sdate.split("-")
print(sp)
print('dia:', sp[0], '-mes:', sp[1], '-año:', sp[2])
"""Completamos con ceros al inicia una cadena de texto hasta el numero
    requerido entre los parentesis"""
account = '123456789'
print(account.zfill(15))

"""
Para trabajar con texto  existen muchas funciones que nos permiten hacer
diferentes cosas como cambiarlo, contarlo, transformarlo,etc.
"""
texto = "bienvenidos a mi sitio Web---+---"
print('🚀👉 file:Cadenas.py-6 string')
print(texto)
print()
'''De esta forma podemosm imprimir de manera consecutiva la misma variable las veces que se indique'''
print('🚀👉 file:Cadenas.py-9 string * 3')
print(texto * 3)
print()
"""con la funcion lower convertimos todo el texto en minusculas"""
print('🚀👉 file:Cadenas.py-12 strign en minusculas')
print(texto.lower())
print()
"""Con la funcion upper convertimos todo el texto en mayusculas"""
print('🚀👉 file:Cadenas.py-15 string mayusculas')
print(texto.upper())
print()
"""Con la funcion tittle convertimos todo el texto en formato titulo"""
print('🚀👉 file:Cadenas.py-18 string en forma titulo')
print(texto.title())
print()
"""Con la funcion find sabemos la posicion que una porcion de texto se encuentra
dentro de la cadena"""
print('🚀👉 file:Cadenas.py-22 posicion de mi en la frase')
print(texto.find("mi"))
print()
"""Con esta funcion sabemos cuantas veces se repite una porcion o caracter
dentro de una cadena"""
print('🚀👉 file:Cadenas.py-26 cuantas i hay en la frase')
print(texto.count("i"))
print()
"""Con esta funcion podemos reemplazar un caracter por otro que necesitemos"""
print('🚀👉 file:Cadenas.py-29 reemplazamos la i por el 2')
textoFinal = texto.replace("i", "2")
print(textoFinal)
print()
"""Con la función .is sabemos que tipo de texto hay en la cadena devolviendo 
una respuesta True o False; esta funcion nos proporciona varios factores a evaluar
numerico, digital, alpha, lower, etc, las cuales podemos usar  """
valor = texto.isnumeric()
print('🚀👉 file:Cadenas.py-36 validacion si es numerico')
print(valor)
print()
"""Con la funcion split podemos convertir una cadena en un array, basta con dejar un espacio entre las comillas del parentesis"""
cadenaSeparada = texto.split(" ")
print('🚀👉 file:Cadenas.py-40 string hecho array')
print(cadenaSeparada)
print()
""" Podemos acceder a un caracter de una cadena de texto colocando la posicion
 dentro de unos brakeds """
print('🚀👉 file:Cadenas.py-44 caracter de la posicion 5')
print(texto[5])
print()
print('🚀👉 file:Cadenas.py-46 caraccter de la posicio 10')
print(texto[10])
print()
print('🚀👉 file:Cadenas.py-46 string hasta la posicion 11')
print(texto[:11])
print()
print('🚀👉 file:Cadenas.py-46 string desde la posicion 11')
print(texto[11:])
print()
print('🚀👉 file:Cadenas.py-46 string desde la posicion 11 hasta la 20')
print(texto[11:20])
print()
"""Para acceder a un caracter de una cadena de atras hacia adelante
anteponemos el signo - al numero"""
print('🚀👉 file:Cadenas.py-50 caracter de la posicio -8')
print(texto[-8])
print()
print('🚀👉 file:Cadenas.py-50 caracter de la posicio -9')
print(texto[-9])
print()
"""Con la funcion len contamos la cantidad de caracteres que contiene
   una cadena, este conteo tambien agraga los espacios"""
print('🚀👉 file:Cadenas.py-56 largo del string')
print(len(texto))
print()
"""Con la funcion capitalizer ponemos la primera letra de una cadena en mayuscula"""
print('🚀👉 file:Cadenas.py-59 primera letra en mayuscula')
print(texto.capitalize())
print()
"""Con el metodo swapcase tranformamos las letras de una cadena
    de mayus a minus y visceversa"""
print('🚀👉 file:Cadenas.py-63 cambio el strig de min a may  y visc...')
print(texto.swapcase())
print()
"""con el metodo strip eliminamos los espacios en blanco y/o caracteres especiales, estos ultimos mencionandolos dentro del parentesis *lstrip* eliminina los espacios de la izquierda *rstrip* elimina los espacios de la derecha"""
print('🚀👉 file:Cadenas.py-66 elimincaion de espacios en blanco')
print(texto.strip())
print()
print('🚀👉 file:Cadenas.py-66 elimincaion de caracteres especiales')
print(texto.strip('-+'))
print()
"""Eliminamos de la parte izquierda de una cadena"""
print('🚀👉 file:Cadenas.py-71 eliminacion parte izqu')
print(texto.lstrip('-+'))
print()
"""Eliminamos de la parte derecha de una cadena"""
print('🚀👉 file:Cadenas.py-74 eliminacion parte der')
print(texto.rstrip('-+'))
print()
"""Completamos una cadena en la izquierda hasta alcanzar
    la cantidad de caracteres que querramos con un caracter especial"""
print('🚀👉 file:Cadenas.py-78 alargamos la cadena a la izq')
print(texto.ljust(45, "#"))
print()
"""Completamos una cadena en la derecha hasta alcanzar
    la cantidad de caracteres que querramos con un caracter especial"""
print('🚀👉 file:Cadenas.py-78 alargamos la cadena a la der')
print(texto.rjust(45, "#"))
print()
"""Completamos una cadena al centro hasta alcanzar
    la cantidad de caracteres que querramos con un caracter especial"""
print('🚀👉 file:Cadenas.py-78 alargamos la cadena al centro')
print(texto.center(45, "#"))
print()
print('🚀👉 file:Cadenas.py-94 funcion IN para srigns');
print('dos' in texto)
print()
print('🚀👉 file:Cadenas.py-94 funcion NOT IN para srigns');
print('dos' not in texto)
print()
sdate = "01-06-2021"
sp = sdate.split("-")
print('🚀👉 file:Cadenas.py-91 fecha en array');
print(sp)
print()
print('🚀👉 file:Cadenas.py-93 fecha fromatead');
print('dia:', sp[0], '-mes:', sp[1], '-año:', sp[2])
"""Completamos con ceros al inicia una cadena de texto hasta el numero
    requerido entre los parentesis"""
account = '123456789'
print(account.zfill(15))
print()
texto_largo = """Esto es
un texto en varias lineas de codigo 
 en una sola variable
"""
print('🚀👉 file:Cadenas.py-94 estring largo')
print(texto_largo)
print()
texto = "bienvenidos a mi \"sitio\" Web---+---"
print('🚀👉 file:Cadenas.py-115 back slash para poder poner comillas doblews dentro de las misas');
print(texto)
print()
nombre= 'Carlos'
apellido='Gualtero'
nombre_completo= f"{nombre} {apellido}"
print('🚀👉 file:Cadenas.py-114 funcion format');
print(nombre_completo)
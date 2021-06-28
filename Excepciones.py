"""Una excepción es un error en tiempo de ejecucion
    (durante la ejecucion de un programa"""
"""Al tener un código, sin error de sintaxis  pero no se puede ejecutar por algún motivo 
    esto se llama una excepsión y esto puede parea todo nuestro programa"""

"""     numero1 = 20
        numero2 = 0
        print("La división de {0} entre {1} es: {2}".format(numero1, numero2, (numero1 / numero2)))
        print("Aquí termina mi programa")
"""

"""Para evitar lo anterior existe una estructura llamada TRY y nos permite saltar ese
    error para seguir ejecuntando nuestro programa"""

numero1 = 20
numero2 = 0

try:
    print("La división de {0} entre {1} es: {2}".format(numero1, numero2, (numero1 / numero2)))
except:
    print("Error de programa .....")

print("Aquí termina mi programa")
print(" ")
print(" ")
print(" ")

"""Tambein podemos usar la clausula finally que siempre se ejecutará sin importar si 
    cumple la excepsión o no"""
numero1 = 20
numero2 = 2

try:
    print("La división de {0} entre {1} es: {2}".format(numero1, numero2, int((numero1 / numero2))))
except:
    print("No se puede dividir entre %s ....." % numero2)
finally:
    print("¡Yo siempre aparezco!")

print("Aquí termina mi programa")
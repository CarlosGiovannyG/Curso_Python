"""Bucles: son estrcuturas de control de flujo que repiten 1 o varias
    lines de codigo"""

for num in range(0,20,2):
    print("Valor actual: %s " % num)

for i in range(1,13):
    print("{0} x {1} es: {2}".format(i, i, (i * i)))

for i in range(1,5):
    print("Tabla del ", i)
    for f in range(1,6):
        print(i, " x ", f, " = ", (i*f))

lista = ["Carlos", "Giovanny", "Gultero", "Londoño"]

for nom in lista:
    print("cantidad de letras de {0} es: {1}".format(nom,len(nom)))
print("La cantidad de letras de la cadena es: ", (len(lista[0]) + len(lista[1]) + len(lista[2]) + len(lista[3])))
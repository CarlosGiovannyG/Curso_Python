"""El bucle while es una estructur que nos permite ralizar multiple interacciones
    basandonos en el resultado de una expresion lógica que pude tener como
     resultado un valor falso o verdadero (True or False) debemos tener presente de darle
     un final al bucle pra que no que infinito"""

indice = 1
print("****************Números de 1 a 9********************")
while indice < 10:
    print("valor actual: %s" % indice)
    indice = indice + 1

print("Hemos terminado el bucle while y continúa el programa")
print(" ")
print(" ")
print(" ")
print(" ")


print("****************Números pares menor o igual a 100********************")
inicio = 2

while inicio <= 100:
    print("Número par menor o igual a 100 es: %s" % inicio)
    #otra manera de incrementar una variable es
    inicio += 2

print("Hemos terminado el bucle while y continúa el programa")

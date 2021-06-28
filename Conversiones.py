"""
Para realizar conversiones de datos en python solo debes saber el uso
que le vamos a dar a cada tipo de dato para asi saber la funcion
que vamos a usar para poder convertir.
lo podemos hacer de:
texto (str) ==> entero (int)
entero (int) ==> texto (str)
texto (str) ==>  flotante (float)
flotatnte (float) ==>  entero (int)
y visceversa
"""

numero1 = "35"
numero2 = "18"
print(numero1 + numero2)


num1 = int(numero1)
num2 = int(numero2)
print(num1 + num2)

sueldo = 1200.43
sueldoEntero = int(sueldo)
print(sueldoEntero)

valor = "4500.89"
valorDecimal = float(valor)
print(valorDecimal * 3)

edad = 100
print(len(str(edad)))

year = 2022
a = 25
b = 18.9
while a > b:
  a = a+(a*0.02)
  b = b+(b*0.03)
  year += 1
print("El pais B superara a A en el año: " + str(year))


"""def poblacion(pA, pB):
  anio = 2022
  while pA > pB:
    pA += pA*0.02
    pB += pB*0.03
    
    anio += 1
  return print("Año: ", anio, "\nTotal población A: ", pA, "\nTotal poblacion B: ", pB)

pobA = 25e6
pobB = 18.9e6
poblacion(pobA, pobB)"""

"""SEGUNDO  numero1 = int(input('Ingresa un valor: \n'))

while numero1 != 1:
      if numero1 % 2 == 0:
          print(numero1,"",numero1//2)
      else:
          print(numero1," ",numero1 * 3 + 1)
      numero1 = int(input('Ingresa un valor: \n'))"""


"""PRIMERO   numero = int(input('Ingresa un valor: \n'))

while numero > 0:
      cuadrado = numero * numero
      print('El cuadrado es:',cuadrado)
      numero = int(input('Ingresa un valor: \n'))"""

"""
def factorial(n):
      if n == 0 or n == 1:
            return 1
      aux = 1

      for i in range(n, 0, -1):
            aux = aux * i
      return aux

n = int(input("Ingresa un valor maximo 10: \n "))

for i in range(1, n + 1):
      print(i, factorial(i), end=" \n")"""

"""
flag = True
aux = 0
while flag:
      print(aux)
      aux += 1

      if aux == 11:
            flag = False
else:
      print('Sirvió')

AREA DE UN RECTANGULO ES A * B
_______________*************************____________________________
import math
def areaRectangulo(a,b):
      resultado = a * b
      return resultado

def areaCirculo(r):
      return math.pi * r**2

a = int(input('Ingresa altura: \n'))
b = int(input('Ingresa base: \n'))
r = int(input('Ingresa radio: \n'))

area1 = areaRectangulo(a,b)
area2 = areaRectangulo(b,a)
area3 = int(areaCirculo(r))
areaTotal = area1 + area2 + area3

print(areaTotal)
"""
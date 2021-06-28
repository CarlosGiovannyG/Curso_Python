"""Factorial de un numero es el producto de todos los numeros positivos enteros
    comprendidos entre 1 y un determinado numero"""

# factorial de 5: 1 * 2 * 3 * 4 * 5 = 120
# factorial de 4: 1 * 2 * 3 * 4 = 24

numero = int(input("Ingrese un numero: \n"))

factorial = 1

for n in range(1, (numero + 1)):
    factorial = factorial * n

print("El factorila de {0} es: {1}".format(numero, factorial))

# forma 2 de hayar un factorial

x = int(input('Ingresa un número: '))
fac = 1
for i in range(x):
    fac *= i + 1
    print(i + 1, fac)

# forma 3 de haar un factorial

def factorial(n):
    if n == 0 or n == 1:
        return 1
    aux = 1
    for i in range(n, 0, -1):
        aux = aux * i
    return aux

n = int(input("Ingresa un valor maximo 10: \n "))

for i in range(1, n + 1):
    print(i, factorial(i), end=" \n")
'''El * antes del parametro me permite poder resibir una cantidad de argumentos indeterminada desde dos en adelante hasta infinito osea iterables'''


def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)


suma(2, 5, 7)
suma(2, 5)
suma(2, 8, 7, 45, 32)

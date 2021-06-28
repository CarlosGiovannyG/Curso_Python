# range(): rea una lista inmutable de números enteros en sucesión
# ella crea la lista desde la posicion cero por defecto
numero = range(5)
print(numero[2])
"""para acceder a una posición de la lisa de numeros creada basta con poner 
    la posicion dentro de unos brakets
"""
print(numero[4])
"""podemos crear una lista dando en el primer parametro desde que numero comienza
    y en el segundo parametro hasta que numero incrementaria, estos separados por coma"""
numero1 = range(5, 50)
print(numero1[6])
"""podemos usar los tres parametros que acepta la funcion para crear una lista desde un punto
    hasta un punto final, y con el tercer argumento condicionando la cantidad de caracteres
    de intervalo"""
numero2 = range(5, 50, 5)
print(numero2[7])
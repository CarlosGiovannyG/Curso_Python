"""cona la funcion input solicitamos los datos mediante teclado,
    todos los datos son tomados como str"""
nombre = input('Ingrese su nombre \n')
"""Debemos tener presente de hacer el casteo necesario para convertir los valores
    a entros o flotantes al ingresarlos"""
edad = int(input('Ingrese su edad \n'))
edadFutura = edad + 20
print('Hola, '+ nombre)
print('Tu edad es: ', edad)
print('Tu edad (dentro de 20 años) será: ', edadFutura)

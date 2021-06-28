"""Es un conjunto de instrucciones que realiza un proceso.
su principal ventaja es que nos ayudan a evitar código repetido"""

def saludar (a,b,c):
    print(a,b,c)
    return 'Hola'

a='Carlos'
b='Giovanny'
c='Gualtero'
print(saludar(a,b,c))

def evaluarSueldoMinimo (sueldo):
    if sueldo >= 850:
        print('Cumples con el sueldo')
    else:
        print('Ganas menos que el sueldo minimo')

s = 1200
evaluarSueldoMinimo(s)
""" repetida
texto = list(input(" "))

for i in texto:
    aux = texto.count(i)
     
    if aux > 1:
        print("Es repetido: {0}".format(i))
    """

# palindrome
"""def tieneRepetidos(arr):
    if arr[::-1] == arr: print('Es palídrome')
    else: print('No es palídrome')

x = list(input('Ingrese una lista: ').split(', '))
tieneRepetidos(x)

print(x)"""

def contieneVocalRepetida(arr):
    existe = []
    for i in arr:
        if i.count('a') > 1 : existe.append(i)
        if i.count('e') > 1 : existe.append(i)
        if i.count('i') > 1 : existe.append(i)
        if i.count('o') > 1 : existe.append(i)
        if i.count('u') > 1 : existe.append(i)
    if not existe: print('No existe')
    else: print(', '.join(existe))

x = list(input('Ingrese una lista: ').split(', '))
contieneVocalRepetida(x)

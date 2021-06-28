
"""Dabale arroz a la zorra el abad"""

"""texto = input(" ")
textoSinEspacios = texto.replace(" ","")
textoAlReves = textoSinEspacios[::-1]

if textoSinEspacios == textoAlReves:
    print(texto)
else:
    print("No existe")"""
    
x = input('Ingrese un String: ')
if x == x[::-1]: print('Es palíndrome')
else: print('No es palíndrome')

texto = input(" ")
textoMinusculas = texto.lower()
textoSinEspacios = textoMinusculas.replace(" ","")
textoAlReves = textoSinEspacios[::-1]

if textoSinEspacios == textoAlReves:
    print("Es palíndromo")
else:
    print("No es")
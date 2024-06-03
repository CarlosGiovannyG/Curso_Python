
"""Dabale arroz a la zorra el abad"""

"""texto = input(" ")
textoSinEspacios = texto.replace(" ","")
textoAlReves = textoSinEspacios[::-1]

if textoSinEspacios == textoAlReves:
    print(texto)
else:
    print("No existe")"""

# x = input('Ingrese un String: ')
# if x == x[::-1]: print('Es palíndrome')
# else: print('No es palíndrome')

# texto = input(" ")
# textoMinusculas = texto.lower()
# textoSinEspacios = textoMinusculas.replace(" ","")
# textoAlReves = textoSinEspacios[::-1]

# if textoSinEspacios == textoAlReves:
#     print("Es palíndromo")
# else:
#     print("No es")


def no_space(texto):
    nuevo_texto = ''
    for char in texto:
        if char != ' ':
            nuevo_texto += char
    return nuevo_texto


def reves(texto):
    texto_al_reves = ''
    for char in texto:
        texto_al_reves = char + texto_al_reves
    return texto_al_reves


def es_palindromo(texto):
    texto = no_space(texto)
    texto_al_reves = reves(texto)
    return texto.lower() == texto_al_reves.lower()


print(es_palindromo(input('Ingrese un String: ')))
print(es_palindromo('amo la paloma'))
print(es_palindromo('Carlos Giovanny'))
print(es_palindromo('Reconocer'))
print(es_palindromo('somos o no somos'))

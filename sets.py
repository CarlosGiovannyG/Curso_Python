'''los sets elimina los elelmentos repetidos de una lista'''
primer = {1, 1, 2, 2, 3, 4}
segundo = [3, 3, 4, 5]

print(primer)
print(segundo)

'''podemmos covertir una lista en un set con la palabra set'''

tercer = set(segundo)
print(tercer)

'''podemos unir un set con otro los une eliminando repetidos'''
print(primer | tercer)
'''podemos crear una interseccion compara los elementos que estan en los dos set'''
print(primer & tercer)
'''podemos validar la diferencia en dos sets'''
print(primer - tercer)
'''podemos validar la diferencia simetrica en dos sets'''
print(primer ^ tercer)

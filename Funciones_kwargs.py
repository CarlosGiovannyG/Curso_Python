'''Cuando usamos la propiedad kwargs de python es necesario darle un nombre a los parametros que le vayamos a pasar y podremos acceder a estos con los parentesis cuadrados desde la funcion'''


def get_product(**datos):
    print(datos)
    print(datos['id'])
    print(datos['name'])


get_product(id=23,
            name='telefono',
            desc='esto es un telefono')

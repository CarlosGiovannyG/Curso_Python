"""
Constructores: Sirven para darle un estado inicial a nuestro objeto, esto quiere decir
que se le dan unos valores iniciales a los objetos, para esto se dan los valores al 
momento de instancia el objeto. 
Para hacer uso de un constructor definimos una función constructora con la función
__init__(self); dentro de ella asignamos los atributos que se asignan en el estado 
inicial del objeto. El parámetro inicial siempre es self la cual hace referencia a la propia clase;
seguido nombramos los parámetros que le vamos a asignar al objetos (de nombre seria nom)
dentro de la función llamamos la palabra self y seguido de un punto nombramos el atributo 
luego con un igual se asigna al argumento asignado anteriormente dentro del paréntesis  
    
    -*- del atributo "nombre" se podría poner el parámetro "nom"
        -*- self.nombre = nom
Para que luego al nombrar a cada objeto, el cual se nombra como si fuera una variable, pro después
del igual se llama a la clase y dentro del paréntesis se asignan los atributos de cada objeto, como
puede ser nombre, apellido, etc.
Asi con un print llamamos al objeto y seguido de un punto lamamos el atributo que queremos mostrar
"""


class Curso():
    def __init__(self, nom, cre, pro):
        self.nombre = nom
        self.creditos = cre
        self.profesion = pro


print(" ")
print(" ")
curso1 = Curso("Matemáticas", 5, "Ingernieria Civil")
print(curso1.nombre, curso1.creditos, curso1.profesion)
print(" ")
print(" ")
curso2 = Curso("Lenguaje", 4, "Ingernieria Industrial")
print(curso2.nombre, curso2.creditos, curso2.profesion)
print(" ")
print(" ")
curso3 = Curso("Inglés", 3, "Comercio Exterior")
print(curso3.nombre, curso3.creditos, curso3.profesion)
print(" ")
print(" ")

"""
El ENCAPSULAMIENTO: consiste denegar el acceso a los atributos y metodos internos 
de la clase desde el exterior. 
En Python no existe, pero se puede simular precediendo los atributos y métodos 
con dos barras bajs ( __ ) antes de dar nombre al atributo
Solo se pueden acceder a estos atributos encapsulados desde la misma clase, definiendo 
una funcion para este proposito
"""

class Curso():
        
    def __init__(self, nom, cre, pro): 
        self.nombre = nom
        self.creditos = cre
        self.profesion = pro
        self.__imparticion = "Presencial"
    
    def mostrar_datos(self):
        dat = "Nombre: {0} / Creditos: {1} / Modo de Impartición: {2}"
        #print(dat.format(self.nombre, self.creditos, self.__imparticion))



print(" ")
print(" ")

curso1 = Curso("Matemáticas", 5, "Ingernieria Civil")
print(curso1.nombre, curso1.creditos, curso1.profesion)
curso1.mostrar_datos()
curso1.__imparticion = "Virtual"
print(curso1.__imparticion)
print(" ")
print(" ")


curso2 = Curso("Lenguaje", 4, "Ingernieria Industrial")
print(curso2.nombre, curso2.creditos, curso2.profesion )
print(" ")
print(" ")



curso3 = Curso("Inglés", 3, "Comercio Exterior")
print(curso3.nombre, curso3.creditos, curso3.profesion )
print(" ")
print(" ")
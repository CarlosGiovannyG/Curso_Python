"""
El ENCAPSULAMIENTO: consiste denegar el acceso a los atributos y metodos internos 
de la clase desde el exterior. 
En Python no existe, pero se puede simular precediendo los atributos y métodos 
con dos barras bajs ( __ ) antes de dar nombre al atributo
Solo se pueden acceder a estos atributos encapsulados desde la misma clase, definiendo 
una funcion para este proposito. 
En este caso vemos una funcion encapsulada la cual hará su proposito si poder ser 
accesible desde el exterior solo se puede acceder a ella desde la misma clase
"""

class Curso():
        
    def __init__(self, nom, cre, pro): 
        self.nombre = nom
        self.creditos = cre
        self.profesion = pro
        self.__imparticion = "Presencial"
    
    def __verificardocente(self):
       
        if self.__imparticion == "Presencial":
            return True
        else:
            return False
        
    
    def mostrar_datos(self):
        dat = "Nombre: {0} / Creditos: {1} / Modo de Impartición: {2}"
        print(dat.format(self.nombre, self.creditos, self.__imparticion))
        docente_asignado = self.__verificardocente()
        if docente_asignado:
            print("Existe docente asignado")
        else:
            print("No es necesario docente")
            

print(" ")
print(" ")

curso1 = Curso("Matemáticas", 5, "Ingernieria Civil")
print(curso1.nombre, curso1.creditos, curso1.profesion)
curso1.mostrar_datos()
print(" ")
print(" ")
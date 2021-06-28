""" El principío  de sustitución significa que cuando aplicamos herencia, existen clases
    padres y clases hijas; esto signifca que los objetos de la clase hija siempre serán 
    INSTANCIADOS a la clase padre. No se puede decir lo mismo de lo contrario; los objetos 
    de la clase pádre no siempre son INSTANCIADOS a la clase hija.
    Ejemplo de esto un ESTUDIANTE siempre será una persona; pero una persona no será siempre
    un ESTUDIANTE.
    Para comprobar esto usamos la función 
                                            ISINSTANCE(objeto, clase)
                                            
    Esta función nos ayuda a comprobar si un objeto es INSTANCIADO a una clase dando un
    resultado TRUE. De lo contrario nos dará un resultado FALSE.
                    
""" 
class Persona():
    
    def __init__(self, apePat, apeMat, nom):
        self.apellido_paterno = apePat
        self.apellido_materno = apeMat
        self.nombres = nom
    
    def mostrar_nombre_completo(self):
        txt = "{0} {1} {2}"
        return txt.format(self.apellido_paterno, self.apellido_materno, self.nombres)

    def datos(self):
        print(self.mostrar_nombre_completo())
        
    

class Estudiante(Persona): 
    
    def __init__(self,apePat, apeMat, nom, pro): 
        super().__init__(apePat, apeMat, nom)
        self.profesion = pro 
    
    def datos(self):
        super().datos()
        print("Profesión: ", self.profesion)   


estudiante1 = Estudiante("Gualtero", "Londoño", "Carlos Giovanny", "Estudiante")
print(" ")
print(" ")
print(estudiante1.datos())
print(" ")
print(" ")
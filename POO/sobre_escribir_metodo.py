""" La sobre escritura de metodo significa que dentro de clase padre creamos un metodo que
    nos muestre algo en paricular (en este caso los datos de una persona). Acto seguido
    en la clase hija creamos otro metodo llamado igual que al metodo antes creado en la 
    clase padre. Y a esta le damos un comportamiento adicional (en este caso la profesion). 
    Hasta este punto el metodo tiene como prioridad EL PRICIPIO DE ESPECIFICACIÓN (da importancia
    a la clase donde fue creada o clase especifica o especializada). 
    Para hacer uso del metodo creado en la clase padre, lo hacemos usando la palabra SUPER y
    de esta manera podemos acceder al metodo de la clase hija y reutilizarlo
    
                    super().nombre_metodo_clase_padre()
                    
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
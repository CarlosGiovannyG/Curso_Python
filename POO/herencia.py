""" se define una clase padre con su respectivo costructor, a esta clase se le
    asignan los atributos en comun de cada objeto que vayamos a crear. 
    * Se crea un metodo o función en el cul especificamos la operación o acción
    que va a realizar.
    Luego podemos crear otra clase sin necesidad de darle un nuevo constructor, 
    para eso detro del parentesis se nombra la clase padre para que esta herede
    de dicha función los atributos y los metodos que contenga.
    Para agregar atributos que tenga esta clase hija que sean independientes o 
    propios, creamos un constructor dentro de esta clase.
    En la primera linea del constructor debemos hacer uso de la palabra reservada
    SUPER(). e invocamos al constructor de la clase PADRE y del mismo modo llamamos 
    los parametros que contiene el constructor de la clase PADRE, sin la palabra SELF. 
    y estos mismos los definimos dentro del constructor de la clase HIJA enseguida de 
    la palabra SELF y por ultimo los parametros que le vamos a agregar. 
    
    
                def __init__(self, par1, par2, par3, par4):
                    super().__init__(par1, par2, par3) 
                    self.parametro4 = par4
    
    
    
""" 
class Persona():
    
    def __init__(self, apePat, apeMat, nom):
        self.apellido_paterno = apePat
        self.apellido_materno = apeMat
        self.nombres = nom
    
    def mostrar_nombre_completo(self):
        txt = "{0} {1} {2}"
        return txt.format(self.apellido_paterno, self.apellido_materno, self.nombres)

class Estudiante(Persona): 
    
    def __init__(self,apePat, apeMat, nom, pro): 
        super().__init__(apePat, apeMat, nom)
        self.profesion = pro 
        


estudiante1 = Estudiante("Gualtero", "Londoño", "Carlos Giovanny", "Estudiante")
print(estudiante1.mostrar_nombre_completo())
print(estudiante1.profesion)
print(" ")
print(" ")
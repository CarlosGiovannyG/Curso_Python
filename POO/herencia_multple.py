""" La herencia multiple significa que una clase puede heredar o reutilizar de otras clases
    el código. EQuiere ecir que una clase HIJA puede heredar de multiples clases PADRES los
    metodos de ellas.
    Según lo necesitemos nombramos las clases PADRES en su determinado orden dentro de los
    parentesis de la clase hija.

                    class Clase_3(Clase_1, Clase_2)
                    class Clase_3(Clase_2, Clase_1)
"""
class Clase_a(): 
    
    def __init__(self, par1, par2): 
        self.parametro1 = par1
        self.parametro2 = par2
        
class Clase_b(): 
    
    def __init__(self, par3, par4, par5): 
        self.parametro3 = par3
        self.parametro4 = par4
        self.parametro5 = par5

class Clase_c(Clase_a,Clase_b): 
    pass

var = Clase_c(15, 21)
print(var.parametro1, var.parametro2)
""" Las relaciones entre clases pueden ser de dependencia o independencia, 

"""

class Pais():
    
    def __init__(self, nom, cap):
        self.nombre = nom
        self.capital = cap
        
    def __str__(self):
        txt = "PAIS: {0} \nCAPITAL: {1}".format(self.nombre, self.capital)
        return txt

class Ciudad():
    
    def __init__(self,nom, hab, dep, pais):
        self.nombre = nom
        self.habitantes = hab
        self.departamento = dep
        self.pais = pais
    
    def __str__(self): 
        txt = "CIUDAD: {0} \nN° HABITANTES: {1} \nDEPARTAMETO: {2} \n({3})".format(self.nombre, 
                                                                                   self.habitantes,
                                                                                   self.departamento,
                                                                                   self.pais)
        return txt


class Localidad():
    
    def __init__(self,nom, ciud):
        self.nombre = nom
        self.ciudad = ciud
    
    def __str__(self): 
        txt = "LOCALIDAD: {0} \n({1})".format(self.nombre,self.ciudad)
        return txt    
    


pais1 = Pais("Colombia", "Bogotá")
print(" ")
print(" ")
print(pais1)
print(" ")
print(" ")

ciudad1 = Ciudad("Bogota", 15000, "Cundinamarca", pais1)
print(" ")
print(" ")
print(ciudad1)
print(" ")
print(" ")

Localidad1 = Localidad("Suba", ciudad1)
print(" ")
print(" ")
print(Localidad1)
print(" ")
print(" ")
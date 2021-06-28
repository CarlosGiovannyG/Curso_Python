"""Con el metodo GET podremos acceder a un elemento encapsulado dentro de una clase;}
    y con el metodo SET podremos cambiar o asignar un nuevo valor a elemento en mención
"""
class Cuenta(): 
    
    def __init__(self, pro, sal, mon):
        self.__propietario = pro
        self.__saldo = sal
        self.__moneda = mon
        
    # Getters (metodo GET)
    def get_saldo(self):
        return self.__saldo
        
    def get_propietario(self):
        return self.__propietario
       
    def get_moneda(self):
        return self.__moneda
        
    
    #Setters (metodo SET)
    
    def set_moneda(self, moneda):
        self.__moneda = moneda

print(" ")
print(" ")       
cuenta1 = Cuenta("Carlos Giovanny", 15000, "Pesos")
print(cuenta1.get_saldo())
print(cuenta1.get_propietario())
print(cuenta1.get_moneda())
print(" ")
print(" ")
""" En este caso la funcion con el metodo SET creada dentro de la clase nos permite 
    cambiar el valor de moneda dando versatilidad en su uso"""
cuenta1.set_moneda("Dolares")
print(cuenta1.get_moneda())
print(" ")
print(" ")
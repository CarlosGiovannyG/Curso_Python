""" Cuando queremos imprimir una instancia sin acceder al atributo o funcion, 
    se nos va a mostrar el nombre de la clase de tipo objeto y el espacio de
    memoria que esta usando este objeto; para evitar esto se usa la funcion 
    'DEF __STR__(SELF) la cual nos permite indicar el texto a mostrar en este
    caso
""" 
class Curso():
        
    def __init__(self, nom, cre, pro): 
        self.nombre = nom
        self.creditos = cre
        self.profesion = pro
        
    def __str__(self):
        
        texto = "Estamos tabajando para mejorar"
        return texto
        
    
    
    
print(" ")
print(" ")
curso1 = Curso("Matemáticas", 5, "Ingernieria Civil")
print(curso1)
print(" ")
print(" ")
print(curso1.nombre, curso1.creditos, curso1.profesion)
print(" ")
print(" ")
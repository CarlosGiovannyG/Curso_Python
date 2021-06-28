"""
    el poliformismo significa muchas formas: quieres decir que un objeto puede cambiar
    o mutar su forma dependiendo del contexto en que se utilice, y al cambiar de forma
    tambien cambia su comportamiento 
    
""" 
class Estudainte():

    def describir(self):
        print("Soy un buen estudiante.")
        
class Docente():

    def describir(self):
        print("Me dedico a enseñar cursos.")

class Empleado():

    def describir(self):
        print("Trabajo en una gran empresa.")


def describir_persona(persona):
    persona.describir()

docente1 = Empleado()
print("")
print("")
describir_persona(docente1)
print("")
print("")
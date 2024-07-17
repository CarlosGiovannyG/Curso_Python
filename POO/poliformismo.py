"""
    el polimorfismo significa muchas formas: quieres decir que un objeto puede cambiar
    o mutar su forma dependiendo del contexto en que se utilice, y al cambiar de forma
    también cambia su comportamiento 
    
""" 
class Estudiante():

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

empleado = Empleado()
describir_persona(empleado)
estudiante = Estudiante()
describir_persona(estudiante)
docente = Docente()
describir_persona(docente)
print("")
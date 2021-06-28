"""
    ¿En qué consiste la programación orientada a objetos?
    Es un paradigma de la programación, o una forma de ver algo
    - Consiste en trasladar la naturaleza de los objetos de la vida reala código de programación
    (en algpun lenguaje de programación, en este caso Python)

    Los objetos de la realidad como pueden ser un auto, una persona, un animal, etc,
    tienen caracteristicas (Apellidos, nombre, sexo, etc; tambien llamados "atributos o propiedades")
     y funcionalidades o comportamientos ( saludar, comer, etc; tambien llamados
     "funciones o metodos"), cosas que pueden hacer

    Ventajas:
    - Modularización (división en pequeñas partes) de un programa completo.
    - Código fuente muy reutilizable
    - Código fuente más fácil de incrementar en el futuro y mantener
    - Si existe un fallo en uan pequeña parte del código el programa completo no debe fallar
    necesariamente. Además, es mas fácil de corregir esos fallos.
    - Encapsulamiento: Ocultamiento del funcionamiento interno de un objeto"""


# Una clase (class) es una plantilla que creamos de un objeto de realidad
class Persona():
    # propiedades, caracteristicas o atributos:
    apellidos = ""
    nombres = ""
    edad = 0
    despierta = False

    # funcionalidades
    def despertar(self):
        # self: Parámetro que hace referencia a la instancia perteneciente a la clase
        self.despierta = True
        print("Buen día")


# Nombramos un objeto
persona1 = Persona()
persona1.apellidos = "Gualtero Londoño"
persona1.edad = 20
print(persona1.apellidos)
persona1.despertar()
print(persona1.edad)
print(persona1.despierta)

print(" ")
print(" ")

# Nombramos otro objeto
persona2 = Persona()
persona2.apellidos = "Londoño Gualtero"
print(persona2.apellidos)
print(persona2.despierta)
print(" ")
print(" ")
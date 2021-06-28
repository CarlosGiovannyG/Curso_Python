"""
Ejercicios de us del condicional If con Tuplas
"""

print("--cursos--")

lista_cursos1 = ["Matematicas".lower(), "Biologias".lower(), "Lenguajes".lower(),
                "Ciencias".lower()]

lista_cursos = ["Matematica".lower(), "Biologia".lower(), "Lenguaje".lower(),
                "Ciencia".lower()]
print("-".join(lista_cursos))

curso = input("Ingrese el curso desesado \n")
curso = curso.lower()

if curso in lista_cursos + lista_cursos1:
    print("Curso %s selecciondo." % curso)
else:
    print("No existe ese curso...")
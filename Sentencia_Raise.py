
"""La función RAISE nos permite lanzar una excepsión al programa voluntariamente para
    no continuar con su ejecución"""

def evaluar_nota(nota):
    if nota < 0:
        print("Valor incorrecto ....")
        #raise ValueError("Valor incorrecto....")
    elif nota >= 16:
        raise ValueError("Valor incorrecto....")
        #print("Excelente")
    elif nota >= 11:
        print("Aprobado")
    else:
        print("Desaprobado")

evaluar_nota(17)
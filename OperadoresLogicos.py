#AND ==> Equivalente a "Y si ademas...."
#OR ==>  "O si no..."
#NOT ==> Negacion lo que es falso lo conviete a verdadero y visceversa
"""********** Tabla de condiciones en python****************"""
"""
not ==> True == False
        False == True

and ==> False - False == False
        False - True  == False
        True  - False == False
        True  - True  == True

or ==>  False - False == False
        False - True  == True
        True  - False == True
        True  - True  == True
"""

distancia = 1200
numero_hermanos = 3
salario_padres = 1500

tiene_beneficio = False

if (distancia > 1000 and numero_hermanos > 2) or  salario_padres < 2000:
        tiene_beneficio = True
        print("Tiene beneficio")
else:
        print("No tiene beneficio")



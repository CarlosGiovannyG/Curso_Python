"""
string == sexo;
sexo = (10 > 20) ? "Masculino" : "Femenino";
sexo = "Masculino" if 10 > 20 else "Femenino"
"""




sexos = ("Masculino", "Femenino")

sexo = sexos[1]
print(sexo)
sexo = sexos[0]
print(sexo)

posicion = True # == 1
sexo = sexos[posicion]
print(sexo)
sexo = sexos[not posicion] # FALSE == 0
print(sexo)

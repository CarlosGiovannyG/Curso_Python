
"""Son estructuras de datos que nos permiten almacenar distintos
valores. Los datos se alamcenan asociados a una clave unica; esto nos da una relacion
clave valor. Los elementos almacenados estan desordenados. el orden es indiferente
a la forma de almacenamiento, para crear un disccionarios se hace dentro de llaves,
y cada llave va unida a su clave por medio de los dos puntos, y la separacion de cada
elemento se hace por medio de una coma.
Los diccionarios nos permiten tener asociado cualquier tipo de datos"""
print("")
miDiccionario = {"España": "Madrid", "Perú": "Lima", "Alemania": "Berlin",
                "Colombia": "Bogota"}
print(miDiccionario)
print("")
"""Para imprimir una valor solo nesecitamos nombrar el dato asosiado a esa clave 
entre unos brakets"""
print(miDiccionario["Alemania"])
print("")
"""Para agregar un elemento al diccionario, llamamos el diccionario entre brakets 
colocamos el valor y con un igual incluimos la clave"""

miDiccionario["Caracas"] = "Venezuela"
print(miDiccionario)
print("")
"""Para reemplazar una clave del dicconario nombramos el diccionario entre 
brakets ponemos el dato y con igual asignamos la nueva clave"""
miDiccionario["Colombia"] = "Cali"
print(miDiccionario)
print("")
"""Con la clausula del borramos un dato y su respectiva clave"""
del miDiccionario["Caracas"]
print(miDiccionario)
print("")
"""Podemos definir una tupla para definir las llaves que va a tener un diccionario"""

llaves = ("Cundinamarca", "Tolima", "Quindio", "Caldas")
dicDepartamentos = {llaves[0]: "Bogota", llaves[1]: "Ibague", llaves[2]: "Armenia",
                    llaves[3]: "Manizales"}
print(dicDepartamentos)
print("")
"""Podemos definir un dicconario dentro de otro diccionario"""
dicDatosPersonales = {"Apellido": "Gualtero", }
print("")
# El método UPDATE agrega ítems a un diccionario

dict_ports1 = {22: "SSH", 80: "Http"}
dict_ports2 = {53: "DNS", 443: "https"}
print(dict_ports1)
dict_ports1.update(dict_ports2)
print(dict_ports1)
print("")
# SE PUEDEN HACER COMPARACIONES ENTRE DICCIONARIOS
a = {123: "Rojas", 87: "Rosas"} == {87: "Rosas", 123: "Rojas"}
print(a)
print({"Rosas": 123} != {"rosas": 123})
b = {123: "Rosas", 87: "rojas"} == {"Rosas": 123, 87: "rojas"}
print(b)
print("")
# DE LA SIGUIENTE MANERA SI NO EXISTE SE AGREGA O SI EXISTE LO MODIFICA
puertos = {80: "HTTP", 23: "SMTP", 443: "HTTPS"}
print(puertos)
puertos[23] = "Telnet"
print(puertos)
puertos[110] = "POP"
print(puertos)
print("")
# con un for podemos saber si un item esta en un diccionario
puertos = {80: "HTTP", 23: "SMTP", 443: "HTTPS"}
if 80 in puertos:
    print("yes")
    if 110 not in puertos:
        print("no")
    else:
        print("yes")
        
# CON UN CICLO FOR  PODEMOS OBTENER LAS LLAVES DE UN DICCIONARIO
print("")
dict_ports = {22:"SSH", 23:"telnet", 80:"Http"}
for key in dict_ports:
    print(key)
print("")

# CON UN CICLO FOR Y EL METODO ITEMS PODEMOS OBTENER LAS LLAVES Y SU 
# RESPECTIVO ITEMS, DE UN DICCIONARIO
print("")
dict_ports = {22:"SSH", 23:"telnet", 80:"Http"}
for k,v in dict_ports.items():
    print(k, "->", v)

print("")

print("")
# CON LA FUNCION LEN SABEMO EL NUMERO DE ITEMS DE UN DICCIONARIO
puertos = {80:"HTTP", 23:"SMTP", 443:"HTTPS"}
print(len(puertos))
print("")

print("")
# CON EL METODO GET SABEMOS EL VALOR DE UN ITEM A PARTIR DE LA LLAVE Y 
#TENEMOS LA OPCION DE DE PONER UN MENSAJE DE RETORNO SI NO SE ENCUENTRA 
dict1 = {"a":1, "b":2, "c":3}
print(dict1.get("a"))
print(dict1.get("d", "clave no encontrada."))
print("")

"""
CON LA FUNCION MAX SABEMOS EL VALOR MAXIMO
CON LA FUNCION MIN SABEMOS EL VALOR MINIMO
"""
print("")
# CON EL METODO KEYS OBTIENE UNA LISTA CON TODAS LAS CLAVES
# Y EL METODO VALUES OBTIENE LOS VALORES
dict1 = {"a":1, "b":2, "c":3}
print(list(dict1.keys()))
print(list(dict1.values()))
print("")

#El metodo dict permite convertir listas de listas y listas de tuplas a diccionarios.
print("")
puertos = [[80, "http"], [20, "ftp"], [23, "telnet"]]
d_port = dict(puertos)
print(d_port)
puertos = [(20, "ftp"), (80, "http"), (23, "telnet")]
d_port = dict(puertos)
print(d_port)
print("")



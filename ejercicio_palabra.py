"""
n = input("Ingresa Palabra:\n ")
b = input("Ingresa Frase: \n ")
bandera = True 
for i in n:
  x = b.find(i)
  if x ==-1:
    bandera = False
    break
  b= b[:x]+b[x+1:]
  
    
if bandera:
  print("la contiene")
else:
  print("no la contiene" )
"""
#crear entradas
#condicion para comparar pr1 y pr2 con los clientes

#pr1 = input(" ")
#pr2 = input(" ")
cliente = input(" ")
cont1 = 0
cont2 = 0

def letras (pr1, pr2):

  for i in cliente:
    x = pr1.count(i) 
    
  return

pr1 = input(" ")
pr2 = input(" ")

letras(pr1, pr2)


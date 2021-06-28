#Break: Permite salir de un bucle cuando se cumple una condición

for numero in range(1,6):
    print("El número es: %s" % numero)
print("Bucle terminado.")

for numero in range(1,6):
    if numero == 3:
        break
    print("El número es: %s" % numero)
print("Bucle terminado.")

#Continue: Permite omitir una parte de un bucle cuando se cumple una condición
# y continua con el resto

for numero in range(1,10):
    if numero >= 5 and numero <= 7:
        continue
    print("El número es: %s" % numero)
print("Bucle terminado.")

"""Pass: Permite continuar con una sentencia o funcion que ya no tiene o aun no tiene 
    un bloque de código util"""

for numero in range(1,10):
    if numero <= 3:
        pass #aqui no pasa nada
        print("El número es: %s" % numero)
    else:
        print("El siguiente es mayor o igual a 3 es: %s" % numero)

print("Bucle terminado.")
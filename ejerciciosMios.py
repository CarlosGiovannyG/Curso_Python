"""
1 ==> SOLICITAR NUMERO DE EMPLEADOS
2 ==> NOMBRE EMPLEADO
3 ==> SOLICITAR SUELDOS
4 ==> SOLICITAR BONIFICACIONES
5 ==> SOLICITAR DEDUCCIONES
6 ==> HACER CALCULOS
7 ==> ENVIAR DATOS
"""
def calcular_pago(sueldo,bonificaciones, deducciones):

    if sueldo <= 800:
        sueldo = sueldo + 100
    elif sueldo > 800 and sueldo <= 1000:
        sueldo = sueldo + 60

    if bonificaciones > 600:
        bonificaciones = 600
    elif bonificaciones < 0:
        bonificaciones = 0

    sueldo_total = sueldo + bonificaciones - deducciones
    return sueldo_total

cantida_empleados = int(input("Ingrese cantidad de empleados \n"))
empleados = {}

for i in range(0,cantida_empleados):
    identificacion = input("Ingresa número de identificación \n")
    sueldo = int(input("Ingresa el sueldo \n"))
    bonificaion = int(input("Ingresa la bonificación \n"))
    deduccion = int(input("Ingresa las deducciones \n"))
    empleados[identificacion]=[sueldo,bonificaion,deduccion]

for i in empleados:
    valores = empleados[i]
    print(i,calcular_pago(valores[0],valores[1],valores[2]))
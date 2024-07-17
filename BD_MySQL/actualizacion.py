""" Para hacer una lectura de datos usamos la sentencia SELECT propia de SQL.
    1. necesitamos un CURSOR que es un objeto relacionado con las DB y actuar omo un nexo 
    para poder hacer lectura de datos y hacer inserciones, actualizaciones y eliminaciones 
                    CURSOR = CONEXIÓN.CURSOR()
    Seguid a esto, ejecutamos un CURSOR.EXECUTE() la cual nos permitirá ejecutar una sentencia
    SQL, dentro del paréntesis hacemos una sentencia INSERT INTO entre comillas por ser STR seguido de
    la función TABLEBASE() y entre paréntesis marcar los campos que vamos a afectar seguido de la 
    palabra VALUES (), y en comillas sencillas los valores a ingresar
      
            CURSOR.EXECUTE("INSERT INTO(Nombres, Apellidos, Correo, Edad, Teléfono ) VALUES('','',)")
    Para hacer dinámico el proceso, recordemos usar variables para el ingreso de los datos, y crear otra 
    variable con la sentencia para crear el método y así quede mejor elaborado.
                    dato = input()
                    sentencia = "INSERT INTO(Nombres, Apellidos, Correo, Edad, Teléfono ) VALUES('{0}')".format(dato)
                    CURSOR.EXECUTE(sentencia)
"""

from logging import info
import mysql.connector
from mysql.connector import Error
try: 
    conexion = mysql.connector.connect(
        host = 'localhost',
        port = 3306,
        user = 'root',
        password = '',
        db = 'python'                
    )
 
    if conexion.is_connected():
        print("Conexion exitosa.")
        cursor = conexion.cursor()
        nomb = input('Ingrese los Nombres: \n')
        apel = input('Ingrese los Apellidos: \n')
        corr = input('Ingrese el E-Mail: \n')
        edad = input('Ingrese la Edad: \n')
        tele = input('Ingrese el Teléfono: \n')
        id = int(input('Ingrese Id a Actualizar: \n'))
        sentencia = """UPDATE usuarios SET nombres = '{0}',apellidos = '{1}',correo = '{2}',
                    edad ='{3}',teléfono = '{4}'
                    WHERE id = '{5}'""".format(nomb,apel,corr,edad,tele,id)
        cursor.execute(sentencia)
        conexion.commit()
        print('Registro Actualizado con Exito')
        
except Error as ex:
    print("Error en la conexion.", ex)
    
finally: 
    if conexion.is_connected():
        conexion.close() #Se cierra la conexion a la BD
        print("La conexión ha finalizado.") 
        


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
        id = int(input('Ingrese Id a Eliminar: \n'))
        sentencia = "DELETE FROM usuarios WHERE id = '{0}'".format(id)
        cursor.execute(sentencia)
        conexion.commit()
        print('Registro Eliminado con Exito')
        
except Error as ex:
    print("Error en la conexion.", ex)
    
finally: 
    if conexion.is_connected():
        conexion.close() #Se cierra la conexion a la BD
        print("La conexión ha finalizado.") 
        
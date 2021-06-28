""" Para hacer una lectura de datos usamos la sentencia SELECT propia de SQL.
    1. necsitamos un CURSOR que es un objeto relacionado con las DB y actua omo un nexo 
    para poder hacer lectura de datos y hacer inserciones, actualizaciones y eliminaciones 
                    CURSOR = CONEXION.CURSOR()
    Seguid a esto, ejecutamos un CURSOR.EXECUTE() la cual nos permitira ejecutar una sentencia
    SQL, dentro del parentesis hacemos una sentecia SELECT entre comillas por ser STR seguido de
    la función DATABASE() la cual nos devuelve  el nombre de la DB 
                    CURSOR.EXECUTE("SELECT database();")
    este resultado lo alojamos en una variable a la cual le asignamos el CURSOR.FETCHONE() esta 
    función nos devuelve un registro
    Para hacer una consulta de ua TABLE en general usamos el cursor.execute con la sentencia
    "SELECT * FROM #el nombre de la tabla#" la cual nos permite hacer una lectura delo datos de 
    dicha TABLE.
    Como la tabla tiene varios registro,creamos una variable y le asignamos el objeto CURSOR con la
    función FETCHALL() para leerlos todos en una estructura enendible para PYTHON
    Con una estructura FOR asignamos u nombre IN la vriable anterior para que alvergue cada una de las
    filas obtenidas.
    Con un PRINT podemos mostar los datos obtenidos teniendo en cuenta que la variable creada en el 
    FOR va a copnvertir los datos en una espcie de LISTA por tanto para aceder a ellos tener 
    presente el tratarlos como tal; accediendo a cada posición de ellos por medio de VARIABLE[: :]
    Paraoberla cantidad de registros de una tabla usamos CURSOR.ROWCOUNT
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
        cursor.execute("SELECT database();")
        registro = cursor.fetchone()
        print("Conectado a:", registro)
        cursor.execute("SELECT * FROM usuarios")
        resultado = cursor.fetchall()
        for fila in resultado:
            print(fila[0],fila[1],fila[2],fila[3],fila[4])
        print("Total de registros: ", cursor.rowcount)
            
except Error as ex:
    print("Error en la conexion.", ex)
    
finally: 
    if conexion.is_connected():
        conexion.close() #Se cierra la conexion a la BD
        print("La conexión ha finalizado.") 
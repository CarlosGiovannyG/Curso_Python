from logging import info


# ********************** CONEXION A MYSQL ***************************
# Para poder instalar la libreria que vamos a usar en esta conexión debemos saber cual es el 
# interprete de Python instalado, para esto desde el explorador de archivos de mi pc vamos a esta
# direccion C:\Users/nombre Computador\AppData\Local\Programs\Python\Python39\ que es donde 
# se encuentra instalado Python. Abrimos desde esa carpeta el Power Shell y digitamos el siguiente
# comando * python -m pip install --upgrade pip setuptools wheel * cuando haya instalado o actaulizado
# digitamos el siguiente comando para intalar el cnecto de MYSQL para Pyton
# * pip install mysql-connector-python * Con estos pasos ya tenemos todo listo para conectarnos a la
# base de datos. Nodemos activar nuestra XAMPP

# Para conectarnos a una DB debemos importa el MYSQL.CONECCTOR que es la libreria que es  
# nos permite hacerlo

# De MYSQL.CONECCTOR importamos el modulo ERROR para poder hacer uso del TRY-ERROR

# Tambien debemos importar de LOGGING el metodo INFO para tener informacion del servidor. 

# Para poder controlar las exepsiones creamos una estructura TRY-EXCEP controlando el ERROR de 
# no conexión. 
# Ahora dentro del TRY creamos una variable CONEXION con la función CONNECT para indicar los 
# paramteros de conexión a la DB 

# Usamos la función IS_CONNECTED con un condional IF para validar si la conexion fue exitosa a la DB.
# Con el EXCEP podemos mostrar en un print si hubo algún error. 
# Con una variable INFOSERVER y usando la función GET_SERVER_INFO podemos obtener la información
# precisa del servidor
# Tambien debemos tener muy presente que toda conexion debe ser finalizada, y esto lo hacemos con
# un FINALLY y una condicional IF y la función CONEXION.CLOSED la cual cerrará la conexion

from logging import info
import mysql.connector
from mysql.connector import Error
try: 
    conexion = mysql.connector.connect(
        host = 'localhost',
        port = 3306,
        user = 'root',
        password = '',
        db = 'universidad'                
    )

    if conexion.is_connected():
        print("Conexion exitosa.")
        infoServer = conexion.get_server_info()
        print("infoServer:", infoServer)
except Error as ex:
    print("Error en la conexion.", ex)
    
finally: 
    if conexion.is_connected():
        conexion.close() #Se cierra la conexion a la BD
        print("La conexión ha finalizado.")
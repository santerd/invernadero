import pyodbc
import json

# Parámetros de conexión
server = 'projectgreenhouse.database.windows.net'
database = 'greenhouse_database'
username = 'santiago'
password = 'Biyin123'
driver= '{ODBC Driver 18 for SQL Server}'  # Asegúrate de tener el controlador correcto instalado

# Crear la cadena de conexión
connection_string = f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}"

try:
    # Establecer la conexión
    conn = pyodbc.connect(connection_string)
    print("Conexión exitosa a la base de datos en Azure SQL Database")
    
    # Crear un cursor
    cursor = conn.cursor()
        
    # Crea la consulta SQL de visualizacion
    query = f"SELECT TOP (1000) * FROM condiciones"
    
    # Ejecutar la sentencia SQL para crear la tabla
    cursor.execute(query)
    
    # Recuperar los resultados de la consulta
    rows = cursor.fetchall()
    
    # Mostrar los resultados
    for row in rows:
        print(row)  # Esto mostrará cada fila de resultados en la salida

    # Cerrar la conexión
    cursor.close()
    conn.close()

except pyodbc.Error as e:
    print(f"Error de conexión a la base de datos: {str(e)}")

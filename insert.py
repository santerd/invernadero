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

# Abre el archivo JSON y carga los datos
with open('datos_invernadero.json', 'r') as json_file:
    data = json.load(json_file)

try:
    # Establecer la conexión
    conn = pyodbc.connect(connection_string)
    print("Conexión exitosa a la base de datos en Azure SQL Database")
    
    # Crear un cursor
    cursor = conn.cursor()
    
    # Itera a través de los datos y crea una consulta SQL para cada registro
    for record in data:
        dia = record['Dia']
        temp_registrada = record['Temperatura Registrada']
        temp = record['Temperatura']
        humedad_registrada = record['Humedad Registrada']
        humedad = record['Humedad']
        
        # Calcula la fecha combinando "10/2023" con el número del campo "Dia"
        fecha = f"2023-10-{dia:02}"
        
        # Crea la consulta SQL de inserción
        query = f"INSERT INTO condiciones (Fecha, TemperaturaRegistrada, Temperatura, HumedadRegistrada, Humedad) VALUES ('{fecha}', {temp_registrada}, {temp}, {humedad_registrada}, {humedad})"
    
        # Ejecutar la sentencia SQL para crear la tabla
        cursor.execute(query)
    
    # Guarda los cambios en la base de datos
    conn.commit()

    # Cerrar la conexión
    cursor.close()
    conn.close()

except pyodbc.Error as e:
    print(f"Error de conexión a la base de datos: {str(e)}")

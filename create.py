import pyodbc

# Parámetros de conexión
server = 'projectgreenhouse.database.windows.net'
database = 'greenhouse_database'
username = 'santiago'
password = 'Biyin123'
driver= '{ODBC Driver 18 for SQL Server}'  # Asegúrate de tener el controlador correcto instalado

# Crear la cadena de conexión
connection_string = f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}"

# Sentencia SQL para crear la tabla
codesql = """
CREATE TABLE condiciones (
    id INT IDENTITY(1,1) PRIMARY KEY,
    Fecha DATE,
    TemperaturaRegistrada FLOAT,
    Temperatura FLOAT,
    HumedadRegistrada FLOAT,
    Humedad FLOAT
)
"""

try:
    # Establecer la conexión
    conn = pyodbc.connect(connection_string)
    print("Conexión exitosa a la base de datos en Azure SQL Database")
    
    # Crear un cursor
    cursor = conn.cursor()
    
    # Ejecutar la sentencia SQL para crear la tabla
    cursor.execute(codesql)
    conn.commit()

    print("Tabla creada con éxito.")

    # Cerrar la conexión
    cursor.close()
    conn.close()

except pyodbc.Error as e:
    print(f"Error de conexión a la base de datos: {str(e)}")

import random
import numpy as np
import time

class Chile:
    def __init__(self):
        self.vida = 40

class Invernadero:
    def __init__(self, filas, columnas, temperatura, humedad, materiales, tamano):
        self.filas = filas
        self.columnas = columnas
        self.temperatura = temperatura
        self.humedad = humedad
        self.materiales = materiales
        self.tamano = tamano
        self.invernadero = [[Chile() for _ in range(columnas)] for _ in range(filas)]
        self.hora = 6  # Comienza antes del día

    def mostrar_invernadero(self):
        for fila in self.invernadero:
            for chile in fila:
                if chile.vida > 15:
                    print('🌱', end=' ')
                else:
                    print('🌶️', end=' ')
            print()
        if 7 <= self.hora <= 19:
            print("☀️ Día")
        else:
            print("🌙 Noche")
        print(f"Hora: {self.hora}:00")
        print(f"Temperatura: {self.temperatura}°C")
        print(f"Humedad: {self.humedad}%")
        print(f"Materiales: {', '.join(self.materiales)}")
        print(f"Tamaño: {self.tamano} m²")

    def crecimiento_chiles(self):
        new_invernadero = [[Chile() for _ in range(self.columnas)] for _ in range(self.filas)]
        for i in range(self.filas):
            for j in range(self.columnas):
                chile = self.invernadero[i][j]
                if (7 <= self.hora <= 19) and (25 <= self.temperatura <= 30) and (50 <= self.humedad <= 70):
                    if random.random() < 0.3:
                        new_invernadero[i][j] = chile
                elif (self.hora < 7 or self.hora > 19) and (15 <= self.temperatura <= 20) and (50 <= self.humedad <= 70):
                    if random.random() < 0.3:
                        new_invernadero[i][j] = chile
                else:
                    # Penalizar chiles con menos vida si las condiciones no son adecuadas
                    chile.vida -= 1
                    new_invernadero[i][j] = chile
        return new_invernadero

    def avanzar_hora(self):
        self.hora = (self.hora + 1) % 24

    def simulacion_invernadero(self, horas):
        for i in range(horas):
            self.avanzar_hora()
            if self.hora == 0:
                print(f"Día {i//24 + 1}")
            print(f"Hora {self.hora}:00:")
            self.temperatura = random.uniform(15, 30)  # Temperatura aleatoria
            self.humedad = random.uniform(30, 80)    # Humedad aleatoria
            self.mostrar_invernadero()
            self.invernadero = self.crecimiento_chiles()
            time.sleep(1)
            print("\n" + "-" * 20 + "\n")

    def germinacion(self):
        for i in range(self.filas):
            for j in range(self.columnas):
                chile = self.invernadero[i][j]
                if chile.vida > 15:
                    chile.vida = 100  # Establecer la vida a un valor alto para indicar que germinó

# Parámetros del invernadero
temperatura_quintana_roo = 28  # Temperatura promedio en Quintana Roo
humedad_quintana_roo = 70  # Humedad promedio en Quintana Roo
materiales_invernadero = ["Vidrio", "Acero", "Madera"]
tamano_invernadero = 100  # Tamaño en metros cuadrados

# Crear un invernadero en Quintana Roo
invernadero_quintana_roo = Invernadero(5, 5, temperatura_quintana_roo, humedad_quintana_roo, materiales_invernadero, tamano_invernadero)

# Simular el ciclo día-noche con crecimiento de chiles
invernadero_quintana_roo.simulacion_invernadero(72)

# Realizar la germinación
invernadero_quintana_roo.germinacion()

# Imprimir resultados de la germinación
print("\nResultados de la germinación:")
invernadero_quintana_roo.mostrar_invernadero()

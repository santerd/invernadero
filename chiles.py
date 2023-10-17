import random
import numpy as np
import time

class Invernadero:
    def __init__(self, filas, columnas, temperatura, humedad, materiales, tamano):
        self.filas = filas
        self.columnas = columnas
        self.temperatura = temperatura
        self.humedad = humedad
        self.materiales = materiales
        self.tamano = tamano
        self.invernadero = np.zeros((filas, columnas), dtype=int)
        self.hora = 6  # Comienza antes del día

    def mostrar_invernadero(self):
        # Mostrar Dia o Noche y Hora
        if 7 <= self.hora <= 19:
            print("☀️ Día")
        else:
            print("🌙 Noche")
        print(f"Hora: {self.hora}:00")

        # Mostrar Invernadero
        for fila in self.invernadero:
            for celda in fila:
                if celda == 0:
                    print('🌱', end=' ')
                elif celda == 1:
                    print('🌶️', end=' ')
            print()

        # Mostrar Parametros
        print(f"Temperatura: {self.temperatura:.2f}°C")
        print(f"Humedad: {self.humedad:.2f}%")
        print(f"Materiales: {', '.join(self.materiales)}")
        print(f"Tamaño: {self.tamano} m²")

    def crecimiento_chiles(self):
        new_invernadero = np.copy(self.invernadero)

        for i in range(self.filas):
            for j in range(self.columnas):
                if self.invernadero[i][j] == 0:  # Si no hay chile en la celda
                    if (7 <= self.hora <= 19 and 25 <= self.temperatura <= 30 and 50 <= self.humedad <= 70) or (0 <= self.hora < 7 and 15 <= self.temperatura <= 20 and 50 <= self.humedad <= 70):
                        # Hay condiciones de temperatura, humedad y tiempo para germinar
                        if random.random() < 0.2:  # Probabilidad de germinación
                            new_invernadero[i][j] = 1  # Germinar chile
        return new_invernadero

    def avanzar_hora(self):
        self.hora = (self.hora + 1) % 24

    def simulacion_invernadero(self, horas):
        for i in range(horas):
            self.avanzar_hora()
            if self.hora == 7:
                print(f"Día {i // 24 + 1}")
            self.temperatura = random.uniform(15, 30)  # Temperatura aleatoria
            self.humedad = random.uniform(30, 80)  # Humedad aleatoria
            self.mostrar_invernadero()
            self.invernadero = self.crecimiento_chiles()
            time.sleep(1)
            print("\n" + "-" * 20 + "\n")

# Ejemplo de uso
# Invernadero (filas, columnas, temperatura, humedad, materiales, tamano)
invernadero = Invernadero(5, 5, 28, 70, ["Suelo", "Agua", "Abono"], 25)
invernadero.simulacion_invernadero(48)  # Simula dos días (48 horas)

import random
import time
from SistemaSensoresActuadores import SensorTemperatura, ActuadorVentilacion, ActuadorIluminacion
from SistemaSensoresActuadores import SensorHumedad, ActuadorRiego

class Invernadero:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.invernadero = [[None for _ in range(columnas)] for _ in range(filas)]
        self.condiciones_ambientales = {'temperatura': 0, 'humedad': 0}
        self.actuador_riego = ActuadorRiego()
        self.actuador_ventilacion = ActuadorVentilacion()
        self.actuador_iluminacion = ActuadorIluminacion()
        self.sensorT = SensorTemperatura(self.actuador_ventilacion, self.actuador_iluminacion)
        self.sensorH = SensorHumedad(self.actuador_riego)

    def establecer_condiciones_ambientales(self):
        self.condiciones_ambientales['temperatura'] = round(random.uniform(15, 30), 2)
        self.condiciones_ambientales['humedad'] = round(random.uniform(40, 80), 2)

    def mostrar_condiciones_ambientales(self, dia):
        print(f"Día: {dia}")

        # Se guarda la temperatura registrada y si es necesario se activan los actuadores
        TempReg = self.condiciones_ambientales['temperatura']
        print(f"Temperatura Registrada: {TempReg}°C")
        resultado = self.sensorT.detectarTemperatura(TempReg)
        self.condiciones_ambientales['temperatura'] = resultado

        # Se guarda la humedad y si es necesario se activan los actuadores
        HumReg = self.condiciones_ambientales['humedad']
        print(f"Humedad Registrada: {HumReg}%")
        resultado2 = self.sensorH.detectarHumedad(HumReg)
        self.condiciones_ambientales['humedad'] = resultado2

        print(f"Temperatura: {self.condiciones_ambientales['temperatura']}°C")
        print(f"Humedad: {self.condiciones_ambientales['humedad']}%")

    def germinar_chiles(self):
        for fila in range(self.filas):
            for col in range(self.columnas):
                chile = self.invernadero[fila][col]
                if chile and 25 <= self.condiciones_ambientales['temperatura'] <= 30 and 50 <= self.condiciones_ambientales['humedad'] <= 70:
                    chile.vida += 2

    def mostrar_invernadero(self):
        for fila in self.invernadero:
            for chile in fila:
                if chile is None:
                    print("⬜", end=' ')
                elif chile.vida <= 15:
                    print("🌱", end=' ')
                elif chile.vida > 15:
                    print("🌶️", end=' ')
            print()
        print("\n" + "-" * 20 + "\n")
        
    def plantar_chile(self, fila, columna):
        self.invernadero[fila][columna] = Chile()

class Chile:
    def __init__(self):
        self.vida = 0

def main():
    filas = 5
    columnas = 5
    invernadero = Invernadero(filas, columnas)
    
    for mes in range(1):
        print(f"Mes: {mes + 1}")

        for dia in range(1, 30):
            
            # Plantar 3 chiles
            for _ in range(3):
                fila = random.randint(0, filas - 1)
                col = random.randint(0, columnas - 1)
                if invernadero.invernadero[fila][col] is None:
                    invernadero.invernadero[fila][col] = Chile()
            
            # Se calculan las condiciones del invernadero
            invernadero.establecer_condiciones_ambientales()

            # Muestra el invernadero
            invernadero.mostrar_condiciones_ambientales(dia)

            invernadero.germinar_chiles()
            invernadero.mostrar_invernadero()
            time.sleep(1)  # Simular un día en 1 segundo

if __name__ == "__main__":
    main()

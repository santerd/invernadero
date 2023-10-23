import random
import time
from SistemaSensoresActuadores import SensorTemperatura, ActuadorRiego, ActuadorVentilacion, ActuadorIluminacion


class Invernadero:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.invernadero = [[None for _ in range(columnas)] for _ in range(filas)]
        self.condiciones_ambientales = {'temperatura': 0, 'humedad': 0}

    def establecer_condiciones_ambientales(self):
        self.condiciones_ambientales['temperatura'] = random.uniform(15, 30)
        self.condiciones_ambientales['humedad'] = random.uniform(40, 80)

    def mostrar_condiciones_ambientales(self, hora):
        if 7 <= hora <= 19:
            momento = "Día ☀️ "
        else:
            momento = "Noche 🌙 "
        print(f"{momento} Hora {hora}:")
        print(f"Temperatura: {self.condiciones_ambientales['temperatura']:.2f}°C")
        print(f"Humedad: {self.condiciones_ambientales['humedad']:.2f}%")

    def germinar_chiles(self):
        for fila in range(self.filas):
            for col in range(self.columnas):
                if self.invernadero[fila][col] is not None:
                    chile = self.invernadero[fila][col]
                    if 7 <= chile.hora <= 19 and 25 <= self.condiciones_ambientales['temperatura'] <= 30:
                        if 50 <= self.condiciones_ambientales['humedad'] <= 70:
                            chile.vida += 2
                    elif 1 <= chile.hora <= 6 or 20 <= chile.hora <= 24:
                        if 15 <= self.condiciones_ambientales['temperatura'] <= 20:
                            if 50 <= self.condiciones_ambientales['humedad'] <= 70:
                                chile.vida += 2

    def mostrar_invernadero(self):
        for fila in self.invernadero:
            for chile in fila:
                if chile is None:
                    print("⬜", end=' ')
                elif chile.vida <= 15:
                    print("🌱", end=' ')
                else:
                    print("🌶️", end=' ')
            print()
        print("\n" + "-" * 20 + "\n")

class Chile:
    def __init__(self, hora):
        self.hora = hora
        self.vida = 0

def main():
    filas = 5
    columnas = 5
    invernadero = Invernadero(filas, columnas)
    
    actuador_riego = ActuadorRiego()  # Instancia del actuador de riego
    actuador_ventilacion = ActuadorVentilacion()  # Instancia del actuador de ventilación
    actuador_iluminacion = ActuadorIluminacion()  # Instancia del actuador de iluminación
    sensor = SensorTemperatura(None, actuador_riego, actuador_ventilacion, actuador_iluminacion)
    
    for dia in range(1):
        print(f"Día {dia + 1}:")

        for hora in range(1, 25):
            invernadero.establecer_condiciones_ambientales()
            Tp = invernadero.condiciones_ambientales['temperatura']
            print("La temperatura actual es: ", Tp)
            resultado = sensor.detectarTemperatura(hora, Tp)
            print("La temperatura nueva es: ", resultado)
            invernadero.condiciones_ambientales['temperatura'] = resultado
            invernadero.mostrar_condiciones_ambientales(hora)
            # Generar chiles en 3 ubicaciones aleatorias
            for _ in range(3):
                fila = random.randint(0, filas - 1)
                col = random.randint(0, columnas - 1)
                if invernadero.invernadero[fila][col] is None:
                    invernadero.invernadero[fila][col] = Chile(hora)

            invernadero.germinar_chiles()
            invernadero.mostrar_invernadero()

            time.sleep(1)  # Simular una hora en 1 segundo

if __name__ == "__main__":
    main()

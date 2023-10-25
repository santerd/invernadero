import random

class ActuadorRiego:
    def activarse(self, señal, humedad):
        if señal == 1:
            humedad = round(random.uniform(50, 70), 2)
            return humedad
        else:
            pass

class ActuadorVentilacion:
    def activarse(self, señal, temp):
        if señal == 1:
            temp = round(random.uniform(25, 30), 2)
            return temp
        else:
            pass

class ActuadorIluminacion:
    def activarse(self, señal, temp):
        if señal == 1:
            temp = round(random.uniform(25, 30), 2)
            return temp
        else:
            pass

class SensorTemperatura:
    def __init__(self, actuador_ventilacion, actuador_iluminacion):
        self.actuador_ventilacion = actuador_ventilacion
        self.actuador_iluminacion = actuador_iluminacion

    def detectarTemperatura(self, tempt):
        if 25 <= tempt <= 30:
            self.actuador_ventilacion.activarse(0, tempt)
            self.actuador_iluminacion.activarse(0, tempt)
        elif tempt > 30:
            tempt = self.actuador_ventilacion.activarse(1, tempt)
            self.actuador_iluminacion.activarse(0, tempt)
        elif tempt < 25:
            self.actuador_ventilacion.activarse(0, tempt)
            tempt = self.actuador_iluminacion.activarse(1, tempt)
        return tempt
    
class SensorHumedad:
    def __init__(self, actuador_riego):
        self.actuador_riego = actuador_riego

    def detectarHumedad(self, humedad):
        if 50 <= humedad <= 70:
            self.actuador_riego.activarse(0, humedad)
        else:
            humedad = self.actuador_riego.activarse(1, humedad)
        return humedad
import random

class ActuadorRiego:
    def activarse(self, señal, humedad):
        if señal == 1:
            humedad = random.uniform(50, 70)
            return humedad
        else:
            pass

class ActuadorVentilacion:
    def activarse(self, señal, hora, temp):
        if señal == 1:
            if 7 <= hora <= 19:
                temp = random.uniform(25, 30)
            else:
                temp = random.uniform(15, 20)
            return temp
        else:
            pass

class ActuadorIluminacion:
    def activarse(self, señal, hora, temp):
        if señal == 1:
            if 7 <= hora <= 19:
                temp = random.uniform(25, 30)
            else:
                temp = random.uniform(15, 20)
            return temp
        else:
            pass

class SensorTemperatura:
    def __init__(self, actuador_ventilacion, actuador_iluminacion):
        self.actuador_ventilacion = actuador_ventilacion
        self.actuador_iluminacion = actuador_iluminacion

    def detectarTemperatura(self, hora, tempt):
        if 7 <= hora <= 19:
            if 25 <= tempt <= 30:
                self.actuador_ventilacion.activarse(0, hora, tempt)
                self.actuador_iluminacion.activarse(0, hora, tempt)
            elif tempt > 30:
                tempt = self.actuador_ventilacion.activarse(1, hora, tempt)
                self.actuador_iluminacion.activarse(0, hora, tempt)
            elif tempt < 25:
                self.actuador_ventilacion.activarse(0, hora, tempt)
                tempt = self.actuador_iluminacion.activarse(1, hora, tempt)
        elif hora < 7 or hora > 19:
            if 15 <= tempt <= 20:
                self.actuador_ventilacion.activarse(0, hora, tempt)
                self.actuador_iluminacion.activarse(0, hora, tempt)
            elif tempt > 20:
                tempt = self.actuador_ventilacion.activarse(1, hora, tempt)
                self.actuador_iluminacion.activarse(0, hora, tempt)
            elif tempt < 15:
                self.actuador_ventilacion.activarse(0, hora, tempt)
                tempt = self.actuador_iluminacion.activarse(1, hora, tempt)
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
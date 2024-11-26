import math

class Angle:
    def __init__(self, angle):
        if angle < 0 or angle > 360:
            raise ValueError
        self.angle = angle

    def __str__(self):
        return str(self.angle) + " degrés"
        
    def ajoute(self, Angle2):
        calcul = self.angle + Angle2.angl
        if calcul > 360:
            self.angle = calcul % 360
        else:
            self.angle = calcul

    def cos(self):
        math.cos(self.angle) * (math.pi / 180)

    def sin(self):
        math.sin(self.angle) * (math.pi / 180)
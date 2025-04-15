import math

class SodaCan:
    def __init__(self, altezza, raggiobase):
        self.altezza = altezza
        self.raggiobase = raggiobase

    def getSurfaceArea(self):
        area_basi = 2 * math.pi * self.raggiobase**2
        area_laterale = 2 * math.pi * self.raggiobase * self.altezza
        return area_basi + area_laterale

    def getVolume(self):
        return math.pi * self.raggiobase**2 * self.altezza

# Creazione dell'istanza e chiamata dei metodi
lattina = SodaCan(10, 5)  
print("Superficie totale:", lattina.getSurfaceArea())
print("Volume:", lattina.getVolume())
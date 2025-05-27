from Tier import Tier

class Vogel(Tier):
    def __init__(self, name, alter, gewicht, mikrochip_id, fluegelspannweite):
        super().__init__(name, alter, gewicht, mikrochip_id)
        self.fluegelspannweite = fluegelspannweite
    
    def zwitschern(self):
        print("fiep!")

    def fliegen(self):
        print("Der Vogel fliegt davon.")
from Tier import Tier

class Katze(Tier):
    def __init__(self, name, alter, gewicht, mikrochip_id, lieblingsspielzeug):
        super().__init__(name, alter, gewicht, mikrochip_id)
        self.lieblingsspielzeug = lieblingsspielzeug
    
    def miau(self):
        print("miau!")
    
    def klettern(self):
        print("Die Katze klettert auf den Baum.")
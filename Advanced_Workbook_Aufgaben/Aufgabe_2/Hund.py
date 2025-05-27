from Tier import Tier

class Hund(Tier):
    def __init__(self, name, alter, gewicht, mikrochip_id, gassi_gehen_zeit):
        super().__init__(name, alter, gewicht, mikrochip_id)
        self.gassi_gehen_zeit = gassi_gehen_zeit

    def bellen(self):
        print("wuff!")
    
    def gassi_gehen(self):
        print("Der Hund geht Gassi.")
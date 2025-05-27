from abc import ABC #Abstrakte Klasse, keine Instanz von Tier

class Tier(ABC):
    def __init__(self, name, alter, gewicht, mikrochip_id):
        self.name = name
        self.alter = alter
        self.gewicht = gewicht
        self.mikrochip_id = mikrochip_id


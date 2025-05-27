from Hund import Hund
from Katze import Katze
from Vogel import Vogel

class Tierheim:
    pass

if __name__ == "__main__":
    hund1 = Hund("bello", 4, 13, 34532, 50)
    hund1.bellen()
    hund1.gassi_gehen()
    katze1 = Katze("kitty", 5, 8, 93859, "feder")
    katze1.miau()
    katze1.klettern()
    vogel1 = Vogel("birdy", 2, 10, 38479, 45)
    vogel1.zwitschern()
    vogel1.fliegen()

    #wuff!
    #Der Hund geht Gassi.
    #miau!
    #Die Katze klettert auf den Baum.
    #fiep!
    #Der Vogel fliegt davon. 	

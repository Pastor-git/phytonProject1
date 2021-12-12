
# Tworzenie klasy
# Klasa jest SZABLONEM
class Czlowiek:
    gatunek = "homo sapiens"
    def __init__(self, imie):
        print("Tworzę człowieka o imieniu", imie)
        self.imie = "Adam"
        #adam.imie = "Adam"

    def powiedz_hej(self):
        print("No hej!")

# Tworzę OBIEKT
# INSTANCJĘ klasy Człowiek
adam = Czlowiek("Adam") # self = adam
ewa = Czlowiek("Ewa") # self = ewa

print("Adam ma na imię", adam.imie)

# print(adam.gatunek)
# print(ewa.gatunek)
#
# adam.powiedz_hej()
# ewa.powiedz_hej()
#
# print(dir(Czlowiek))
# print(dir(adam))
# print(dir(ewa))
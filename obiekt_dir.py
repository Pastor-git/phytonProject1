# a = 5
# print(dir(a))
# print(type(a))
# Zawsze CAmelcase
# w python wszystko jesto biektem
class Czlowiek:
    gatunek = "homo sapiens"
    def __init__(self, imie):
        print("metoda inicjalizacyjna działa")
        print("tworzę człowieka o imieniu: ", imie)
        self.imie=imie
    def powiedz_hej(self):
        print("hej")

print(dir(Czlowiek))
print(type(Czlowiek))
Czlowiek("Kapitan Gender")
adam = Czlowiek("Adam")
print(dir(adam))
print(type(adam))
print(adam.gatunek)
ewa = Czlowiek("Ewa")
ewa.powiedz_hej()
adam.powiedz_hej()


print(adam.imie, ewa.imie)
print(type(adam.powiedz_hej()))


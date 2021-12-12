# ZAKRES WIDOCZNOŚCI ZMIENNYCH
a = 5

def funkcja():
    a = 12
    b = 6
    print("Wartość a rowna się", a)
    print("Wartość b rowna się", b)

funkcja()
print(a)
print(b) # BŁĄD - b nie istnieje globalnie

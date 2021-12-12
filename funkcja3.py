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

##########
lista = [1, 2, 3]
a = 5

def zamien(lista):
    lista[0] = 0
    return lista

def zamien2(a):
    a = 0
    return a

zamien(lista)
zamien2(a)

print("a=", a)
print("lista=", lista)

# pary klucz wartość
# Tworzenie słownika
# klucz : wartość
en_to_es = {'cat' : 'gato', 'dog' : 'perro'}
# Pobranie elementu ze słownika
print(en_to_es['cat'])
# Dodanie nieistniejącego elementu
en_to_es['mouse'] = 'el rato'

# print(dir(dict))
# Wyświetl wartośći
print(en_to_es.values())
# Wyświetl klucze
print(en_to_es.keys())
# print(type(en_to_es))

# Wyświetl elementy
print(en_to_es.items())

# "Bezpieczne' odszukanie wartości
# Nie rzuci wyjątku, gdy go nie znajdzie
print(en_to_es.get('mouse'))

for key in en_to_es:
    print(key)

print("Itemy: ", en_to_es.items())
for item in en_to_es.items():
    print("element", item, "typu", type(item))

# Iterowanie po parach klucz : wartość
for (key, value) in en_to_es.items():
    print(key, "->", value)

# Czy jest klucz 'cat' w słowniku
print('cat' not in en_to_es)

print("Ile jest elementów w słowniku?", len(en_to_es))
lista_ocen = input("Podaj oceny oddzielone przecinkiem: ")
print(lista_ocen)
suma = 0

lista_ocen = lista_ocen.split(',')
for ocena in lista_ocen:
    suma += float(ocena)
    print(ocena)

print("średnia ocen to: ", suma/float(len(lista_ocen)))



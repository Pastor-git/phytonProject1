lista1 = [1,'hello',1.5,['a','b','c']]

print("Lista zawiera:")
print("element:", lista1[0],"typu: ", type(lista1[0]))
print("element:", lista1[1],"typu: ", type(lista1[1]))
print("element:", lista1[2],"typu: ", type(lista1[2]))
print("element:", lista1[3],"typu: ", type(lista1[3]))

print("Lista zawiera po raz drugi:")
for element in lista1:
    print("Iteracja")
    print(element, type(element))


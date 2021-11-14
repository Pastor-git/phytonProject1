
pizza1 = input("podaj po przecinku średnice oraz cenę pizzy1: ")
pizza2 = input("podaj po przecinku średnice oraz cenę pizzy2: ")

pizza1 = pizza1.split(',')
pizza2 = pizza2.split(',')

pole1 = float(pizza1[0]/2)*float(pizza1[0]/2)*3.14
pole2 = float(pizza2[0]/2)*float(pizza2[0]/2)*3.14

print (pole1, " ", pole2)
# rentownosc1 =
# rentownosc2 =
#
# if float(pizza1[1])/float(pizza1[0])/2 > float(pizza2[1])/float(pizza2[0])/2:
#     print("pizza2 jest tańsza o: ", float(pizza1[1])/float(pizza1[0])/2 - float(pizza2[1])/float(pizza2[0])/2)
# elif float(pizza1[1])/float(pizza1[0])/2 < float(pizza2[1])/float(pizza2[0])/2:
#     print("pizza2 jest tańsza o: ", float(pizza1[1]) / float(pizza1[0]) / 2 - float(pizza2[1]) / float(pizza2[0]) / 2)
# else:
#     print("nie jest jak myślisz")
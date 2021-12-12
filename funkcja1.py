word = str(input("Wpisz słowo: "))
word = word.replace(" ", "")
word = word.lower()
reverse_word = (word[::-1])
print (reverse_word)
if reverse_word == word:
    print("To jest palindrom")
else:
    print(f'{word} nie jest palindromem')


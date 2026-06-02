frase = input('Digite uma frase: ')

fraseseparad = []
palavra = ''

for letra in frase:
    if letra != ' ':
        palavra += letra
    else:
        fraseseparad.append(palavra)
        palavra = ''

fraseseparad.append(palavra)

print(fraseseparad)
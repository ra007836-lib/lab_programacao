# 3. O Contador de Vogais

# Problema: Peça para o usuário digitar uma palavra.
# O programa deve percorrer a string caractere por caractere
# e contar quantas vogais (a, e, i, o, u) existem na palavra

palavra = input("Digite uma palavra: ").lower()

contador = 0

for letra in palavra:
    if letra in 'aeiou':
        contador += 1

print(f'a palavra "{palavra}" tem {contador} vogais')
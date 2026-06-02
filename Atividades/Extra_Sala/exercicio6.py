# 6. Inversão Espelhada de Vetor

# Problema: Faça um programa que leia 5 nomes e os armazene em uma lista.
# Em seguida, o programa deve criar uma segunda lista contendo os mesmos nomes,
# mas na ordem inversa (o último nome lido deve ser o primeiro da nova lista).
# Imprima ambas.

listainvertida = []

for i in range(5):
    nome = input(f'Nome {i + 1}: ')
    listainvertida.append(nome)

listanormal = listainvertida
listainvertida.reverse()

print('Lista normal:', listanormal)
print('Lista invertida:', listainvertida)
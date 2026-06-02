# 5. O Localizador de Duplicatas Problema: 
# Preencha uma lista com 6 números inteiros informados pelo usuário.
# Depois, peça para ele digitar um número X.
# O programa deve usar métodos de lista para informar quantas vezes X aparece na lista
# e, se aparecer, qual é o indice da primeira ocorrência.

lista = []

for ind in range(1,7):
    lista.append(int(input(f'Numero {ind}: -> ')))

valorachar = int(input('QUal valor vc quer olhar -> '))

print(lista.count(valorachar))
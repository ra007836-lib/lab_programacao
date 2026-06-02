vetor = []

print('-' * 60)
print('DIGITE OS VALORES')
print('-' * 60)

for i in range(5):
    numero = int(input(f'Digite o {i+1}º valor: '))
    vetor.append(numero)

print('-' * 60)
print('PROCURE UM VALOR NO VETOR')
print('-' * 60)

while True:
    valor = int(input('Digite o valor que deseja procurar: '))

    if valor in vetor:
        posicao = vetor.index(valor)
        print(f'O valor {valor} foi encontrado na posição {posicao}.')
        print('-' * 60)
        break
    else:
        print('Valor não encontrado. Tente novamente!')
        print('-' * 60)
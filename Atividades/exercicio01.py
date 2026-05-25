vetor = []
repetidos = 0
sem_repeticao = []

print('-' * 60)
print('DIGITE OS VALORES DO VETOR')
print('-' * 60)

for i in range(10):
    numero = int(input(f'Digite o {i+1}º valor: '))
    vetor.append(numero)

print('-' * 60)
print('VERIFICANDO REPETIÇÕES...')
print('-' * 60)

for numero in vetor:
    if numero not in sem_repeticao:
        sem_repeticao.append(numero)
    else:
        repetidos += 1
        print(f'O valor {numero} está repetido.')

print('-' * 60)
print(f'Total de valores repetidos: {repetidos}')
print('-' * 60)

print('Vetor sem repetição:')
for numero in sem_repeticao:
    print(numero)

print('-' * 60)
print(f'Temos {len(sem_repeticao)} valores diferentes.')
print('-' * 60)
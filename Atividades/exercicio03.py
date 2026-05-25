import random

dado = [1,2, 3, 4,5, 6]
jogadas = []
cont_6 = 0

print('-' * 60)
print('JOGADAS DO DADO')
print('-' * 60)

for i in range(50):
    resultado = random.choice(dado)
    jogadas.append(resultado)

    if resultado == 6:
        cont_6 += 1
        print(f'\033[32mJOGADA {i+1}: {resultado} -FACE 6 SAIU {cont_6} VEZ(ES)\033[0m')
    else:
        print(f'JOGADA {i+1}: {resultado}')

print('-' * 60)
print('RESULTADO FINAL')
print('-' * 60)

print(f'A face 6 apareceu {cont_6} vezes em 50 jogadas.')

print('-' * 60)
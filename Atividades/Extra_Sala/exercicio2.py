# 2. O Multiplicador Acumulativo

# Problema: Escreva um programa que peça um número inteiro positivo ao usuário e, utilizando um laço for, 
# calcule e mostre o resultado do produto de todos os números Impares de 1 até o número digitado.

num = int(input('Digite um número: '))
resultado = 1
for i in range(1, num + 1):
    if i % 2 != 0:
        resultado *= i
print(resultado)
# 1. O Validador de Intervalo Problema: 
# Faça um programa que leia um número do teclado e 
# verifique se ele está dentro do intervalo entre 10 e 50 (inclusive).
# Se estiver, exiba "Dado Válido".
# Caso contrário, exiba "Dado Inválido".
# Atente-se para que o programa repita essa validação
# até que o usuário digite o número 0 para sair.

while True:
    num = int(input('Digite um número: '))
    if num == 0:
        break
    elif num in range(10, 51):
        print('Dado Válido')
    else:
        print('Dado Inválido')
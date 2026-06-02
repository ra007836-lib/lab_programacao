# 4. O Filtro de Notas Problema: 
# Crie um programa que preencha uma lista com as notas de 5 numalunos
# (valores lidos do teclado).
# Em seguida, o programa deve remover a menor nota da lista
# utilizando comandos de vetor e exibir as notas restantes na tela.

notas = []

for numaluno in range(1,6):
    notas.append(int(input(f'Nota aluno {numaluno}: -> ')))

notas.remove(min(notas))
print('restou ',notas)
# 9. O Histórico Balancete de Caixa
# Problema: Crie um simulador de fluxo de caixa. 
# O programa deve receber operações financeiras de uma empresa. 
# O usuário digita o valor (positivo para Receita, negativo para Despesa). 
# Cada valor deve ser guardado em um vetor histórico. 
# O programa para quando o usuário digitar 0. 
# No final, limpe todos os valores que foram menores que R$ 5,00 (tanto positivos quanto negativos) 
# usando o comando del ou remove, e mostre o saldo final remanescente.


historico = []

while True:
    valor = float(input("digite um valor (0 para parar): "))
    if valor == 0:
        break
    historico.append(valor)

i = 0

while i < len(historico):
    if historico[i] < 5 and historico[i] > -5:
        del historico[i]
    else:
        i = i + 1

print("saldo final:", sum(historico))
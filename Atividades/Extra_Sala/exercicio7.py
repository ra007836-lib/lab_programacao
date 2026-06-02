pares = []
impares = []

while len(pares) + len(impares) < 10:
    num = int(input('Digite um numero: -> '))

    if num in pares or num in impares:
        print('nummero já digitado, tente outro')
    else:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)



print('pares: ', pares)
print('impares:', impares) 
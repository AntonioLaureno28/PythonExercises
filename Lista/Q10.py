num = [11, 15, 6, 9, 54, 23, 2]

maior = num[0]
menor = num[0]

for numero in num[1:]:
    if numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero
print('Maior:', maior)
print('Maior:', menor)
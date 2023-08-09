palavra = str(input('Digite uma palavra: ')).lower()
print(palavra)
inv = ''
for letra in range(len(palavra)-1, -1, -1):
    inv += palavra[letra]
if palavra == inv:
    print('Palíndromo')
else: 
    print('Não é um palíindromo')
    
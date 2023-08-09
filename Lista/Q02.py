count = 0
soma = 0
while True: 
    num = int(input('Digite um numero: '))
    if num == 0:
        break
    soma = soma + num
    count = count + 1
media = soma / count
print(media)    
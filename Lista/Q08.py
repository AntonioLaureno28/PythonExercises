def segundo(numeros):
    maior = max(numeros[0], numeros[1])
    segundomaior = min(numeros[0], numeros[1])

    for numero in numeros[2:]:
        if numero > maior:
            segundomaior = maior
            maior = numero
        if numero > segundomaior and numero != maior:
            segundomaior = numero
        
    return segundomaior

num = [12, 15, 4, 9, 32, 23, 78]
segundo_maior = segundo(num)
print(segundo_maior)
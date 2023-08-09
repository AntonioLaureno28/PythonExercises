def primo(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i+2) == 0:
            return False
        i = i + 6
    return True

def listaprimos(numero):
    listaprimos = [num for num in numero if primo(num)]
    return listaprimos

listanumeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
primos = listaprimos(listanumeros)
print(primos)

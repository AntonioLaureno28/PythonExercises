def impares(lista):
    impar = [num for num in lista if num % 2 != 0]
    return impar

list = [1,2,3,4,5,6,7,8,9,10]
impar = impares(list)
print(impar)


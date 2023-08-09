def sort(lista):
    ordenar = sorted(lista, key=lambda pessoas: pessoas[0])
    return ordenar

listapessoas = [("Fernando", 22), ("Josias", 25), ("Lorena", 20), ("Márcia", 26), ("Antonio", 21)]
pessoasordenadas = sort(listapessoas)
print(pessoasordenadas)
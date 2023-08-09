def uniao(list1, list2):
    unidos = []
    for num in list1:
        if num not in list2:
            unidos.append(num)
    for num in list2:
        if num not in list1:
            unidos.append(num)
            
    return unidos

lista1 = [1, 2, 3, 4, 5, 6, 10, 11]
lista2 = [7, 8, 9, 10, 11, 12, 6, 4]
juntos = uniao(lista1, lista2)
print(juntos)
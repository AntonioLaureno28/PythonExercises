frutas = ['banana', 'maçã', 'laranja', 'abacaxi']

cincoletras = [fruta for fruta in frutas if len(frutas)]
ultimaletra = [fruta for fruta in frutas if fruta[-1] == 'a']
print('Mais de 5 letras: ', cincoletras)
print('terminado em "a": ', ultimaletra)
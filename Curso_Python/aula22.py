from itertools import zip_longest

capitais = ['Salvador', 'Ubatuba', 'Belo Horizonte']
estados = ['Ba', 'SP', 'MG', 'Rj']

print (list(zip_longest(capitais, estados, fillvalue='Sem cidade ')))
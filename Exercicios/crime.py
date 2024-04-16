crime = []

for i in range(1):
    nome_crime = input('Telefonou para a vítima?(v ou f) ')
    if nome_crime == 'v':
        crime.append(nome_crime)
    
for i in range(1):
    nome_crime = input('Esteve no local do crime?(v ou f) ')
    if nome_crime == 'v':
        crime.append(nome_crime)

for i in range(1):
    nome_crime = input('Mora perto da vítima?(v ou f) ')
    if nome_crime == 'v':
        crime.append(nome_crime)

for i in range(1):
    nome_crime = input('Devia para a vítima?(v ou f) ')
    if nome_crime == 'v':
        crime.append(nome_crime)

for i in range(1):
    nome_crime = input('Já trabalhou com a vítima?(v ou f) ')
    if nome_crime == 'v':    
        crime.append(nome_crime)

if len(crime) == 0:
    print('Inocente')

if len(crime) == 1:
    print('Inocente')

if len(crime) == 2:
    print('Suspeito')

if len(crime) == 3:
    print('Suspeito')

if len(crime) == 4:
    print('Cúmplice')

if len(crime) == 5:
    print('Assasino')
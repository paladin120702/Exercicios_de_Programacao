lista = []

for i in range(10):
    letra = input('Digite uma letra ')
    lista.append(letra)
    
consoantes = []
consoante = 0
for letra in lista:
    if letra in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
        consoante += 1
        consoantes.append(letra)
        
print (f'tem {consoante} consoantes')
print(f'As consoantes são {consoantes}')
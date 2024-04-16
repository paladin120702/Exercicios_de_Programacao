palavra = input('Digite uma palavra ')

if ' ' in palavra:
    print(f'Contem {len(palavra and " ")} espaço(s)')
else:
    print('Não contem espaços ')

vogais = 0
for letra in palavra:
    if letra in 'aeiou':
        vogais += 1
        
print(f'Há {vogais} vogai(s) nestas palavras ')

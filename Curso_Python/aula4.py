nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
if  nome and idade:
    print (f'Meu nome é {nome}')
    print (f'Meu nome invertido é {nome[::-1]}')
    
    if ' ' in nome:
        print ('Meu nome contem espaços')
    else:    
        print ('Meu nome não contem espaços')

    print (f'Meu nome tem {len(nome)} letras')
    print (f'A primeira letra do meu nome é {nome[0]}')
    print (f'A última letra do meu nome é {nome[-1]}')
else:
    print('Desculpe, você deixou campos vazios') 



    




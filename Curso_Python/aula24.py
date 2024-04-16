import os

lista = []

while True:
    print('Escreva algo para sua lista, ou selecione umas das opções abaixo ')
    opção = input('[r]efazer, [d]esfazer, [s]air ou [c]lear ')

    if opção == 'd':
        try:
            ultino_elemento = lista.pop()
        except:
            print('Não há nada para desfazer ')

    elif opção == 'r':
        try:
            lista.append(ultino_elemento)
        except:
            print('Nao ha nada para refazer')
    
    elif opção == 'c':
        os.system('cls')
        continue

    elif opção == 's':
        break

    else:
        lista.append(opção)

    for item in lista:
        print(item)
    
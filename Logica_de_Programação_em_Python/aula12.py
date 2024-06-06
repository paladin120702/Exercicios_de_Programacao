lista = []

while True:
    print('Selecione uma opção ')
    opcao = input('[i]nserir ,  [a]pagar , [l]istar , [s]air')
    if opcao == 'i':
        valor = input('Digite um valor ')
        lista.append(valor)
        for i , valor in enumerate(lista):
            print(i , valor )
    elif opcao == 'a':
        print('Escolha o valor para apagar ')
        indice_str = input('Escolha um indice para apagar ')

        try:
            indice = int(indice_str)
            del lista[indice]
        except IndexError:
            print('use somente números inteiros ')
        except ValueError:
            print('Erro desconhecido ')
        except Exception:
            print('Indice não encontrado ')

    elif opcao == 'l':
        if len(lista) == 0:
            print('Nada para listar ')
        
        for i , valor in enumerate(lista):
                print(i , valor )
    elif opcao == 's':
        break
    else:
        print('Por favor digite uma das letras acima ')
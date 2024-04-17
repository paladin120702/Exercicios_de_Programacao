def calcular_percentual(voto, total_votos):
    return (voto / total_votos) * 100

def gravar_resultados(arquivo, total_votos, resultados):
    with open(arquivo, 'w') as f:
        f.write(f'Foram computados {total_votos} votos.\n\n')
        f.write('sistemas operaionais   Voto   %\n')
        for sistema, voto, percentual in resultados:
            f.write(f'{sistema:3}   {voto:5}   {percentual:.1f}%\n')

def main():
    votos = [0] * 7

    while True:
        try:
            opcoes = (f' 1- Windows Server\n 2- Unix\n 3- Linux\n 4- Netware\n 5- Mac OS\n 6- Outro\n') 
            print (opcoes)
            sistemas = int(input('Qual o melhor sistema operacional: '))
            if sistemas == 0:
                break
            elif sistemas < 1 or sistemas > 6:
                print('Informe um valor entre 1 e 6 ou 0 para sair!')
            else:
                votos[sistemas] += 1
        except ValueError:
            print('Informe um valor válido (número inteiro).')
    
    total_votos = sum(votos)
    resultados = []
    for sistemas, voto in enumerate(votos):
        if sistemas != 0 and voto > 0:
            percentual = calcular_percentual(voto, total_votos)
            resultados.append((sistemas, voto, percentual))
    
    resultados.sort(key=lambda x: x[0])
    
    print('\nResultado da votação:\n')
    print('Sistemas     Votos      %')
    for sistemas, voto, percentual in resultados:
        print(f'{sistemas:3}        {voto:5}        {percentual:.1f}%')
    
    melhor_sistema, votos_melhor, percentual_melhor = max(resultados, key=lambda x: x[1])
    
    print(f'\nO melhor jogador foi o número {melhor_sistema}, com {votos_melhor} votos, correspondendo a {percentual_melhor:.1f}% do total de votos.')

    gravar_resultados('Relatorio.txt', total_votos, resultados)

if __name__ == '__main__':
    main()
def calcular_percentual(votos_jogador, total_votos):
    return (votos_jogador / total_votos) * 100

def gravar_resultados(arquivo, total_votos, resultados):
    with open(arquivo, 'w') as f:
        f.write(f'Foram computados {total_votos} votos.\n\n')
        f.write('Jogador   Votos   %\n')
        for jogador, votos, percentual in resultados:
            f.write(f'{jogador:3}       {votos:5}   {percentual:.1f}%\n')

def main():
    votos = [0] * 24

    while True:
        try:
            jogador = int(input('Número do jogador (0=fim): '))
            if jogador == 0:
                break
            elif jogador < 1 or jogador > 23:
                print('Informe um valor entre 1 e 23 ou 0 para sair!')
            else:
                votos[jogador] += 1
        except ValueError:
            print('Informe um valor válido (número inteiro).')

    total_votos = sum(votos)
    resultados = []

    for jogador, votos_jogador in enumerate(votos):
        if jogador != 0 and votos_jogador > 0:
            percentual = calcular_percentual(votos_jogador, total_votos)
            resultados.append((jogador, votos_jogador, percentual))

    resultados.sort(key=lambda x: x[0])

    print('\nResultado da votação:\n')
    print('Jogador   Votos   %')
    for jogador, votos_jogador, percentual in resultados:
        print(f'{jogador:3}       {votos_jogador:5}   {percentual:.1f}%')

    melhor_jogador, votos_melhor, percentual_melhor = max(resultados, key=lambda x: x[1])

    print(f'\nO melhor jogador foi o número {melhor_jogador}, com {votos_melhor} votos, correspondendo a {percentual_melhor:.1f}% do total de votos.')

    gravar_resultados('resultado_enquete.txt', total_votos, resultados)

if __name__ == '__main__':
    main()
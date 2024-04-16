horario = input('Digite o horário atual utilizando ponto para separar a horá dos minutos no formato 24hs ')

try:
    entrada = float(horario)
    if entrada >= 0 and entrada <= 11.59:
        print('Bom dia ')
    elif entrada >= 12 and entrada <= 18.59:
        print('Boa tarde ')
    elif entrada >= 19 and entrada <= 23.59:
        print ('Boa noite ')
    else:
        print('Não conheço essa hora')
except:
    print('Digite apenas números ')

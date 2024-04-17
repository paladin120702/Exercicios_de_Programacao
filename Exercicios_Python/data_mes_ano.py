def nascimento(parametro, parametro2, parametro3):
    while True:

        entrada1 = int(parametro)
        entrada2 = int(parametro2)
        entrada3 = int(parametro3)  

        if entrada2 == 1:
            print (f'Data de Nascimento: {entrada1}/01/{entrada3}')
            print (f'Você nasceu em {entrada1} de janeiro de {entrada3}')
        elif entrada2 == 2:
            print (f'Data de Nascimento: {entrada1}/02/{entrada3}')
            print (f'Você nasceu em {entrada1} de fevereiro de {entrada3}')
        elif entrada2 == 3:
            print(f'Data de Nascimento: {entrada1}/03/{entrada3}')
            print(f'Você nasceu em {entrada1} de março de {entrada3}')
        elif entrada2 == 4:
            print(f'Data de Nascimento: {entrada1}/04/{entrada3}')
            print(f'Você nasceu em {entrada1} de abril de {entrada3}')
        elif entrada2 == 5:
            print(f'Data de Nascimento: {entrada1}/05/{entrada3}')
            print(f'Você nasceu em {entrada} de maio de {entrada3}')
        elif entrada2 == 6:
            print(f'Data de Nascimento: {entrada1}/06/{entrada3}')
            print(f'Você nasceu em {entrada1} de junho de {entrada3}')
        elif entrada2 == 7:
            print(f'Data de nascimento: {entrada1}/07/{entrada3}')
            print(f'Você nasceu em {entrada1} de julho de {entrada3}')
        elif entrada2 == 8:
            print(f'Data de Nascimento: {entrada1}/08/{entrada3}')
            print(f'Você nasceu em {entrada1} de agosto de {entrada3}')
        elif entrada2 == 9:
            print(f'Data de nascimento: {entrada1}/09/{entrada3}')
            print(f'Você nasceu em {entrada1} de setembro de {entrada3}')
        elif entrada2 == 10:
            print(f'Data de Nascimento: {entrada1}/10/{entrada3}')
            print(f'Você nasceu em {entrada1} de outubro de {entrada3}')
        elif entrada2 == 11:
            print(f'Data de Nascimento: {entrada1}/11/{entrada3}')
            print(f'Você nasceu em {entrada1} de novembro de {entrada3}')
        elif entrada2 == 12:
            print(f'Data de Nascimento: {entrada1}/12/{entrada3}')
            print(f'Você nasceu em {entrada1} de dezembro de {entrada3}')   
        break

while True:
    dia_nascimento = input('Digite dia do seu nascimento ')
    mês_nascimento = input('Digite o mês do seu nascimento ')
    ano_nascimento = input('Digite seu ano de nasciemnto ')
    
    dia = (len(dia_nascimento))
    mês = (len(mês_nascimento))
    ano = (len(ano_nascimento))
    if ano != 4:
        print('Seu dia e mês do seu nascimento tem que ter 2 números e do seu ano 4 números ')
        continue
    if dia and mês != 2:
        print('Seu dia e mês do seu nascimento tem que ter 2 números e do seu ano 4 números ')
        continue
    if int(dia_nascimento) > 31:
        print('Não existe esse dia ')
        continue
    if int(mês_nascimento) > 12:
        print('Não existe esse mês ')
        continue   
    nascimento(dia_nascimento, mês_nascimento, ano_nascimento)
    break
while True:
    cpf = input('Digite o cpf ')
    if cpf in '':
        print('Você não digitou nada, tente novamente ')
        continue
    if cpf in ' ':
        print('Você não pode digitar espaços, tente novamente ')
        continue
    if len(cpf) != 11:
        print('O CPF tem 11 números, tente novamente ')
        continue
    entrada_sequencial = cpf == cpf[0] * len(cpf)
    if entrada_sequencial:
        print('Você não pode digitar dados sequenciais, tente novamente ')
        continue
    #Calculando o primeiro digito do CPF
    mutiplicacao = int(cpf[0]) * 10 + int(cpf[1]) * 9 + int(cpf[2]) * 8 + int(cpf[3]) * 7 + int(cpf[4]) * 6 + int(cpf[5]) * 5 + int(cpf[6]) * 4 + int(cpf[7]) * 3 + int(cpf[8]) * 2
    mutiplicacao2 = mutiplicacao * 10
    mutiplicacao3 = mutiplicacao2 % 11
    Resultado_do_primeiro_digito = mutiplicacao3 if mutiplicacao3 < 9 else 0
    #Calculando o segundo digito do CPF
    soma = int(cpf[0]) * 11 + int(cpf[1]) * 10 + int(cpf[2]) * 9 + int(cpf[3]) * 8 + int(cpf[4]) * 7 + int(cpf[5]) * 6 + int(cpf[6]) * 5 + int(cpf[7]) * 4 + int(cpf[8]) * 3 + Resultado_do_primeiro_digito * 2
    soma2 = soma * 10
    soma3 = soma2 % 11
    Resultado_do_segundo_digito = soma3 if soma3 < 9 else 0
    #Validando CPF
    cpf_gerado_pelo_calculo = f'{cpf[0:9]}{Resultado_do_primeiro_digito}{Resultado_do_segundo_digito}'
    if cpf_gerado_pelo_calculo == cpf:
        print(f'{cpf} é um CPF válido')
        break
    else:
        print(f'{cpf} é um CPF inválido')
        break
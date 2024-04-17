def valores(parcelas, preco, multa, numero_de_dias_em_atraso, juros):
    if numero_de_dias_em_atraso > 0:
        valor_final = preco + multa + juros
        return valor_final
    else:
        return preco

def numero_parcelas(valor):
    while valor > 0:
        print(f"Valor da prestação: R${valores(valor, preco, multa, numero_de_dias_em_atraso, juros):.2f}")
        valor = int(input('Digite outro valor de parcelas: '))
    print(f'São {parcelas} parcelas, {numero_de_dias_em_atraso} de dias de atraso, R${multa:.2f} de multa e R${juros:.2f} de juros. Ficando no total R${valores(parcelas , preco, multa, numero_de_dias_em_atraso, juros):.2f}')

parcelas = int(input('Digite a quantidade de parcelas: '))
preco = 820
multa = (3 / 100) * preco
numero_de_dias_em_atraso = int(input('Digite o valor dos dias de atraso: '))
juros = numero_de_dias_em_atraso * (0.1 / 100) * preco

print(f"Valor a ser pago: R${valores(parcelas, preco, multa, numero_de_dias_em_atraso, juros):.2f}")

numero_parcelas(parcelas)
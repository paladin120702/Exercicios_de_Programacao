#f-strings
nome = 'Artur'
altura = 1.77
peso = 104.55
imc = peso / (altura * altura)
resumo = f'{nome} tem {altura} de altura , pesa {peso} Kg e seu imc é {imc:.2f}'
#format
string = 'O {} tem {} metros de altura, pesa {}Kg e seu imc é {:.2f}'
formato = string.format(nome , altura , peso , imc)
print (formato)

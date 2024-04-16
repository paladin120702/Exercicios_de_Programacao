nota1 = int(input('Primeira nota: '))
nota2 = int(input('Segunda nota: '))

soma = nota1 + nota2
soma2 = soma / 2
print(soma2)

if soma2 == 10:
    print('Aprovado com distinção')

if soma2 >= 7 and soma < 10 :
    print('Aprovado')

if soma2 < 7:
    print('Reprovado')


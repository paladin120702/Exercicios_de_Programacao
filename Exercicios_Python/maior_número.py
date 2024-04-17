numeros = []

for i in range(5):
    num = float(input('Digite um número '))
    numeros.append(num)

maior_numero = max(numeros)
print(f'O maior número é {maior_numero}')

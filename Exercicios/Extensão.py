n = int(input('Digite um valor para o termos '))
numerador = 1
denominador = 1
s = 'S = '
for i in range(n):
    s = s + str(numerador) + '/' + str(denominador) + ' + '
    numerador += 1
    denominador +=2
s = s[:-2]
print (s)

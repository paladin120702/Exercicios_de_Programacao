def numeros(parametro):
    contador = 0
    for caractere in parametro:
        if caractere == '5':
            contador += 1
    print(contador)

digito = input('Digite um número ')
numeros(digito)



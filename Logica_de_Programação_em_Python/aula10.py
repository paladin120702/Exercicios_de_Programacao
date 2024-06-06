palavra_secreta = ('AdVictoriam')
letras_acertadas = ''
tentativas = 0
while True:
    palavra_permitida = input('Digite a palavra secreta ')
    tentativas += 1

    if tentativas > 25:
        print('Programa encerrado: Você não conseguiu desvendar a palavra secreta ')
        break

    if  len(palavra_permitida) > 1:
        print('Pode apenas digitar uma letra ') 
        continue

    if palavra_permitida in palavra_secreta:
        letras_acertadas += palavra_permitida
    
    palavra_fomrada = ''
    for letra_secrerta in palavra_secreta:
        if letra_secrerta in letras_acertadas:
            palavra_fomrada += letra_secrerta
        else:
            palavra_fomrada += '*'
    print('Palavra formada:' , palavra_fomrada)
    
    if palavra_fomrada == palavra_secreta:
        print('Vc ganho parabéns ')
        print('A palavra era:' , palavra_secreta)
        print('Tentativas:' , tentativas)
        break

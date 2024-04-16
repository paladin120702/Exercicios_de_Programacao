while True:
    numero1 = input('Digite o primeiro número ')
    numero2 = input('Digite o segundo número ')
    operador = input('Digite o operador ')
    numeros_validos = None
    num_1 = 0
    num_2 = 0

    try:
        num_1 = float(numero1)
        num_2 = float(numero2)
        numeros_validos = True
    except:
        numeros_validos = None

    operdores_permitidos = '+-*/'

    if numeros_validos is None:
        print('Um ou ambos os números digitados são invalidos ')
        continue

    if operador not in operdores_permitidos:
        print('Operador invailido ')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador')
        continue    

    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '*':
        print(num_1 * num_2)
    elif operador == '/':        
        print(num_1 / num_2)

    quer_sair = input('Digite para sair ').lower().startswith('s')

    if quer_sair is True:
        break
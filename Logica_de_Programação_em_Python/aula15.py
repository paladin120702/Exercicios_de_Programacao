def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total
multiplicacao = multiplicar(1,2,5,8)
print (f'Todos os valores = {multiplicacao}')


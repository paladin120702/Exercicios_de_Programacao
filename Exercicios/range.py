def imprimir_padrao(n):
    for i in range(1, n + 1):
        linha = ' '.join(str(i) for _ in range(i))
        print(linha)

n = int(input("Digite o valor de n: "))

imprimir_padrao(n)
def somaimposto(taxaimposto , custo):
    custo_com_imposto = custo + taxaimposto
    return custo_com_imposto
    
custo_final = somaimposto(10 , 100)
print(f'O custo final com a taxa de imposto é: R${custo_final:.2f}')
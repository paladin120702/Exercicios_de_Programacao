import copy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

def mercado(novo_preco):
    for produto in produtos:
        {**produto, 'preco': round(produto['preco'] * 1.1, 2)}
    return produto

def copia(produto):
    produto_copy = copy.deepcopy(produto)
    return produto_copy

def maior_menor(produto):
    decrescente = sorted(produto, key=lambda x: x['preco'], reverse=True)
    return decrescente

def menor_maior(produto):
    crescente = sorted(produto, key=lambda x: x['preco'])
    return crescente

print (mercado(produtos),sep='\n')
print (copia(produtos),sep='\n')
print (maior_menor(produtos),sep='\n')
print (menor_maior(produtos),sep='\n')

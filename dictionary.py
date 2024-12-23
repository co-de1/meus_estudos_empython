
paises = {'br': 'Brasil', 'ru': 'Rússia'}

#    var = dict(chave = 'elemento', ...)

print(paises)
print(paises.get('br'))   # acessando o dicionario

# print(paises['chave']) # acessando o dicionario
# tuplas --> podem ser usadas como chave de um dicionario, pois, sao imutaveis

pais = paises.get('br')

if pais:
    print(f"I found the country {pais}")
else:
    print("I didn't find")

#  Podemos adicionar elementos no dicionario
#  paises['chave'] = atribuicao
#  novo_dado = {'chave': 'atribuicao'}
# --> paises.update(novo_dado)

novo_dado = {'ang': 'Angola'}
paises.update(novo_dado)

print(paises)

#  Podemos remover elementos num dicionario
pais = paises.pop('br')  # removendo um elemento

print(paises)

del paises['ang']  # removendo um elemento

print(paises)

carrinho = []
"""
carrinho = []

produto1 = ['Play', 1, 3500.00]
produto2 = ['God w', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

"""
produto1 = {'nome': 'Play', 'quantidade': 1, 'preço': 3500.00}
produto2 = {'nome': 'God War', 'quantidade': 1, 'preco': 150.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

veja = {}.fromkeys(range(1, 5), 'LEINAD')  # forma um dicionario igualmente as outras formas
print(veja)

# acessando as chaves usando keys() --> print(var.keys()) ou usando um for
# for chave in var.keys():
# print(var[chave])


"""

CONJUNTOS -->> Não diferem dos conjuntos numericos
-->> Podemos aplicar dos os conceitos matmáticos
-->> Podemos usar alguns conceitos usados em listas, tuplas e dicionários aqui também
(metódos em particular)

-->> it can be represented by { }
-->> Diferente de dos Mapas (dicionarios), nao possuem chaves, so valores

"""

# Declarando um conjunto

conjunto = {2, 3, 3, 4, 5, 2, 3}
print(conjunto)
print(type(conjunto))

# Podemos adicionar/remover/copiar/unir/intercetar elementos
"""

Entao podemos dizer que os conjuntos sao mutaveis

-->> usamos a funcao add() ##adicionando
-->> variavel.add(atribuicao) ##adicionando
conjunto.add(4)

-->> usamos a funcao remove() ##removendo
-->> variavel.remove(atribuicao) ##removendo
podemos usar tambem discard/clear

conjunto.discard(4)

lista = [1, 3, 'arroz']
print(lista)
tupla = 1, 3, 'frango'
print(tupla)
dicionario = {}.fromkeys(range(1, 5), 'LEINAD')
print(dicionario)

conjunto = set(dicionario)
print(conjunto)

-->> iterando sobre um set(conjunto)

for valor in conjunto:
    print(f'Elementos em comum: {valor}')
    
podemos copiar usando a funcao copy() / fazendo a atribuicao

-->> novo = conjunto.copy()

"""
conjunto1 = {'Sao Paulo', 'Angola', 'Brasil', 'Inglaterra'}
conjunto2 = {'EUA', 'Angola', 'Brasil', 'Mali'}

# value = value1/value2.difference(value1/value2)

conjunto = conjunto1.intersection(conjunto2)
print(conjunto)
print(len(conjunto))

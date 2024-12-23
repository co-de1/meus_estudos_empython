"""

FUNCOES SEM NOME OU ANOMINAS

lambda argumentos: retorno (expressao)

soma = lambda x, y: x + y
print(soma(5, 3))  # Saída: 8

# ORDENANDO UMA LISTA

lista = [(1, 'a'), (2, 'c'), (3, 'b')]
lista_ordenada = sorted(lista, key=lambda x: x[1])
print(lista_ordenada)

# FILTRANDO UM ELEMENTO

numeros = 1, 2, 3, 4, 5, 6
tupla_filtrada = tuple(filter(lambda x: x % 2 == 0, numeros))
print(tupla_filtrada)

numeros = 1, 2, 3, 4, 5, 6
quadrados = list(map(lambda x: x ** 2, numeros))
print(quadrados)  # Saída: [1, 4, 9, 16, 25, 36]


def quadrado_de_um_numero(a, func):
    return func(a)


resultado = quadrado_de_um_numero(2, lambda x: x**2)
print(resultado)

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

ler_nome = input('Informe o nome: ')
ler_sobrenome = input('Informe o sobrenome: ')

print('\n', nome_completo(ler_nome, ler_sobrenome))

autores = ['Jose Antonio', 'Eduardo Cabundo', 'Alfredo Macutunda', 'Joao Alvaro']
autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1])

print(autores)

def geradora_quadratica(a, b, c):
    return lambda x: a * x ** 2 + b * x + c


teste = geradora_quadratica(2, 3, -5)
print(teste(4))

# FUNCOES SEM NOME OU ANOMINAS

# lambda argumentos: retorno (expressao)


numeros = [1, 2, 3, 4]
impar = map(lambda x: x + 1, numeros)

print(list(impar))

resultado = map(lambda x: x * 2, numeros)
print(list(resultado))  # Saída: [2, 4, 6, 8]

nomes = ['Vanessa', 'Ana', 'Maria']
lista = filter(lambda nome: len(nome) < 5, nomes)

print(list(lista))

valores = [0, 1, False, None, "Texto", [], {}]
verdadeiros = filter(None, valores)

print(list(verdadeiros))  # Saída: [1, 'Texto']

from functools import reduce

dados = [2, 3, 4, 5, 10]
multi = lambda x, y: x * y
res = reduce(multi, dados)

print(res)


num = 1
for i in dados:
    num *= i

print(num)

print(max(musicas, key=lambda musica: musica["tocou"])["titulo"])


tupla = 1, 2, 3, 4, 5, -1, -2
print(sorted(tupla, reverse=True))
print('Soma =', sum(tupla))
print('Minimo =', min(tupla))

musicas = [
    {"titulo": "Love", "tocou": 3},
    {"titulo": "amor", "tocou": 10},
    {"titulo": "Love_", "tocou": 15}
]

max = 0
for musica in musicas:
    if musica['tocou'] > max:
        max = musica['tocou']

print(max)

nome = ['Jose', ' Antonio', 'Eduardo']
print(max(nome, key=lambda x: len(x)))
"""

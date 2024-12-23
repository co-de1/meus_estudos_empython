"""
for item in interavel:
    //execução do loop

    iterar sequências ou valores iteráveis

- Range
    numeros = range (inicio, fim)
- Lista
    lista = [1, 3, 5, 7, 9]
- String
    nome = 'Geek University'

    #   exemplo 1 string
for letra in nome:
    print(letra, end='')

#   exemplo 2 string
for numero in lista:
    print(numero)

#   exemplo 2
for numero in range(1, 10):
    print(numero)
for num in range(1, 11):
    print(num)


nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numero = range(1, 10)  # transformar em lista

for valor in enumerate(nome):
    print(valor)

for num in range(10, -1, -1):
    print(num)


resposta = 'Não'

while resposta != 'Sim':
    resposta = input('Já acabou?: ')
print('Muito bem')
"""
"""

OBS: quando invocamos um loop for, o iter também
é invocado sobre a variável iterada.

lista = [1, 2, 3, 4]

for i in lista:
    print(f'{i}')

mas podemos criar um loop, montando partes de cada função
usando o iter() e next() e tratando os erros

def meu_loop(iteravel):
    it = iter(iteravel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break
"""

lista = [1, 2, 3, 4]


def meu_loop(iteravel):
    it = iter(iteravel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break


meu_loop(lista)

"""

OBS: quando invocamos um loop for, o iter também
é invocado sobre a variável iterada.

lista = [1, 2, 3, 4]

for i in lista:
    print(f'{i}')

mas podemos criar um loop, montando partes de cada função
usando o iter() e next() e tratando os erros


lista = [1, 2, 3, 4]


def meu_loop(iteravel):
    it = iter(iteravel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break


meu_loop(lista)
meu_loop('geek')

"""


class Contador:
    def __init__(self, menor, maior):
        self.menor = menor
        self.maior = maior

    def __iter__(self):
        return self

    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor += 1
            return numero
        raise StopIteration


ret = Contador(1, 11)

for i in ret:
    print(i)

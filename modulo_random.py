
# RANDOM
"""

from random import random


def num_aleatorio():
    print(random())


num_aleatorio()


for i in range(3):
    print(random())

    from random import uniform

print(uniform(1, 3))

for i in range(4):
    print(uniform(0, 2))

    from random import randint

for i in range(3):
    print(randint(0, 2), end='; ')


from random import choice

print(choice((1, 2, 3, 4, )))  # Usado com iteraveis

"""

from random import shuffle


lista = [1, 2, 3, 4, 5, 6]
shuffle(lista)

print(lista)

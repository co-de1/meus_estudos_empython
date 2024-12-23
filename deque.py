"""

deque --> Uma lista de alta performance

from collections import deque

from collections import deque

deq = deque[1, 2, 3, 4, 5]
lista = ['Eu', 'Te', 'Amo', 'Leinad']

print(deq)
print(lista)

if 'Eu' or 'eu' in lista:
    print('Amo-te')

def soma_numbers(num1, num2):
    return num1 + num2


resultado: float = soma_numbers(num1=float(input('The first number: ')), num2=float(input('The second number: ')))

# soma_numbers(num1=input("The first number: "), num2=input("The second number: "))
print(f"The sum is: {resultado}")
"""


def soma(*args):
    return sum(args)


numbers = [1, 2, 3, 4, 5]
print(soma(*numbers))

# print(soma(num1=3, num2=4))

teste = {'1': 'Amor', '2': 'LEINAD'}

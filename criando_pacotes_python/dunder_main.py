# Dunder main is used to guarantee that a script, once imported
# might work with no problem, although exist in another script it


def soma_impares(numeros):
    return sum(numeros)


lista = [1, 2, 3, 4, 5, 6]

if __name__ == '__main__':
    print(soma_impares(lista))

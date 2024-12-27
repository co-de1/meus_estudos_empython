# Tratando erros


"""
 RAISE

 def tratar_erros(nome, cor):
    if type(nome) is not str:
        raise TypeError('O nome precisa ser string')
    if type(cor) is not str:
        raise TypeError('A cor precisa ser string')
    print(f'O nome {nome} eh de cor {cor}')


tratar_erros('Jose', 'verde')


TAMBÉM TEMOS O else e o finally.


"""


def divisao(a, b):
    try:
        return round(num1/num2, 2)
    except (ZeroDivisionError, ValueError, TypeError, KeyError):
        return 'Ocorreu algum erro'


print('\nDigite dois numeros\n')

num1 = int(input('num1: '))
num2 = int(input('num2: '))

print('Resultado: ', divisao(num1, num2))

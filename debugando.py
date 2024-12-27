

def divisao(a, b):
    try:
        return round(num1/num2, 2)
    except (ZeroDivisionError, ValueError, TypeError, KeyError):
        return 'Ocorreu algum erro'


print('\nDigite dois numeros\n')
breakpoint()

num1 = int(input('num1: '))
num2 = int(input('num2: '))

print('Resultado: ', divisao(num1, num2))

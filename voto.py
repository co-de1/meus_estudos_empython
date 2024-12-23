
"""

List comprehesion

numeros = [1, 2, 3, 4, 5, 6]

resultado = [numero * 4 for numero in numeros]

print(resultado)

old_numero = [1, 2, 3, 4, 5]
new_numero = []

for numero in old_numero:
    new_numero.append(numero*2)

print(new_numero)

print([numero*2 for numero in old_numero])

nome = 'Jose Antonio'

print([letra.upper() for letra in nome])

def caixa_alta(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome


amigos = ['jose', 'maria', 'eduardo']

print([caixa_alta(amigo) for amigo in amigos])

"""

A = [1, 0, 5, -2, -5, 7]
soma = A[0] + A[1] + A[5]

print(soma)

for i in A:
    A[5] = 100
print(A)

for j in range(len(A)):
    print(A[j])

B = []

for k in range(10):
    valores = int(input('Informe os valores: '))
    B.append(valores)

contador = 0
for k in range(len(B)):
    if B[k] % 2 == 0:
        print(f'{B[k]} Par')
        contador = contador + 1
    else:
        print(f'{B[k]} Impar')

print(f'Existem {contador} pares')

"""
Iteraveis e iteradores

# Testando se são iteráveis
print(iter(lista))   # Retorna um iterador
print(iter(string))  # Retorna um iterador
print(iter(tupla))   # Retorna um iterador

# Exemplos de iteráveis
lista = [1, 2, 3]
string = "Python"
tupla = (4, 5, 6)

teste = iter(lista)

for i in lista:
    print(f'{i}')

# Iterável
lista = [1, 2, 3]

# Python cria automaticamente o iterador no loop for
for item in lista:
    print(item)

"""


class Contador:
    def __init__(self, inicio, fim):
        self.atual = inicio
        self.fim = fim

    def __iter__(self):
        return self  # Retorna o próprio iterador

    def __next__(self):
        if self.atual > self.fim:
            raise StopIteration
        valor = self.atual
        self.atual += 1
        return valor


# Usando o iterador
contador = Contador(1, 5)
for numero in contador:
    print(numero)

# Treinando o uso da funcao Zip

"""
nomes = ["Ana", "Carlos", "Beatriz"]
idades = [25, 30, 22]

# Combinar usando zip
combinado = zip(nomes, idades)

# Transformar em lista ou qualquer iteravel para visualizar
print(tuple(combinado))
# Saída: [('Ana', 25), ('Carlos', 30), ('Beatriz', 22)]
"""

cores = ["vermelho", "azul", "verde"]
valores = [10, 20, 30]

for cor, valor in zip(cores, valores):
    print(f"A cor {cor} tem o valor {valor}")
# Saída:
# A cor vermelho tem o valor 10
# A cor azul tem o valor 20
# A cor verde tem o valor 30

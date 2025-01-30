"""
Porgramação orientada a objetos
--> Classe - Modelos de objetos do mundo real, representados computacionalmente
--> Atributos - Características de uma classe
--> Métodos - Comportamentos da classe (O que a classe faz)
--> Constructor - Um método, mas especial (utilizado para criar objetos a partir da nossa classe)

NOTA: Atributos em Python podem ser públicos ou privados, mas por conveniença,
são todos públicos. Ainda assim, é possível representar um privato usando (self.__nomeAtributo))
"""


class Produto:
    # ATRIBUTO DE CLASSE
    imposto = 0.2
    contador = 0

    # ATRIBUTO DE INSTANCIA
    def __init__(self, nome, preco, descricao):
        self.id = Produto.contador + 1
        self.nome = nome
        self.preco = preco
        self.descricao = descricao
        Produto.contador = self.id


coisas = Produto("Massa", 2.000, "spagueth")
coisas1 = Produto("Arroz", 3.000, "tio joao")
coisas2 = Produto("Feijao", 3.500, "carioca")

print(coisas.nome, " = ", coisas.preco, " - ", coisas.descricao)
print(coisas1.nome, " = ", coisas1.preco, " - ", coisas1.descricao)
print(Produto.imposto)

print(coisas.id)
print(coisas1.id)
print(coisas2.id)

coisas.peso = "3kg"

print(coisas.nome, " = ", coisas.preco, " - ", coisas.descricao, " | Peso = ", coisas.peso)
print(coisas.__dict__)

del coisas.peso

print(coisas.__dict__)

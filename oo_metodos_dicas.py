"""

METODOS EM PYTHON --> REPRESENTAM COMPORTAMENTO DOS OBJETOS DE UMA INSTÂNCIA
OU AÇÕES QUE ESTE OBJETO PODE REALIZAR NO SOTWARE

EM PYTHON DIVIDIMOS OS MÉTOS EM 2:
-- MÉTODOS DE INSTÂNCIA
-- MÉTODOS DE CLASSE

O Método dunder init {__init__} é um método especial chamado constructor e sua função
é especial construir o objeto a partir da classe.


produto = Produto("Massa", 2.500, "spageth", 1234)

print("Nome: ", produto.nome_produto(), "\nPreco = ", produto.preco_produto(), "Senha = ")
from passlib.hash import pbkdf2_sha256 as cryp  # usado para criptografar senhas em Python

"""


class Produto:
    imposto_produto = 1.05
    contador = 0

    @classmethod  # Metodos estaticos
    def contar_produtos(cls):
        return cls.contador + 1

    @staticmethod
    def teste():
        return "TESTE"

    def __init__(self, nome, preco, descricao):
        self.__nome = nome
        self.__preco = preco + preco*Produto.imposto_produto
        self.__descricao = descricao

    def nome_produto(self):
        return self.__nome

    def preco_produto(self):
        return self.__preco

    def descreve_produto(self):
        return self.__descricao


produto = Produto("Massa", 2.500, "spageth")

print("Nome: ", produto.nome_produto(), "\nPreco = ", produto.preco_produto())

print(f"Quantidade de produtos: {Produto.contar_produtos()} ")
print(Produto.teste())

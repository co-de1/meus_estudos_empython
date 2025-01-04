# Vamos ler algum arquivo em Python

"""
# Abrindo o arquivo
arquivo = open('README.md')

# lendo o arquivo
print(arquivo.read())

arquivo.seek(0)
arquivo.close()

caminho_arquivo = "README.md"  # Substitua pelo caminho do arquivo
try:
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            print(linha.strip())  # Imprime cada linha
except FileNotFoundError:
    print("Arquivo não encontrado!")

with open('teste.txt', 'w') as arq:
    arq.write("Fazendo exercicios da aula escrevendo em arquivos\n")
    arq.write('Procurando melhorar cada vez mais as minhas habilidades em Python\n')

    arquivo = open('vamos.txt', 'w', encoding='utf-8')

arquivo.write('Vamos com tudo nesta, temos que conseguir alcançar nossos objetivos')
arquivo.write('\nFoi desta, que 2025 seja um ano de mais foco')

try:
    with open('teste.txt', 'a+', encoding='utf-8') as arq:
        arq.write("Fazendo exercicios da aula escrevendo em arquivos\n")
        arq.write('Procurando melhorar cada vez mais as minhas habilidades em Python\n')
except FileExistsError:
    print('Arquivo já existe')

"""

from io import StringIO

mensagem = 'Fzendo testes com o modulo StringIo'
arq = StringIO(mensagem)

print(arq.read())

arq.write('\tFunciona para escrever outro texto')
arq.seek(0)

print(arq.read())

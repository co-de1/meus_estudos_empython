# Vamos ler algum arquivo em Python

"""
# Abrindo o arquivo
arquivo = open('README.md')

# lendo o arquivo
print(arquivo.read())

arquivo.seek(0)
arquivo.close()

"""
caminho_arquivo = "README.md"  # Substitua pelo caminho do arquivo
try:
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            print(linha.strip())  # Imprime cada linha
except FileNotFoundError:
    print("Arquivo não encontrado!")

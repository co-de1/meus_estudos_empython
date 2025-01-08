# Manipulação de arquivos
"""
# Abre o arquivo para escrita
with open('arq.txt', 'w', encoding='utf-8') as aq:
    while True:
        entrada = input('Informe caracteres ou 0 para sair: ')
        if entrada == '0':
            break
        aq.write(entrada + '\n')


with open('arq.txt', 'r', encoding='utf-8') as aq:
    print(aq.read())

"""

with open('arquivo.txt', 'w', encoding='utf-8') as arq:
    nome_texto = input('Insira o texto: ')
    arq.write(nome_texto + '\n')


contador = 0

with open('arquivo.txt', 'r', encoding='utf-8') as arq:
    for linha in arq:
        contador += 1

print(contador)


tupla = (1, 2, 3, 4)

for indice, var in enumerate(tupla):
    print(indice, var)

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro'
         , 'Dezembro')
#print(meses)

i = 0

while i < len(meses):
    print(meses[i])
    i += 1

print(meses.index('Agosto'))

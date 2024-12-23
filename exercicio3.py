
num: int = int(input("\nEnter a number: "))
count: int = 1
multiplo: int = 0

while count < 50:
    if count % num == 0:
        multiplo += 1
        print(count)
    if multiplo == 5:
        break
    count += 1

lista = 'Jose'

print(lista[::-1])


nome = input("\nEnter a sentence: ")

nome = list(nome)

list.reverse(nome)

nome1 = nome

if nome == nome1:
    print(f"\nThe word {nome1} is polindromo")

print(len(nome1))

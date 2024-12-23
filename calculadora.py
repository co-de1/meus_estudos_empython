"""

VAMOS FAZER UM PROJECTO DE CALCULADORA ENVOLVENDO AS 4 OPERAÇÕES (+, -, x, /)
VAMOS COMEÇAR FAZENDO O MENU

1- SOMA
2- SUBTRAÇÃO
3- MULTIPLICAÇÃO
4- DIVISÃO
0 - SAIR

VAMOS USAR A ESTRURA DE REPETIÇÃO WHILE
"""

print("__________CALCULADORA__________\n\n")

while True:

    print("1 - SOMA\n2 - SUBTRAÇÃO")
    print("3 - MULTIPLICAÇÃO\n4 - DIVISÃO\n0 - SAIR")
    op = int(input("\nEscolha a operação que deseja: "))

    if op == 1:
        numero1 = float(input("Digite o primeiro numero: "))
        numero2 = float(input("Digite o segundo numero: "))

        resultado: float = numero1 + numero2
        print(f"\nResultado = {resultado}")
    elif op == 2:
        numero1 = float(input("Digite o primeiro numero: "))
        numero2 = float(input("Digite o segundo numero: "))

        if numero1 > numero2:
            resultado: float = numero1 - numero2
            print(f"\nResultado = {resultado}")
        else:
            resultado: float = numero2 - numero1
            print(f"\nResultado = {resultado}")
    elif op == 3:
        numero1 = float(input("Digite o primeiro numero: "))
        numero2 = float(input("Digite o segundo numero: "))

        resultado: float = numero1 * numero2
        print(f"\nResultado = {resultado}")
    elif op == 4:
        numero1 = float(input("Digite o primeiro numero: "))
        numero2 = float(input("Digite o segundo numero: "))

        if numero2 == 0:
            print("Erro")
        else:
            resultado: float = numero1 / numero2
            print(f"\nResultado = {resultado}")
    else:
        break

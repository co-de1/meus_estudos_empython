# Faça um programa que exiba o resultado do resto da divisão de 100 por 7.


"""

teste = seja_educado(saudacao)

teste()



def seja_educado(funcao):
    def sendo():
        print('Foi um prazer')
        funcao()
    return sendo


@seja_educado  # decorator
def saudacao():
    print('Seja Bem-vindo')


saudacao()


def meu_decorator(func):
    def wrapper(*args, **kwargs):
        # Código antes da função original
        print("Antes de chamar a função")
        resultado = func(*args, **kwargs)
        # Código depois da função original
        print("Depois de chamar a função")
        return resultado
    return wrapper


@meu_decorator
def minha_funcao():
    print("Função sendo executada")


minha_funcao()

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Executando {func.__name__} com argumentos {args} e {kwargs}")
        resultado = func(*args, **kwargs)
        print(f"{func.__name__} retornou {resultado}")
        return resultado
    return wrapper


@log_decorator
def soma(a, b):
    return a + b


soma(3, 5)
"""

import time


def medir_tempo(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fim = time.time()
        print(f"Tempo de execução de {func.__name__}: {fim - inicio:.4f} segundos")
        return resultado
    return wrapper


@medir_tempo
def tarefa_lenta():
    time.sleep(2)
    print("Tarefa concluída")


tarefa_lenta()

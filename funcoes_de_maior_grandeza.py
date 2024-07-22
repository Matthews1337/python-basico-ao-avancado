"""
Funções de maior grandeza - Higher Order Functions -> HOF

O que isso significa ?

- Quando uma linguagem de programação suporta HOF, indica que podemos ter funções
 que retornam outras funções como resultado ou mesmo podemos passar funções como
 argumentos para outras funções, e até mesmo criar variáveis do tipo de funções


"""

# Ex: Definindo as funções

def somar(a,b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a,b):
    return  a*b

def dividir(a,b):
    return a/b


def calcular(num1, num2, funcao):
    return funcao(num1, num2)


print(calcular(2, 4, somar))
print(calcular(2, 4, multiplicar))


"""
Nested Functions - Funções aninhadas

Em Python podemos tembém ter funções, que são conhecidas por Nested Funtions ou também Inner Functions

"""
from random import choice


def cumprimento(pessoa):
    def humor():
        return choice(['E ai', 'Que bom te ver', 'Tudo bem?'])
    return humor() + ' ' + pessoa # Executando a função humor()

print(cumprimento('Miguel'))



def faz_me_rir():
    def risada():
        return choice(['hahahhaahah', 'kkkkkkkkkkkkkk', 'jajajajajajaja'])
    return risada # retornando a função risada
    
# Testando

rindo = faz_me_rir()

print(rindo()) # Executando a variável como fosse a função
    
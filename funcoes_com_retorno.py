"""
Funções com retorno


numeros = [1, 2, 3]

ret_pop= numeros.pop()

print(f'Retorno de pop {ret_pop}')

ret_pr = print(numeros)

print(f'Retorno de print: {ret_pr}')

OBS: Em Python, quando uma função nao retorna nehnum valor, o retorno é None

OBS: Funçoes Python que retorna valores, devem retornar estes valores com a palavra reservada return

OBS: Não precisamos necessariamente criar uma variavel para receber o retorno de uma funçao. Podemos passar a execução da função para outras funçoes



                                   # Vamos refatorar esta funçao para que ela retorne o valor

def quadrado_de_7():
    return 7 * 7


                                   # Criamos uma variavel para receber o retorno da função

ret = quadrado_de_7()
print(f'Retorno de {ret}')

print(f'Retorno: {quadrado_de_7()}')


                                    # Refatorando a primeira função

def diz_oi():
    return'oi '


alguem = 'Pedro'

print(diz_oi() +f'{alguem}!')


OBS: Sobre a palavra return

1 - Ela finaliza a função, ou seja, ela sai da execução da função:
2 - Podemos ter, em uma função, diferentes returns:
3 - Podemos em uma função, retornar qualquer tipo de dado e até mesmo multiplos valores:


# Exemplo 1 - Ela finaliza a função, ou seja, ela sai da execução da função:

def diz_oi():
    return 'oi '
    print('estou sendo executado apos o retorno...') # Esta linha não é executada

print(diz_oi())



# Exemplo 2 - Podemos ter, em uma função, diferentes returns:


def nova_funcao():
    variavel = False   # Quando "True" a variavel retorna '4'
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'          # Imprime "b" quando a variavel não é "True" nem "None"

print(nova_funcao())



# Exemplo 3 - Podemos em uma função, retornar qualquer tipo de dado e até mesmo multiplos valores:

def outra_funcao():
    return 2, 3, 4, 5

#num1, num2, num3, num4 = outra_funcao()

#print(num1, num2, num3, num4)

print(outra_funcao())


# Vamos criar uma funçao para jogar a moeda

from random import random

def joga_moeda():
    #gera um numero pseudo-randomico entre 0 e 1
    valor = random()
    if valor > 0.5:         # (ou simplificando) if random() > 0.5
        return 'cara'
    return 'coroa'

print(joga_moeda())

"""

# Erros comuns na utilização do retorno, que na verdade nem é erro, mas sim codificação desnecessaria


# Desnecessario
def eh_impar():
    numero = 5
    if numero % 2 != 0:   # "%"  <- módulo
        return True
    else:
        return False

print(eh_impar())

# simplificando

def eh_impar():
    numero = 5
    if numero % 2 != 0:
        return True
    return False

print(eh_impar())
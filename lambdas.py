"""
UTILIZANDO LAMBDAS

Conhecidas por Expressões Lambdas, são funções sem nome, ou seja funções anônimas

# Função em Python


def soma(a, b):
    return a + b

    
---------------------------------------------------------------------------------------------

def funcao(x):
    return 3 * x + 1

print(funcao(4))


# EXPRESSAO LAMBDA



calc = lambda x: 3 * x + 1

print(calc(7))

----------------------------------------------------------------------------------------------

soma = lambda y: y + 2

print(soma(5))

----------------------------------------------------------------------------------------------

# Podemos ter expressoes lambdas com multiplas entradas

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo('matheus', 'fonseca'))

----------------------------------------------------------------------------------------------


# EM FUNÇOES PYTHON PODEMOS TER NENHUMA OU VARIAS ENTRADAS. EM LAMBDAS TAMBEM

amar =  lambda: 'Como não amar Python?'

uma = lambda x: x + 1

duas = lambda x, y: x * y

tres = lambda x, y, z: 3 / (1 / x + 1 / z)

print(amar())
print(uma(1))
print(duas(2, 2))
print(tres(5, 4, 3))

----------------------------------------------------------------------------------------------


autores = ['Isaac Asimov', 'Ray Bradbury', 'Robert Heinlein', 'Arthur C. Clarke', 'Frank Herbert', 'Orson Scott Card']

print(autores)

autores.sort(key = lambda sobrenome: sobrenome.split(' ')[-1].lower())

print(autores)



"""



#função quadratica

# f(x) = a * x ** 2 + b * x + c

#definindo a função

def geradora_funcao_quadratica(a, b, c):
    """RETORNA A FUNCAO f(x) = a * x ** 2 + b * x + c """
    return lambda x: a * x ** 2 + b * x + c

teste = geradora_funcao_quadratica(2, 3, -5)

print(teste(0))
print(teste(1))
print(teste(2))

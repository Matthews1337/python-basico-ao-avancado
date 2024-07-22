"""
Preservando metadatas com wraps

Metadatas -> São dados íntrisecos em arquivos. (caractristicas dos arquivos)

wraps -> são funções que envolvem elementos com diversas finalidades.

"""


# Problema


def ver_log(funcao):
    def logar(*args, **kwargs):
        """ Eu sou uma função logar dentro de outra função"""
        print(f'Você está chamando {funcao.__name__} com {args}')
        print(f'Documentação {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    """ Soma dois números"""
    return a + b



print(soma(10, 40))
print('------------------------------------')

# Problema -> chama a documentação da função logar
print(soma.__name__)
print(soma.__doc__)


print('------------------------------------')


# Resolução do problema


from functools import wraps


def ver_log(funcao):
    @wraps(funcao) # -> Protege os metadados das funções
    def logar(*args, **kwargs):
        """ Eu sou uma função logar dentro de outra função"""
        print(f'Você está chamando {funcao.__name__} com {args}')
        print(f'Documentação {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    """ Soma dois números"""
    return a + b



print(soma.__name__)
print(soma.__doc__)
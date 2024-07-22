"""
Decorators com diferentes assinaturas

"""

# Relembrando

def gritar(funcao):
    def aumentar(nome):
        return funcao(nome).upper()
    return aumentar


@gritar
def meu_nome(nome):
    return f'Eu sou {nome}'


print(meu_nome('Matheus'))


@gritar
def ordem(principal, acompanhamento):
    return f'Olá eu gostaria de {principal} acompanhado de {acompanhamento}'

print('----------------------------------------------------------------------')
# print(ordem(principal='hamburguer', acompanhamento='batatas')) # Vai dar erro pela quantidade de parametros

"""
Para resolver vamos usar *args e **kwargs
"""

def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar

@gritar
def meu_nome(nome):
    return f'Eu sou {nome}'


print(meu_nome('Matheus'))


@gritar
def ordem(principal, acompanhamento):
    return f'Olá eu gostaria de {principal} acompanhado de {acompanhamento}'

print(ordem(principal='hamburguer', acompanhamento='batatas')) 




"""
Decorators com parametros/argumentos
"""

# def verifica_primeiro_argumento(valor):
#     def interna(funcao):
#         def outra(*args, **kwargs):
#             if args and args[0] != valor:
#                 return f'Valor incorreto! {args[0]} != {valor}'
#             return funcao(*args, **kwargs)
#         return outra
#     return interna

print('----------------------------------------------------------------------')


def verifica_argumento(argumento): # => vai receber o parametro do decorator
    def recebe_funcao(funcao): # -> vai receber a funcao decorada
        def compara_argumentos(*args, **kwargs): # -> faz a comparação entre o parametro do decorator com o parametro da função decorada
            if args and args[0] != argumento:
                return f'Valor incorreto! {args[0]} != {argumento}'
            return funcao(*args, **kwargs) # -> vai retornar o comida_preferida()
        return compara_argumentos
    return recebe_funcao



@verifica_argumento('hamburguer')
def comida_preferida(*args):
    return f'minha comida preferida é {args}!'


print(comida_preferida('pizza'))
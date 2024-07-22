

def cumprimenta(nome):
    return f'Olá {nome}'


def cumprimenta_v2(nome, /):
    return f'Olá {nome}'



print(cumprimenta(nome='Matheus'))
print(cumprimenta_v2('Matheus'))
# print(cumprimenta_v2(nome='Matheus')) # TypeError: cumprimenta_v2() got some positional-only arguments passed as keyword arguments: 'nome'

def cumprimenta_v3(nome, mensagem='olá', /): # Todos os parametros antes da barra são somente posicionais
    return f'{mensagem} {nome}'


print(cumprimenta_v3('Matheus'))
print(cumprimenta_v3('Matheus', 'Hello'))
# print(cumprimenta_v3('Matheus', mensagem='Hello')) # TypeError: cumprimenta_v3() got some positional-only arguments passed as keyword arguments: 'mensagem'




def cumprimenta_v4(*, nome, idade): # Todos os parametros depois do '*' devem ser nomeados quando for chamar a função
    return f'Olá {nome}, você tem {idade} anos.'




print(cumprimenta_v4(nome='matheus', idade=26))
print(cumprimenta_v4('matheus', 25)) # TypeError: cumprimenta_v4() takes 0 positional arguments but 2 were given

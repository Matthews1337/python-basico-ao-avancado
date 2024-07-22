"""
**Kwargs
Poderiamos chamar este parametro de **xis, mas por convenção chamamos de **Kwargs

Este é só mais um parametro, mas diferente do *args que coloca o valores extras em uma tupla, o **kwargs exige que utilizamos
parametros nomeados, e transforma esses parametros extras em um dicionario.







                                    # Exemplo

def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'a cor favorita de {pessoa} é {cor}')

cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')

# OBS: Os parametros *args e **kwargs não são obrigatorios

cores_favoritas()

cores_favoritas(geek='navy')





                               # Exemplo mais complexo


def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs ['geek'] == 'python':
        return 'voce recebeu um cumprimento pythonico geek!'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} geek!"
    return 'nao tenho certeza quem voce é...'


print(cumprimento_especial())
print(cumprimento_especial(geek='python'))
print(cumprimento_especial(geek='oi'))
print(cumprimento_especial(geek='especial '))




                                 # Nas nossas funçoes, podemos ter (NESTA ORDEM):

- parametros obrigatorios
- *args;
- parametros default (nao obrigatorios)
- **kwargs




def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('solteiro')
    else:
        print('casado')
    print(kwargs)

minha_funcao(8, 'julia')
minha_funcao(18, 'felicity', 4, 5, 6, solteiro=True)
minha_funcao(34, 'felipe', eu= 'não', voce='vai')
minha_funcao(19, 'carla', 9, 4, 3, java=False, python=True)


"""

# Entenda por que é  importante manter a ordem dos parametros na declaração

def mostra_info(a, b, *args, instrutor='geek', **kwargs):
    return [a, b, args, instrutor, kwargs]

"""
a = 1
b = 2
args = (3,)
instrutor = 'geek'


"""



print(mostra_info(1, 2, 3, sobrenome='university', cargo='instrutor' ))


                   # Exemplo de args
    
def data_de_nascimento(nome, *args):
    print('nome: ', nome)
    for data in args:
        print('ano:', data)



print(data_de_nascimento("Matheus", '1997'))
print(data_de_nascimento('Emanuel', '1998'))






"""
raise => lança exceções

OBS: o raise é uma palavra reservada

Util para que possamos criar nossas proprias exceções e mensagens de erro

Ex: raise TipoErro ("mensagem")

O raise assim como o return finaliza a função, ou seja, nada após o raise será executado

"""


letra = 1

if type(letra) is not str:
    raise TypeError("A letra não pode ser maior que 10")

else:
    print("ok")
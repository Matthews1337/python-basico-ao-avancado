"""
Doctestes

Doctestes são testes que colocamos na docstring das funções/metodos python.
Para rodar um teste do docteste:
    python -m doctest -v nome_do_modulo.py

    
# OBS: Em alguns editores de texto, caso houver espaços em branco o teste ira falhar. Por exemplo, se falar que o return deveria ser 'True' 
e sem querer, colocar 'True ' , com o espaço extra na frente, o teste irá falhar.

OBS: As docstrings naão reconhecem aspas duplas, somente simples. Se um parametro for passado com aspas duplas o teste vai dar erro.

"""

def soma(a,b):
    """
    >>> soma(2,3)
    5

    """
    return a + b

# soma(3,3)

def duplicar(valores):
    """
    duplica valores em uma lista

    >>> duplicar([1,2,3,4])
    [2,4,6,8]

    >>> duplicar([])
    []

    >>> duplicar(['a','b','c'])
    ['aa','bb','cc']

    >>> duplicar([True, None])
    Traceback (most recent call last)
    ...
    TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'

    """
    pass

duplicar([1,2,3,4])
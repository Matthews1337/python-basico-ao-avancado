"""
Modulo Collections - Default Dict


dicionario = {'Curso': 'Programação em Python: Essencial'}

print(dicionario)

print(dicionario['curso'])

print(dicionario['outro']) #??? KeyError

Default Dict -> Ao criar um dicionario utilizando-o, nós informamos um valor default, podendo utilizar um lambda para isso.
Este valor será utilizado sempre que nao houver um valor definido. Caso tentemos acessar uma chave que nao existe, essa chave
sera criada e o valor default sera atribuido.
"""

#fazendo import
from collections import defaultdict

dicionario = defaultdict(lambda: 0)

dicionario['curso'] = 'Programação em Python: Essencial'

print(dicionario)
print(dicionario['outro'])  # KeyError no dicionario comum, mas aqui não

print(dicionario)



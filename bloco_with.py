"""
O bloco with

Passo para se trabalhar com arquivos

# 1 - ABRIMOS O ARQUIVO
# 2 - FAZER ALGO COM O ARQUIVO
# 3 - FECHAR O ARQUIVO

O bloco with é utilizado para criar um contexto de trabalho onde os recursos são fechados após o bloco with.

arquivo = open('texto.txt')

"""

# O bloco with - Forma Pythonica de manipular arquivos

with open('teste.txt') as arquivo:
    print(arquivo.readlines())
    print(arquivo.closed)
"""
Módulo collections - deque

Podemos dizer que o deque é uma lista de alta performance.

"""

#importa

from collections import deque

# Criando deques

deq = deque('geek')
print(deq)

# Adicionando elementos no deque

deq.append('y')  # Adiciona no final

print(deq)

deq.appendleft('k') # Adiciona no começo da lista

print(deq)

print(deq.popleft()) # remove e retorna o primeiro elemento

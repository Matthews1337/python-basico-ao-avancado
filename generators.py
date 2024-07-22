"""
tuple comprehensions == generators

nomes = ['Carlos', 'Camila', 'Carla', 'Cristiano']


print(any(nome[0] == 'C' for nome in nomes))



----------------------------------------------------------------------------------------------------------------------------------
from sys import getsizeof

# getsizeof -> retorna a quantidade de bytes em memoria do elemento passado como parametro


print(getsizeof('Geek'))


print(getsizeof('University'))


print(getsizeof(9))


print(getsizeof(91))


"""

from sys import getsizeof

# Gerando uma lista de numeros com List Comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])

# Gerando uma lista de numeros com Set Comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando uma lista de numeros com Dictionary Comprehension
dic_comp = getsizeof({x: x * 10 for x in range(1000)})

# Gerando uma lista de numeros com Generator Comprehension
gen_comp = getsizeof(x * 10 for x in range(1000))


print(f'List comprehension {list_comp}')

print(f'Set comprehension {set_comp}')

print(f'Dictionary Comprehension {dic_comp}')

print(f'Generator Comprehension {gen_comp}')






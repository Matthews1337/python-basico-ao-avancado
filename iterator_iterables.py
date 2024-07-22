"""
Entendendo iterator e iterable


Iterator -> 
    - Um objeto que pode ser iterado
    - Um objeto que retorna um dado, sendo um elemento por vez quando uma funcao next() é chamada

    
Iterable ->
    - Um objeto que irá retornar um iterator quando a funcao iter() for chamada.

"""

nome ="Matheus" # é um iterable mas não é um iterator

numeros = [1, 2, 3, 4, 5, 6, 7, 8] # é um iterable mas não é um iterator



it1 = iter(nome)
it2 = iter(numeros)


print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
print("--------")
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))


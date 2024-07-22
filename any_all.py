"""
Any e All

all() -> Retorna True se todos os elementos do iteravel são verdadeiros ou ainda se o iteravel esta vazio
"""


# Exemplo all()

nomes = ['Camila', 'Caio', 'Carla', 'Cristiano']



print(all([nome[0] == 'C' for nome in nomes]))  # Output: True. Se colocar um nome que nao comece com "C", ele retorna False


print(all([letra for letra in 'eio' if letra in'aeiou']))

print(all([num for num in [4, 2, 10, 6, 8] if num % 2 == 0]))

# any() -> retorna True se qualquer elemento do iteravel for verdadeiro. Se o iteravel estiver vazio, retorna False


print(any([0, 1, 2, 3, 4]))  # True

print(any([0, False, {}, {}])) # False

print(any([nome[0] == 'C' for nome in nomes]))

print(any([num for num in [4, 2, 10, 6, 8, 9] if num % 2 == 0 ]))


"""
REVERSED


OBS: Não confunda com a função reverse() que estudamos nas listas.

reverse() só funciona em listas

já a função reversed() funciona em qualquer iteravel

sua funçao é inverter o iteravel

a função reversed() retorna um iteravel chamado list reverse iterator





"""




# Exemplos

lista = [1, 2, 3, 4, 5]

res = reversed(lista)



print(res) 

# Podemos converter o elemento retornado para uma lista, tupla ou conjunto


# Lista
print(list(reversed(lista)))


# Tupla
print(tuple(reversed(lista)))


# Conjunto

print(set(reversed(lista)))


# podemos ietrar sobre o reversed

for letra in reversed('Geek University'):
    print(letra, end='') 

# Printando da forma reversa sem a funcao reversed()
    
print('Geek University'[::-1])  


# Podemos também usar o reversed() para fazer um loop for reverso
    
for n in reversed(range(0,10)):
    print(n)



# Percorrendo um loop sem a funcao reversed()
    
for n in range(10, -1, -1):
    print(n)
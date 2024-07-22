"""
Cria um iteravel (zip object) que agrega elemento de cada um dos iteraveis passados como entrada em pares.

"""


#EX:

lista1 = [1, 2, 3]

lista2 = [4, 5, 6]

zip1 = zip(lista1, lista2)

print(zip1)  # Output: zip object
print(type(zip1))  # output: zip


# Sempre podemos gerar uma lista, tupla ou dicionario


print(list(zip1))

zip1 = zip(lista1, lista2) # TEMOS QUE REEXECUTAR PARA PODER PRINTAR OS OUTROS TIPOS, POIS, UMA VEZ EXECUTADO ELE SOME DA MEMORIA 

print(dict(zip1))

zip1 = zip(lista1, lista2)

print(set(zip1))

zip1 = zip(lista1, lista2)

print(tuple(zip1))


# OBS: O zip() utiliza como parametro o menor tamanho em iteravel. Isso significa que se estiver
# trabalhando com iteraveis de tamanhos diferentes, irá parar quando os elementos do menor iteravel acabar

lista3 = [7, 8, 9, 10, 11]

zip1 = zip(lista1, lista2, lista3)

print(list(zip1))



# PODEMOS USAR DIFERENTES ITERAVEIS COM ZIP


tupla = (1, 2, 3)

lista = [4, 5, 6]

dicionario = {'a': 11, 'b': 12, 'c': 13}

merged = zip(tupla, lista, dicionario.values())

print(list(merged))



# lista de tuplas

dados2 = [(0,1), (1, 2), (2, 3), (3, 4), (4, 5)]

print(list(zip(*dados2)))  # => "*" faz a descompactação dos elementos, juntando todos os primeiros elementos de cada tupla


prova1 = [8, 9, 7]
prova2 = [5, 6, 8]

alunos = ["matheus", "tripinha", "thales"]


final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)} # A ordem que se coloca os iteraveis importa

print(final)

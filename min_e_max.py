"""
max() -> retorna o maior valor em um iteravel ou o maior de dois ou mais elementos


----------------------------------------------------------------------------------------------

# Exemplo

lista = [1, 8, 4, 99, 34, 129]

print(max(lista)) #129

tupla = (1, 8, 4, 99, 34, 129)
print(max(tupla)) 

conjunto = {1, 8, 4, 99, 34, 129}
print(max(conjunto))

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129} 

print(max(dicionario))

----------------------------------------------------------------------------------------------

# Faça um programa que receba dois valores do usuário e mostre o maior 


val1 = int(input("Informe o primeiro valor: \n"))
val2 = int(input("Informe o segundo valor: \n"))

print("o maior valor é:" , + max(val1, val2))

----------------------------------------------------------------------------------------------

# Outros exemplos


nomes = ['Matheus', 'Caio', 'Emmanuel', 'Thales', 'Pedro']

print(max(nomes)) #Thales

print(min(nomes)) #Caio

print(max(nomes, key=lambda nome: len(nome))) # Emmanuel
print(min(nomes, key=lambda nome: len(nome))) # Caio

"""


musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "Billie-Jean", "tocou": 8},
    {"titulo": "Time", "tocou": 5}
]


print(max(musicas, key = lambda musica: musica["tocou"]))
print(min(musicas, key = lambda musica: musica["tocou"]))

# IMPRIMINDO O TITULO DA MUSICA MENOS E MAIS TOCADA

print(max(musicas, key = lambda musica: musica["tocou"])['titulo'])
print(min(musicas, key = lambda musica: musica["tocou"])['titulo'])
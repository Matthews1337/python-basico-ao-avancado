"""
OBS: Não confunda, apesar do nome, com a função sort() que já estudamos em Listas. O sort()
só funciona em listas


Podemos utilizar o sorted() com qualquer iteravel.

Como o próprio nome diz, sorted() serve para ordenar

OBS: O sorted, SEMPRE retorna uma lista com os elementos do iteravel ordenados


----------------------------------------------------------------------------------------------------------------------------

# Exemplo 

numeros = {6, 1, 24, 5, 7, 8}

print(numeros)

print(sorted(numeros)) #Ordenar do maior para o menor

print(numeros)

----------------------------------------------------------------------------------------------------------------------------

# ADICIONANDO PARAMETROS AO sorted()


numeros = {6, 1, 24, 5, 7, 8, 30, 41} 


print(sorted(numeros, reverse= True)) #Ordena do maior para o menor

----------------------------------------------------------------------------------------------------------------------------



# Podemos utilizar o sorted() para coisas mais complexas


usuarios = [
    {"username": "Samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "Matheus", "tweets": ["Eu adoro bolo de chocolate"]},
    {"username": "Emmanuel", "tweets": ["Quero ir para a academia ", "Ficar monstrao pohaa", "Let's go"]}
]


print(sorted(usuarios, key= lambda usuario: usuario["username"]))

"""

musicas = [
    {"nome": "ThunderStuck", "tocou": "3"},
    {"nome": "Billie Jean", "tocou": "8"},
    {"nome": "Simple Man", "tocou": "5"}
]

# Ordena da mais tocada para a menos tocada

print(sorted(musicas, key = lambda musica : musica["tocou"], reverse=True))
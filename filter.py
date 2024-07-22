"""
FILTER

    SERVE PARA FILTRAR DADOS DE UMA DETERMINADA COLEÇÃO



import statistics

# dados coletados de algum sensor

dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]


# Calculando a média dos dados utilizando a função mean()

media = statistics.mean(dados)

print(f'Media: {media}') # Output: 2.183333333333333

#OBS: Assim como a função map(), a filter() recebe dois parametros, sendo
#Uma função e um iteravel

res = filter(lambda valor: valor > media, dados)
print(list(res))
    
------------------------------------------------------------------------------

paises = ['', 'Argentina', '', 'Brasil', 'Chile', 'Colombia', '', 'Equador']


print(paises)

res = filter(None, paises)

print(list(res))


# A diferença entre map() e filter() é:

# map() -> recebe dois parametros, uma função e um iteravel, e retorna um objeto mapeando a funcao para cada elemento do iteravel

# filter() -> Recebe dois parametros, uma funcao e um iteravel e retorna um objeto filtrando apenas os elementos de acordo com a funcao

#filter: SEMPRE RETORNA True ou False (booleanos)

#map: sempre retorna valores, que nao sejam booleanos

------------------------------------------------------------------------------
# EXEMPLOS MAIS COMPLEXOS

# filtrar os usuarios que estao inativos no twitter

# Filtrando por uma lista vazia

# for usuario in usuarios:
#     if usuario["tweets"] > []:
#         print(usuario)

------------------------------------------------------------------------------

#Filtrando por tamanho dos tweets
for usuario in usuarios:
    if len(usuario["tweets"]) > 0 :
        print(usuario)

------------------------------------------------------------------------------

# filtrando por funcao filter()
        
# inativos = list(filter(lambda usuario: len(usuario["tweets"]) == 0, usuarios))

# print(inativos)



usuarios = [
    {"Username": "Matheus", "tweets":["Aquela smoke, aquela maldita smoke", "O problema mesmo é o macaco"]},
    {"Username": "Caio", "tweets":["Eu amo meu macaco"]},
    {"Username": "Emmanuel", "tweets":["Vagabundo quer perder peso, mas não quer descansar KKKKKKK", "Acabou o time nessa poha"]},
    {"Username": "Thales", "tweets":["Emmanuel é muito chato pprt", "Mlk ta meia hora falando do treino do Zarak pqp"]},
    {"Username": "Zarak", "tweets":[]},
    {"Username": "Kaka", "tweets":[]}
]




# forma 2: filtrando por filter() com negacao "not"

inativos = list(filter(lambda usuario: not usuario["tweets"] == 0, usuarios))

print(inativos)

------------------------------------------------------------------------------

"""

# Combinar filter() e map()

nomes = ['Matheus', 'Caio', 'Kaka', 'Thales', 'Emmanuel', 'Zarak']


lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))

print(lista)

"""
Mapas -->  Conhecidos em Python como Dicionários


Dicionários em Python são representados por chaves {}



# iterar sobre dicionarios

for chave in receita:
    print(chave)


for chave in receita:
    print(receita[chave])


for chave in receita:
    print(f'Em {chave} recebi R$ {receita[chave]}')




# ACESSANDO AS CHAVES

print(receita.keys())

for chave in receita.keys():
    print(receita[chave])



#acessando os valores

print(receita.values())

for valor in receita.values():
    print(valor)



# DESCOMPACTANDO DICIONARIOS


for chave, valor in receita.items():
    print(f'chave={chave} e valor={valor}')
"""


receita = {'jan': 100, 'fev': 250, 'mar': 400}


print(receita)

# SOMA*, VALOR MAXIMO* , VALOR MINIMO*, TAMANHO

# * SE OS VALORES FOREM TODOS INTEIROS OU REAIS


print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita.values()))







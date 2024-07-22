"""
Modulo Collections - Counter

Colletcions -> High Performance Container Datetypes

Counter -> Recebe interavel como parametro e cria um objeto do tipo Collections Counter que é parecido com um dicionario
contendo como chave um elemento da lista passada como parametro e como valor a quantidade de ocorrencias dese elemento

"""

# Realizando o Import

from collections import Counter


                                   # Podemos utilizar qualquer iteravel, aqui usamos uma lista
"""
lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4, 4, 5, 5, 5, 5, 3, 45, 45, 66, 66, 43, 34]

# Utilizando Counter

res = Counter(lista)
print(type(res))
print(res)
"""
# Counter({1: 5, 3: 5, 2: 4, 5: 4, 4: 3, 45: 2, 66: 2, 43: 1, 34: 1})
# Veja que, para cada elemento da lista o Counter criou uma chave e colocou como valor a quantidade de ocorrencias

texto = "O rato roeu a roda da rainha da Inglaterra"

palavras = texto.split()
#print(palavras)

res = Counter(palavras)
print(res)

                                # Econtrando as 5 palavras com mais ocorrencias no texto
print(res.most_common(5))




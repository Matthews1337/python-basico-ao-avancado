"""
Conjuntos

 - Conjuntos dem qualquer linguagem de programação, estamos fazendo referencia à teoria dos cnjuntos da matemática

  - Aqui no Python, os conjuntos são chamados de Sets.

Dito isto, da mesma forma que na matemática:

 - Sets (Conjuntos) não possuem valores deplicados;
 - Sets (conjuntos) não possuem valores ordenados;
 - Elementos não são acessados via índice, ou seja, conjuntos não são indexados;

Conjuntos são bons para se utilizar quando precisamos armazenar elementos
mas não nos importamos com a ordenação deles. Quando não precisamos se preocupar
com chaves, valores e itens duplicados.


Os conjuntos (Sets) são referenciados em Python com chaves {}

Diferença entre conjuntos (set) e mapas (dicionarios) em Python:
    - Um dicionário tem chave/valor:
    - Um conjunto tem apenas valor:




# Definido um conjunto:

# Forma 1

s = set({1, 2, 3, 4, 5, 5,  6, 7, 2, 3})  #REPARE QUE TEMOS VALORES REPETIDOS.

print(s)
print(type(s))

# OBS: Ao criar um conjunto, caso seja adicionado um valor ja existente, o mesmo
# Será ignorado sem gerar error e não fará parte do conjunto.

# Forma 2 - Mais comum

s = {1, 2, 3, 4, 5, 5}

print(s)
print(type(s))

# Podemos verificar se determinado elemento está contido no conjunto

if 3 in s:
    print("tem o 3")
else:
    print('nao tem o 3')



s = set({1, 2, 3, 4, 5, 5,  6, 7, 2, 3})

# Importante lembrar que, além de não termos valores duplicados, não temos ordem


dados = '99, 2, 34, 23, 2, 12, 1, 44, 5, 34'

# Listas aceitam valores duplicados, então temos 10 elementos
lista = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
print(f'lista: {lista} com{len(lista)} elementos')

# Tuplas aceitam valores duplicados, então temos 10 elementos
tupla = (99, 2, 34, 23, 2, 12, 1, 44, 5, 34)
print(f'tupla: {tupla} com {len(tupla)} elementos')

#Dicionarios não aceitam valores duplicados, então temos 8 elementos
dicionario = {}.fromkeys([99, 2, 34, 23, 2, 12, 1, 44, 5, 34], 'dict')
print(f'dicionario: {dicionario} com {len(dicionario)} elementos')

# Conjuntos não aceitam valores duplicados, então temos 8 elementos
conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}
print(f'conjunto: {conjunto} com {len(conjunto)} elementos')




# Assim como todo outro conjunto Python podemos colocar tipos de dados misturados em Sets


s = {1, 'b', True, 34.22, 44}
print(s)
print(type(s))

# Podemos iterar em um set normalmente

for valor in s:
    print(valor)




# USOS INTERESSANTES COM SETS

# Imagine que fizemos um formulario de cadastro de visitantes em uma feira ou museu e os visitantes
#informam manualmente a cidade de onde vieram.

# Nos adicionamos cada cidade em uma Lista Python, ja que em uma Lista podemos adicionar novos elementos
#e ter repetiçao.

cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiaba', 'São Paulo', 'Campo Grande', 'Cuiaba']
print(cidades)
print(len(cidades))

# Agora precisamos saber quantas cidades distintas, ou seja, unicas, temos

# O que voce faria? Faria um loop na lista....?

# Podemos utilizar o set para isso

print(len(set(cidades)))



                                           # Adicionando elementos em um conjunto

s = {1, 2, 3}
s.add(4)
s.add(4) # Duplicidade não gera erro, simplesmente é ignorado
print(s)


s = {1, 2, 3}
print(s)
# Forma 1

s.remove(3) # Não é indice! Informamos o valor a ser removido.
print(s)

# OBS: Caso o valor não seja encontrado será gerado o erro KeyError. Nenhum valor é retornado.

# Forma 2

s.discard(2)

print(s)

#OBS: Se o valor não for encontrado, nenhum erro é gerado.



# Podemos remover todos os itens de um conjunto
s.clear()
print(s)



                                             # Forma 2 - Shallow Copy

novo.add(4)

print(novo)
print(s)



                                                # FORMA 1 - Deep Copy

novo = s.copy()
print(novo)

novo.add(4)

print(novo)
print(s)





# Copiando um conjunto para outro...


s = {1, 2, 3}
print(s)


                                             # Métodos matemáticos de conjuntos

# Imagine que temos dois conjuntos: Um contendo estudantes do curso Python e um
# Contendo estudantes do curso de Java


estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

# Veja que alguns alunos que estudam Python também estudam Java.

# Precisamos gerar um conjunto com nomes de estudantes unicos

#                                                   Forma 1 -  Utilizando union

unicos = estudantes_python.union(estudantes_java)
unicos1 = estudantes_java.union(estudantes_python)
print(unicos)
print(unicos1)


                                                  # FORMA 2 - UTILIZANDO O CARACTERE PIPE |

unicos2 = estudantes_python | estudantes_java

print(unicos2)


# GERAR UM CONJUNTO DE ESTUDANTES QUE NAO ESTAO NO OUTRO CURSO

so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)


"""

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

#  Gerar um conjunto de estudantes que estao em ambos os cursos

                                  # forma 1 - utilizando o Intersection
"""
ambos1 = estudantes_java.intersection(estudantes_python)
print(ambos1)
"""


                                   # Forma 2 - Utilizando o &
"""
ambos2 = estudantes_java & estudantes_python

print(ambos2)
"""


                               # Gerar um conjunto de estudantes de um curso que nao estao no outro
"""
so_python = estudantes_python.difference(estudantes_java)
print(so_python)
"""



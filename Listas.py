"""
Listas em Python funcionam como vetores / matrizes (arrays) em outras linguagens, com a diferença de serem dinamicos
e tambem podemos colocar QUALQUER tipo de dado.


Linguagens C/Java: Arrays
    - Possuem tamanho e tipo de dado fixo;
    ou seja, nestas linguagens se voce criar um array do tipo int e com tamnaho 5, este array sera SEMPRE do tipo inteiro
    e podera ter SEMPRE no maximo 5 valores.

 - Dinamico: Nao possuem tamanho fixo; ou seja, podemos criar a lista e simplesmente ir adicionando elementos;

 - Qualquer tipo de dado: Nao possuem tipo de dado fixo; ou seja, podemos colocar qualquer tipo de dado;

 As listas em Python sao representadas por colchetes: []



 #Podemos facilmente checar se determinado valor esta contido na lista

num = 7

if num in lista4:
    print(f'encontrei o numero {num}')
else:
    print(f'nao encontrei o numero {num}')

# Podemos facilmente ordenar uma lista

lista1.sort()
print(lista1)


                         # Podemos facilmente contar o numero de ocorrencias de um valor em uma lista

print(lista1.count(1))
print(lista5.count("e"))

# Adicionar elementos em listas

"""
                            # Para adicionar elementos em listas, utilizamos a função append

"""

print(lista1)
lista1.append(42)
print(lista1)

"""
                             # OBS: Com append, nós so condeguimos  adicionar 1 elemento por vez
"""
# lista1.append(42, 12, 8)



lista1.append([8, 3, 1])  #Coloca a lista como elemento unico (sublista)
print(lista1)

if [8, 3, 1] in lista1:
    print('encontrei a lista')
else:
    print('nao encontrei a lista')


lista1.extend([123, 44, 67])  # Coloca cada elemento da lista como valor adicional a lista
print(lista1)

                              # Podemos facilmente inverter uma lista

# FORMA 1

# lista1.reverse()
# lista2.reverse()


# FORMA 2

# print(lista1[::-1])
# print(lista2[::-1])

# COPIAR UMA LISTA

# lista6 = lista2.copy()


                             # PODEMOS CONTAR QUANTOS ELEMENTOS EXISTEM DENTRO DA LISTA

# print(len(lista5))


                            #  PODEMOS REMOVER FACILMENTE O ULTIMO ELEMENTO DE UMA LISTA
# OBS : O pop nao somente remove o ultimo elemento mas tambem o retorna

print(lista5)
lista5.pop()
print(lista5)


#  PODEMOS REMOVER UM ELEMENTO PELO INDICE
# OBS: OS ELEMENTOS Á DIREITA DESTE INDICE SERAO DESLOCADOS Á ESQUERDA
# OBS: SE NAO HOUVER ELEMENTO NO INDICE INFORMADO, TEREMOS O ERRO IndexError

lista5.pop(2)
print(lista5)


                                #  PODEMOS REMOVER TODOS OS ELEMENTOS (ZERAR A LISTA)

print(lista5)
lista5.clear()
print(lista5)


                                   # PODEMOS FACILMENTE REPETIR ELEMENTOS EM UMA LISTA

nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)


                                   #  PODEMOS CONVERTER UMA STRING PARA UMA LISTA

# EXEMPLO 1


curso = 'Programação em Python: Essencial'
print(curso)
curso = curso.split()
print(curso)


                                   # OBS: por padrao, o split separa os elementos da lista pelo espaço entre elas.


# Exemplo 2

curso = 'Programação em Python: Essencial'
print(curso)
curso = curso.split(',')
print(curso)



                                   # CONVERTENDO UMA LISTA EM UMA STRING

lista6 = ['Programação', 'em', 'Python:', 'Essencial']
print(lista6)

# Abaixo estamos falando: pega a lista6, coloca espaço entre cada elemento e transforma em uma string

curso = ' '.join(lista6)
print(curso)


# Abaixo estamos falando: pega a lista6, coloca im cifrão entre cada elemento e transforma em uma string
curso = '$'.join(lista6)

                                    # ITERANDO SOBRE LISTAS

# EXEMPLO 1 - utilizando for

soma = 0

for elemento in lista4:
    print(elemento)
    soma = soma + elemento
print(soma)
"""

type([])

lista1 = [1, 99, 2, 4, 7, 8, 10, ]

lista2 = ['M', 'a', 't', 'h', 'e', 'u', 's', '', 'f', 'o', 'n', 's','e', 'c', 'a']

lista3 = []

lista4 = list(range(11))

lista5 = list('Matheus Fonseca')

"""
# EXEMPLO 2 UTILIZANDO WHILE

carrinho = []
produto = ''


while produto != 'sair':
    print("Adicione algo no carrinho ou digite 'Sair' para sair")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)
"""

"""
                                        # UTILIZANDO VARIAVEIS EM LISTAS

numeros = [1, 2, 3, 4, 5]
print(numeros)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]
print(numeros)
"""


                                         # FAZEMOS ACESSO AOS ELEMENTOS DE FORMA INDEXADA


#          0       1       2       3
cores = ['verde, amarelo, azul, branco']

"""
print(cores[0]) #verde
print(cores[1]) #amarelo
print(cores[2]) #azul
print(cores[3]) #branco

                                        # Fazer acesso aos elementos de forma indexada inversa

print(cores[-1]) #branco
print(cores[-2]) #azul
print(cores[-3]) #amarelo
print(cores[-4]) #verde
print(cores[-5]) #erro, pois nao existe indice
"""
"""
for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1
"""

                                          # GERAR INDICE EM UM FOR
""""""
for indice, cor in enumerate(cores):
    print(indice, cor)
"""

# OUTROS METODOS NAO TAO IMPORTANTES MAS TAMBEM UTEIS

                                       # ENCONTRAR O INDICE DE UM ELEMENTO NA LISTA

numeros = [5, 6, 7, 5, 5, 8, 9, 10]

# Em qual indice da lista esta o valor 6?
#print(numeros.index(6))


# Em qual indice da lista está o valor 9 ?
#print(numeros.index(9))

# OBS: Caso nao tenha este elemento na lista, sera dado erro ValueError

# print (numeros.index(19)) #gera ValueError


# OBS: Retorna o indice do primeiro elemento encontrado
#print(numeros.index(5))

# Podemos fazer busca dentro de um range, ou seja, qual indice começar a buscar
""""""
print(numeros.index(5, 1))  #buscando a partir do indice 1
print(numeros.index(5, 2))  #buscando a partir do indice 2
print(numeros.index(5, 3))  #buscando a partir do indice 3
print(numeros.index(5, 4))  #buscando a partir do indice 4
"""
# OBS: Caso nao tenha este elemento na lista, sera apresentado erro ValueError

# podemos fazer busca dentro de um range, inicio/fim

"""
print(numeros.index(8, 3 ,6)) #buscar o indice do valor 8 entre os indices 6 a 8
"""

# Revisão de slicing

# Listas[inicio:fim:passo]
# Range(inicio:fim:passo)

#lista = [1, 2, 3, 4]

#print(lista[1:])  #Iniciando no indice 1 e pegando todos os elementos restantes

# Trabalhando com slice de lista com o parametro "fim"
""""""
print(lista[:2]) #começa em 0, pega até o indice 2 - 1 (nao inclui o indice 2)
print(lista[:4]) #comeca em 0, pega até o 4 - 1
print(lista[1:3]) #começa em 1, pega até o 3 - 1
"""

"""                                                    # INVERTENDO EM UMA LISTA
"""
nomes = ['Geek', 'University']

nomes[0], nomes[1] = nomes[1], nomes[0]
print(nomes)
"""

# Soma*, Valor Maximo*, Valor minimo*, Tamanho

# * Se os valores forem todos inteiros ou reais

lista = [1, 2, 3, 4, 5, 6]

print(sum(lista)) #soma
print(max(lista)) #maximo valor
print(min(lista)) #minimo valor
print(len(lista)) #tamanho da lista

                                        # Transformar uma lista em tupla

lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))



                                       # Desempacotamento de listas

lista = [1, 2, 3]

num1, num2, num3 = lista

print(num1)
print(num2)
print(num3)

# OBS: Se tivermos um numero de elementos na lista ou variaveis para receber os dados, teremos ValueError


# Copiando uma lista para outra (Shallow Copy e Deep Copy)

# Forma 1 Deep Copy

lista = [1, 2, 3]
print(lista)

nova = lista.copy()

print(nova)

nova.append(4)

print(lista)
print(nova)

# Veja que ao utilizarmos lista.copy() copiamos os dados da lista para uma nova lista, mas elas
# Ficaram totalmente independentes, ou seja, modificando uma lista, nao afeta a outra. isso em Python
# é chamado de Deep Copy (cópia profunda)

# Forma 2 - shallow copy

lista = [1, 2, 3]
print(lista)

nova = lista  #Copia

print(nova)

nova.append(4)

print(lista)
print(nova)

# Veja que utilizamos a cópia via atribuição dados da lista para a nova lista, mas
# após realizar modificação em uma das listas, essa modificação se refletiu em ambas as listas.
# Isso em Python é chamado de Shallow Copy.
"""

Listas aninhadas (Nested lists)
 - Algumas linguagens de programação possuem uma estrutura de dados chamadas de arras:
    - Unidimensionais (Arrays/Vetores);
    - Multidimensionais (Matrizes);


Em Python nós temos as Listas

numeros = [1, 'b', 3.14, True, 5]


# Exemplos

listas = [[1, 2, 3], 
          [4, 5, 6], 
          [7, 8, 9]]  #Matriz 3 x 3

print(listas)

print(type(listas))

# Como fazemos para acessar os dados?

print(listas[0])  # pega somente a primeira lista [1, 2, 3,]

print(listas[0][2])  # pega o numero "3" da primeira lista



# Exemplos

# Iterando com loops em uma lista aninhada

for lista in listas:
    for num in lista:
        print(num)

#list comprehension

[[print(valor) for valor in lista] for valor in listas]


# Exemplos

# Iterando com loops em uma lista aninhada

for lista in listas:
    for num in lista:
        print(num)

#list comprehension

[[print(valor) for valor in lista] for valor in listas]

"""




# outros exemplos

# gerando um tabuleiro/matriz 3x3

# tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
# print(tabuleiro)

# # gerando jogadas para o jogo da velha

# velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)]

# print(velha)

# # grando valores iniciais

# print([['*' for i in range(1, 4)] for j in range(1, 4)])




def matriz_bidimensional(x, y, default= 0):
    return [[default for i in range (x)]for j in range (y)]

def multiplicacao_matriz(x, y):
    return [[ [i*j] for j in range (y)] for i in range (x)]



# mult = multiplicacao_matriz(3, 4)
# print(mult)


#print(matriz_bidimensional(3, 2))


x = int(input("Digite a quantidade de linhas"))
y = int(input("Digite a quantidade de colunas"))


matriz = [[ 0 for j in range (y)] for i in range(x)]

print(matriz)







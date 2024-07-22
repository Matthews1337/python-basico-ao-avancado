"""
- Algumas linguagens de programaçao (c/java) possuem uma estrutura de dados chamadas de arrays:
    - Unidimensionadas (arrays/vetores);
    - Multidimensionais (matrizes);


Em Python nós temos as Listas

numeros = [1, 'B', 3.14, True, 5]




                                                       # Exemplos

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Matriz 3 x 3

print(listas)
print(type(listas))

                                        # como fazemos para acessar os dados?

print(listas[0])   # acessa o indice 0
print(listas[0][1])   # acessa o indice 0, coluna 1

print(listas[2][1])  # acessa o indice 2, coluna 1


                                        # Iterando com loops em uma lista alinhada

for lista in listas:
    print(lista)


for lista in listas:
    for num in lista:
        print(num)


# List Comprehension

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Matriz 3 x 3

[[print(valor) for valor in lista] for lista in listas]


# Outros exemplos

# Gerando um tabuleiro/matriz 3x3

tabuleiro = [[numero for numero in range(1, 4)]for valor in range(1, 4)]
print(tabuleiro)

# gerando jogadas para o jogo da velha

velha = [['x' if numero % 2 == 0 else '0' for numero in range(1, 4)]for valor in range(1, 4)]
print(velha)



"""


"""
nome= input ("seu nome ? ")
idade= input ("idade.   ? ")
sexos =["m","f","o"]
sexo = input ("qual seu sexo ? ")

while sexo in sexos:
    print("passou", sexo)
print("Escolha uma das opcoes: m, f, o ")
sexo=input("qual seu sexo ? ")
"""



"""
def pessoa():
    nome = input('digite o seu nome: \n')
    idade = int(input('digite a sua idade: \n'))
    sexo = input('qual o seu sexo? M, F, O : \n')
    if sexo == 'm':
        sexo = 'masculino'
    elif sexo == 'f':
        sexo = 'feminino'
    else:
        sexo = 'outro'
    return f'{nome}, {idade} anos, sexo {sexo}'
print(pessoa())
"""
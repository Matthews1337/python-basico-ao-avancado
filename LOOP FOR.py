"""
loop for

Loop -> Estrutura de repetição
For -> Uma dessas estruturas

Utilizamos Loops para iterar sobre sequencias ou sobre valores iteraveis

Exemplos de iteraveis:

- String
    nome = 'Geek University'
- Lista
    Lista = [1, 3, 5, 7, 9]

- Range
    numero = range[1, 10]

#Exemplo de for 1 (iterando uma string)
for letra in nome:
    print(letra)

#Exemplo de for 2 (iterando sobre uma lista)

for numero in lista:
    print(numero)

#Exemplo de for 3 (iterando sobre um range)

for numero in range(1, 10):
    print(numero)
"""
"""
nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10) # O range nao pega o valor final "10"
soma = 0
qtd = int(input('quantas vezes esse loop dever rodar?'))

for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma = soma + num
print(f'A soma é {soma}')
"""


#1 Faça um programa que determine e mostre os cinco primeiros multiplos de 3
# considerando numeros maiores que 0
"""
for num in range(3, 18, 3):
    print(num)

"""


# 2 Escreva um programa que escreva na tela de 1 até 100, de 1 em 1, 3 vezes. A primeira vez
#deve usar a estrutura de repetição FOR, a segunda WHILE, e a terceira DO WHILE.

"""
for x in range(3):
    for num in range(1, 100+1):
        print(num)
        
"""
"""
numero = 1

while numero <=100:
    print(numero)
    numero = numero + 1
"""

# 3 Faça um algoritmo utilizando o comando while que mostra uma contagem regressivana tela,
# iniciando em 10 e terminando em 0. Mostrar uma mensagem "FIM"! apos a contagem

"""
numero = 10


while numero >= 1:
    print(numero)
    numero = numero -1
print("FIM")

"""

# 4 Escreva um programa que declare um inteiro, inicialize-o com 0, e incremente-o de 1000 em 1000
#imprimindo seu valor na tela, até que seu valor seja 100000

"""
numero = 0

for num in range(0, 100000 +1000, 1000):
    print(num)
"""

# 5 Faça um programa que peça ao usuario para digitar 10 valores e some-os
"""
soma = 0

vezes = int(input('digite quantos numeros vc quer somar'))

for rep in range(1, vezes+1):
    num = int(input(f'Informe o valor {rep}/{vezes} : '))
    soma = soma + num
print(f'a soma dos valores deu {soma}')
"""
'''
soma = 0

for rep in range(1, 10+1):
    num = int(input(f'informe os {rep} valores'))
    soma = soma + num
print(soma)
'''

# 6 Faça um programa que leia 10 inteiros e imprima sua média
'''
media = 0

for qtd in range(1, 10+1):
    num = int(input(f'Coloque os seus resultados : '))
    media = media + num / 10
print(media)

'''

# 7 Faça um programa que leia 10 inteiros positivos, ignorando não positivos e imprima sua média
"""
somatoria = 0


for x in range(10):
    num = int(input(f'digite {x+1}º numeros'))
    if num > 0:
        somatoria = somatoria + num
        media = somatoria / 10
    else:
        print('valor invalido')
else:
    print(f'a media é: {media}')
"""


# 8 Escreva um programa que leia 10 numeros e escreva o menor valor lido e o maior valor lido



#9 Faça um programa que leia N numeros e imprima os N primeiros numeros naturais impares.
"""
n = int(input('digite um valor N:\n'))    # \n serve para escrever na linha de baixo

i = 0

while i < n:
    print(2 * i + 1)
    i = i + 1      # i = 0 +1;  i = 1 + 1 = 2 (previne um loop infinito)
"""
#1 - 2*0 + 1 = 1
#2 - 2*1 + 1 = 3
#3 - 2*2 + 1 = 5
#4 - 2*3 + 1 = 7
#5 - 2*4 + 1 = 9


# 10 Faça um programa que calcule e mostre a soma dos 50 primeiros números pares
"""
qtd = 50
num = 1
while num <= qtd:
    num = num +1
    soma = qtd * (qtd + 1)
print(soma)
"""

# 11 Faça um programa que leia um numero inteiro positivo N e imprima todos os numeros naturais de 0 até N em ordem crescente
"""
n = int(input('Digite um numero N:\n'))


for numeros in range(0, n):
    print(numeros)
"""

# 12 faça um programa que leia um numero inteiro positivo N e imprima todos os numeros naturais de 0 até N em ordem decrescente

"""
n = int(input('Digite um numero N:\n'))
inicio = 0


while inicio <= n:
    print(n)
    n = n - 1
"""

# 13 Faça um programa que leia um numero inteiro positivo par N e imprima todos os numeros pares de 0 até N em ordem cescente
"""
qtd = int(input('Digite um numero N:\n'))
n = 0
total = int(qtd / 2)
"""
"""
for numeros in range(0, total+1):
    print(2 * n)
    n = n + 1
"""


# Com loop while
"""
while n <= total:
    print(2 * n)
    n = n + 1
"""
# quantidade = int(input("Digite um Número: \n"))
# n = 0

# for n in range(0, quantidade +1):
#     if n % 2 == 0:
#         print(f'O número {n} é par')
#     else:
#         print(f'O número {n} é ímpar')



# def impar_par(quantidade):
#     # quantidade = int(input("Digite um Número: \n"))
#     for n in range(0, quantidade +1):
#         if n % 2 == 0:
#             print(f'O número {n} é par')
#         else:
#             print(f'O número {n} é ímpar')
# impar_par(10)


# def impar_par(quantidade):
#     if quantidade % 2 == 0:
#         print(f'O número {quantidade} é par')
#     else:
#         print(f'O número {quantidade} é ímpar')
# impar_par(10)
# impar_par(20)
# impar_par(15)


frase = "olá joão"

palavra = "olá"

if palavra not in frase:
    print(f"A palavra {palavra} não está na frase!")
else:
    print(f"A palavra {palavra} está na frase!")

    








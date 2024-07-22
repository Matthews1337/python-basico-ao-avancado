"""
Estruturas logicas : and (e), or (ou), not (nao, is (é)

Operadores unários :
    - not ;

Operadores binários :
    - and , or , is

Regras de funcionamento :

Para o 'and' , ambos os valores precisam ser True
Para o 'or' , um ou outro valor precisa ser True
Para o 'not' , o valor do booleano é invertido , ou seja , se for True, vira False, e vice versa
Para o 'is' o valor é comparado com um segundo.

"""

#ativo = True
#logado = True


#if ativo and logado:
   # print('Bem-vindo')
#else:
    #print('Voce precisa ativar sua conta')

 # Faça um programa que receba dois numeros e mostre qual deles pe maior
"""
numero1 = int(input('coloque um numero'))

numero2 = int(input('coloque outro numero'))

if numero1 > numero2 :
    print('numero 1 é maior que o numero 2')
else:
    print('numero 2 é maior que numero 1')
"""

#Leia um numero fornecido pelo usuario. Se esse numero for positivo
#calcule a raiz quadrada do numero. Se o numero for negativo, mostre uma mensagem dizendo que o numero é invalido
"""
numero = float(input('ponha um numero'))
raiz = numero ** 0.5

if numero > 0:
    print(f'A raiz quadrada de {numero} é {raiz}')
else:
    print('numero invalido')
"""

#Leia um numero real. Se o numero for positivo imprima a raiz quadrada. DO contrario imprima o numero ao quadrado

"""
num = float(input('coloque um numero'))
raiz = num ** 0.5
numqdrd = num ** 2

if num > 0:
    print(f'a raiz quadrada de {num} é {raiz}')
else:
    print(f'o numero {num} ao quadrado é -{numqdrd}')
"""


#Faça um programa que leia um numero e, caso ele seja positivo, calcule e mostre:
    # O numero digitado ao quadrado
    # A raiz quadrada do numero digitado
'''
num = int(input('digite um numero'))
quadrado = num ** 2
raiz = num ** 0.5
if num > 0:
    print(f'o numero {num} ao quadrado é {quadrado}')
    print(f'a raiz quadrada do {num} é {raiz}')

'''

# Faça um programa que receba um numero inteiro e verifique se este numero é par ou impar
'''
num = int(input('digite um numero'))

resultado = num % 2

if resultado == 0:
    print('este numero é par')
elif resultado != 0:
    print('este numero é impar')
'''

#6 - #Escreva um programa que, dados dois numeros inteiros, mostre na tela o maior deles, assim como a diferença existente entre ambos
'''
num1 = int(input('digite um numero'))
num2 = int(input('digite outro numero'))
diferenca = num1 - num2
diferenca2 = num2 - num1
if num1 > num2:
    print(f'o numero {num1} é maior que  {num2} por {diferenca}')
elif num2 > num1:
    print(f'o numero {num2} é maior que {num1} por {diferenca2}')
'''

#7 #Faça um programa que receba dois numeros e mostre o maior. Se por acaso, os dois forem iguais,imprimir "numeros iguais"

""""
num1 = int(input("Digite um numero"))
num2 = int(input("Digite outro numero"))

if num1 > num2:
    print(f'o numero {num1} é maior que o numero {num2}')
elif num1 < num2:
    print(f'o numero {num2} é maior que o numero {num1}')
else:
    print('os dois numeros sao iguais')
"""

#8 Faça um programa que leia 2 notas de um aluno, verifique se as notas sao validas e exiba na tela a media destas notas
#Uma nota valida deve ser, obrigatoriamente,  um valor entre 0.0 e 10.0,
#Onde caso a nota nao possua valor valido, este fato deve ser informado
"""
nota1 = float(input('Coloque a sua nota'))
if (nota1 > 10) or (nota1 < 0):
    print('valor invalido')
nota2 = float(input('coloque a sua nota'))
if (nota2 > 10) or (nota2 < 0):
    print('valor invalido')

media = (nota1 + nota2) / 2
print(media)"""

"""
def verificar_valor(nota):
    if (nota > 10) or (nota < 0):
        raise Exception('valor invalido')



nota1 = float(input('coloque a sua nota'))
verificar_valor(nota1)
nota2 = float(input('coloque a sua nota'))
verificar_valor(nota2)
media = (nota1 + nota2) /2
print(media)
"""

#9 Leia o salario de um trabalhador e o valor da prestação de um emprestimo
#se a prestaçao for maior que 20% do salario imprima: Emprestimo nao concedido
#Caso contrario imprima: Emprestimo concedido.

"""
prestacao = float(input('digite sua prestacao'))
salario = float(input('digite seu salario'))
porcentagem = salario * (20 / 100)

#se a prestaçao for maior que a porcentagem

if porcentagem < prestacao:
    print('emprestimo nao concedido')
else:
    print('emprestimo concedido')
"""


#10 Faça um programa que receba a altura e o sexo de uma pessoa
#e mostre seu peso ideal, utilizando as seguintes formulas
#(onde h corresponde a altura)

#homens: (72.7 *h) - 58

#mulheres: (62.1 *h) - 44.7

"""
sexo = input('Digite seu sexo (H ou M): ')
h = float(input('altura'))

if sexo == "H":
    peso = (72.7 * h) - 58
elif sexo == "M":
    peso = (62.1 * h) - 44.7
print(f"O peso ideal é {peso}")
"""







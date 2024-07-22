"""
Entendendo o *args

 - O *args é um parametro como outro qualquer. Isso significa que você poderá chamar de qualquer coisa, desde que comece
com asterisco.

Exemplo:

*xis

Mas por convenção, utilizamos *args para defini-lo


Mas o que é o *args?

o parametro *args utilizado em uma função, coloca os valores extras informados como entrada em uma tupla. Então dede ja
lembre-se que tuplas sao imutaveis.


                                             # Exemplos


def soma_todos_numeros(num1=1, num2=2, num3=3, num4=4):
    return num1 + num2 + num3 + num4

print(soma_todos_numeros(4, 5, 6))

print(soma_todos_numeros(4, 6))

print(soma_todos_numeros(4, 6, 9, 5))




                                              # Entendendo o args

def soma_todos_numeros(nome, email, *args):
    return sum(args)

print(soma_todos_numeros('Angelina', 'Jolie'))
print(soma_todos_numeros('Angelina', 'Jolie', 1))
print(soma_todos_numeros('Angeline', 'Jolie', 1, 2))
print(soma_todos_numeros('Angeline', 'Jolie', 1, 2, 4))
print(soma_todos_numeros('Angeline', 'Jolie', 1, 2, 4, 7))




                                             # Outro exemplo de utilização do *args

def verifica_info(*args):
    if 'Geek'in args and 'University' in args:
        return 'Bem-vindo geek'
    return 'Eu não sei quem você é'

print(verifica_info())
print(verifica_info(1, 'University', True, 'Geek'))
print(verifica_info(1, 'University', 3.145))

"""

def soma_todos_numeros(*args):
    return sum(args)


numeros = [1, 2, 3, 4, 5, 6, 7]

# Desempacotador

print(soma_todos_numeros(*numeros))

# OBS: O asterisco serve para que informemos ao Python que estamos
#passando como argumento uma coleção de dados. desta forma, ele saberá
#que precisará antes desempacotar estes dados


# Exemplo de args

def data_de_nascimento(nome, *args):
    print('nome: ', nome)
    for data in args:
        print('ano:', data)


print(data_de_nascimento("Matheus", '1997'))
print(data_de_nascimento('Emanuel', '1998'))
"""
Funções com Parametros (de entrada)

 - Funçoes que recebem dados para serem processados sentro da mesma:

Se a gente pensar em um programa qualquer, geralmente temos:

entrada -> processamento -> saida

se a gente pensar em uma funçao, ja sabemos que temos funçoes que:
 - Não possuem entrada:
 - Não possuem saida:
 - Possuem entrada mas nao possuem saida:
 - Não possuem entrada ma posuem saida:
 - Possuem entrada e saida:




                                                 # Refatorando uma função

def quadrado(numero):
    # return numero * numero
    return numero ** 2


print(quadrado(7))
print(quadrado(2))
print(quadrado(5))

ret = quadrado(6)

print(ret)

print(quadrado()) # TypeError





                                            # Refatorando a função

def cantar_parabens(aniversariante):
    print('Parabens pra voce')
    print('nessa data querida')
    print('muitas felicidades')
    print('muitos anos de vida')
    print(f'viva o {aniversariante}')

cantar_parabens('marcos')


# Funçoes podem ter n parametros de entrada. Ou seja, podemos receber como entrada
# em uma funçao quantos parametros forem necessarios. Eles sao separados por virgula

# Exemplo

def soma(a, b):
    return a + b


def multiplica(num1, num2):
    return num1 * num2


def outra(num1, b, msg):
    return (num1 + b) * msg

print(soma(2, 5))
print(soma(10, 20))


print(multiplica(4, 5))
print(multiplica(2, 8))


print(outra(3, 2, 'geek '))
print(outra(5, 4, 'matheus '))

# OBS: Se a gente informar um numero errado de parametros ou argumento, teremos TypeError

# print(soma(4))         # TypeError - Passando argumentos a menos

# print(soma(2, 3, 4))   # TypeError - Passando argumentos a mais
# print(soma(4))   # TypeError - passando argumentos a menos




                                            # Nomeando parametros

def nome_completo(nome, sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}'

print(nome_completo('Matheus', 'Fonseca'))

# A diferença entre paramentros e argumentos

# Parametros sao variaveis declaradas na definição de uma funçao;
# Argumentos sao dados passados durante a execução de uma função;

# A ordem dos parametros importam

nome = 'Matheus'
sobrenome = 'Fonseca'

print(nome_completo(sobrenome, nome))  #Inverte


# Argumentos nomeados (Keyword Arguments)

# Caso utilizemos nomes dos parametros nos argumentos para informa-los, podemos
# Utilizar qualquer ordem.


print(nome_completo(nome='Matheus', sobrenome='Fonseca'))
print(nome_completo(sobrenome='Fonseca', nome='Matheus'))
print(nome_completo(nome=nome, sobrenome=sobrenome))


"""


# Erro comum na utilizaçao do return

def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
        return total              # o retorno finaliza a função


"""
           # Forma correta
def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total    <---- fora do loop
"""


lista = [1, 2, 3, 4, 5, 6, 7]
print(soma_impares(lista))



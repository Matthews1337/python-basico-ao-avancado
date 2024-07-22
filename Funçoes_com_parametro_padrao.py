"""
Funções com parametros padrão (Default Parameters)

 - Funções onde a passagem de parametros seja opcional;


# Exemplo de função onde a passagem de parametro seja opcional
print('geek university')

print()




                            # Exemplo de função onde a passagem de parametro seja obrigatoria

def quadrado(numero):
    return numero ** 2

print(quadrado(3))
print(quadrado())   # TypeError




def exponencial(numero, potencia=2):
    return numero ** potencia

print(exponencial(2, 3))   # 2 * 2 * 2 = 8
print(exponencial(3, 2))   # 3 * 3 = 9

print(exponencial(3))   # Por padrão eleve ao quadrado
print(exponencial(3, 5))  # Eleva a potencia informada pelo usuario

# OBS
# Se o usuario passa somente um argumento, este sera atribuido ao parametro numero, e sera calculado o quadrado deste numero
# Se o usuario passar dois argumentos, o primeiro sera atribuido ao parametro numero e o segundo ao parametro potencia.
# Entao sera calculada esta potencia




     # OBS: Em funçoes Python, os parametros com valores default (padrao) DEVEM sempre estar ao final da declaraçao.

# ERRO!
def teste(num=2, potencia):
    return num ** potencia

print(teste(6))


# CERTO!

def teste(potencia, num=2):
    return num ** potencia

print(teste(6))


# Outros exemplos

def soma(num1, num2):
    return num1 + num2

print(soma(4, 3))
print(soma(4))   # TypeError
print(soma())    # TyperError




                                         # Exemplo mais complexo


def mostra_informacao(nome='Geek', instrutor=False):
    if nome =='Geek' and instrutor:
        return 'Bem-vindo instrutor Geek'
    elif nome == 'Geek':
        return 'Eu pensei que você era o instrutor'
    return f'Olá {nome}'

print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao(True))
print(mostra_informacao('Ozzy'))
print(mostra_informacao(nome='Matheus'))


# Por quê utilizar parametros com valor default?

 - Nos permite ser mais flexiveis nas funções;
 - Evita erros com parametros incorretos;
 - Nos permite trabalhar com exemplos mais legiveis de codigo;


# Quais tipos de dados podemos utilizar como valores default para parametros?

 - Qualquer tipo de dado:
    - Numeros, Strings, floats, booleanos, listas, tuplas, dicionarios, funçoes e etc;




# Exemplos

def soma(num1, num2):
    return num1 + num2

def mat(num1, num2, fun=soma):
    return fun(num1, num2)

def subtracao(num1, num2):
    return num1 - num2

print(mat(2, 3))
print(mat(2, 2, subtracao))


# Escopo - Evitar problemas e  confusoes...

# Variaveis globais
# Variaveis locais


instrutor = "Geek"     # variavel global


def diz_oi():
    instrutor = 'Python'    # variavel local
    return f'oi {instrutor}'


print(diz_oi())

#OBS: Se tivermos uma variavel local com o mesmo nome de uma variavel global, a local tera preferencia



def diz_oi():
    prof = 'Geek'     # Variavel local
    return f'Olá {prof}'


print(diz_oi())
print(prof)     # Name Error



# Atenção com variaveis globais (e puder evitar, evite)


total = 0

def incremental():
    total = total + 1      #Unbound local error
    return total

print(incremental())

total = 0

def incremental():
    global total    # AVISANDO QUE QUEREMOS A VARIAVEL GLOBAL
    total = total + 1
    return total

print(incremental())
print(incremental())
print(incremental())

"""

# Podemos ter funçoes que sao declaradas dentro de funçoes, e tambem tem uma forma especial de escopo de variavel


def fora():
    contador = 0

    def dentro():
        nonlocal contador

        contador = contador + 1
        return contador
    return dentro()


print(fora())
print(fora())
print(fora())

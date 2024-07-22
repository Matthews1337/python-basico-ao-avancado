"""
Assertions (afirmações/checagens/questionamentos)

Em Python utilizamos a palavra reservada 'assert' para realizar simples afirmações utilizadas nos testes

Utilizamos o 'assert' em uma expressão que queremos checar se é valida ou não.
Se a expressão for verdadeira retorna None e caso seja falsa levanta um erro do tipo AssertionError

# OBS: Nós podemos especificar, opcionalmente, um segundo argumento ou mesmo uma mensagem de erro personalizada.

# OBS: A palavra 'assert' pode ser utilzada em qualquer funçao oi codigo nosso ... nao precisa ser exclusivamente nos testes


# Alerta: Cuidado ao utilizar 'assert'

Se um programa Python for executado com o parametro -O, nenhum assertion será validado. Ou seja, todas as suas validades ja era

"""


def soma_numeros_positivos(a, b):
    assert a > 0 and b > 0 , 'Ambos números precisam ser positivos'
    return a + b

ret = soma_numeros_positivos(2, 4) #6
# ret = soma_numeros_positivos(-2, 4) # Ambos números precisam ser positivos

print(ret)


def comer_fast_food(comida):
    assert comida in ['Hamburguer', 'Pizza', 'Sorvete', 'cachorro quente', 'batata frita'], 'A comida precisa ser fast food'
    return f'Eu estou comendo {comida}'


comida = 'Hamburguer'

print(comer_fast_food(comida))




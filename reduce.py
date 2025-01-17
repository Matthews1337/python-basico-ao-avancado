"""
REDUCE

OBS: A partir do Python versao 3 a função reduce() não é mais uma funcao built-in.

Agora temos que importar e utilizar essa funcao a partir do modulo 'functools'

Guido Van Rossum: Utilize a funcao reduce() se voce realmente precisa dela. Em todo caso, 99% das vezes um loop for é mais legivel


Para entender o reduce()

# Imagine que voce tem uma colecao de dados:


dados = [a1, a2, a3, a4]

# E voce tem uma funcao que recebe 2 parametros:

def funcao(x, y):
    return x + y

    
Assim como map() e filter(), a funcao reduce() recebe 2 parametros: a funcao e o iteravel

reduce(funcao, dados)



A funcao reduce(), funciona da seguinte forma:
    passo 1 - res1 = f(a1, a2) # Aplica a funcao nos dois primeiros elementos da colecao e guarda o resultado
    passo 2 - res2 = f(res1, a3) # Aplica a funcao passando o resultado do passo1 mais o terceiro elemento e guarda o resultado


isso é repetido até o final.
Passo 3: res3 = f(res2, a4)


passo n: resn = f(resm, an)



ou seja, em cada passo ela aplica a funcao passando como primeiro argumento o resultado da aplicacao anterior, No final, reduce() 
ira retornar o resultado final


Alternativamente, poderiamos ver a funcao reduce() como:
funcao(funcao(funcao(a1, a2)a3, a4), ...), an


"""


from functools import reduce

dados = [2, 3, 4, 5, 6, 7, 8, 9, 10]

# Para utilizar o reduce() precisamos de uma funcao que receba 2 parametros


multi = lambda x,  y: x * y
res = reduce(multi, dados)
print(res) 


# Utilizando um loop normal

res = 1

for n in dados:
    res = res * n

print(res)
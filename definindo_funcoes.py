"""
Definindo Funções

 - Funções são pequenos trechos de códigos que realizam tarefas específicas:
 - Pode ou nao receber entradas de dados e retornar uma saida de dados:
 - Muito uteis para executar procedimentos similares por repetidas vezes:

 OBS: SE voce escrever uma funcao que realiza varias tarefas dentro dela
 é bom fazer uma verificaçao para que a funçao seja simplificada

Já utilizamos várias funções desde que iniciamos este curso:
- print()
- len()
- max()
- min()
- count()
- e muitas outras
"""

# Exemplo de utilizaçao de funçoes:

#cores = ['verde', 'amarelo', 'azul', 'braco']

# Utilizando a funçao integrada (built-in) do Python print()

#print(cores)

#curso = 'Programação em Python: Essencial'

#print(curso)

#cores.append('roxo')

#print(cores)

#curso.append('mais dados...' # AttributeError
#print(curso)

#cores.clear()
#print(cores)


# DRY - Don't Repeat Yourself - Não repita voce mesmo/ Não repita seu codigo

# Mas entao, como definir funçoes?
"""
Em Python, a forma geral de definir uma funçao é:

def nome_da_funçao(parametros_de_entrada):
    bloco da funçao


onde:

nome_da_funcao -> SEMPRE, com letras minusculas, e se for nome completo, separado por underline:

parametros_de_entrada -> Opcionais, onde tendo mais de um, cada um separado por virgula, podendo ser opcionais ou nao:

bloco_da_funçao -> tambem chamado de corpo da funçao ou implementaçao, e onde o processamento da funçao acontece.
neste bloco, pode ter ou nao retorno da funçao.

OBS: Veja que para definir uma funçao, utilizamos a palavra reservada 'def' informando ao Python que estamos definind ouma funçao 
tambem abrimos o bloco de codigo com o ja conhecido dois pontos : que é utilizado em Python para definir blocos
"""
# Definindo a primeira funçao

def diz_oi():
    print('diz oi!')

"""
OBS:

1 - veja que, dentro das nossas funcoes podemos utilizar outras funçoes:
2 - veja que nossa funçao so executa 1 tarefa, ou seja, a unica coisa que ela faz e dizer oi
3 - veja que esta funçao nao recebe nenhum parametro de entrada
4 - veja que esta funçao nao retorna nada

"""

# Utilizando funçoes

# chamada de execuçao
diz_oi()

"""
ATENÇÃO: 

Nunca esqueça de utilizar os parenteses ao executar uma funçao

Exemplo:

# Errado!

diz_oi

# Certo

diz_oi()

"""

def cantar_parabens():
    print('Parabens pra voce')
    print('nessa data querida')
    print('muitas felicidades')
    print('muitos anos de vida')
    print('viva o aniversariante')

#cantar_parabens()

#for n in range(5):
    #cantar_parabens()


# Em Python, podemos inclusive criar variaveis do tipo de uma funçao e executar esta funçao atraves da variavel

cantar = cantar_parabens

cantar()


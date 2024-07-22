PEP8

[1] - utilize Camel Case para nomes de classes

class Calculadora:
    pass


class CalculadoraCientifica:
    pass


[2] - Utilize nomes em minusculo, separados por underline para funções ou variaveis:

def soma():
    pass


def soma_dois():
    pass


numero = 4

numero_impar = 5


[3] - utilize 4 espaços para identação! (NO USE TAB)


if 'a' in 'banana':
    print('tem')


[4] - linhas em branco

- Separar funções e definições de classe com duas linhas em branco:
_ Métodos dento de uma classe devem ser separados com uma unica linha em branco:


[5] -Imports

- Imports devem ser sempre feitos em linhas separadas:

# Import ERRADO

import sys , os

# Import CERTO

import sys
import os

# Não há probelemas em utilizar:

from types import StringType, ListType

# Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:

from types import (
    StringType,
    ListType,
    SetType,
    OutroType
)

# Imports devem ser colocados no topo do arquivo, logo depois de quaisquer comentarios ou docstrings
# antes de constantes ou variaveis e intruçoes


[6] - Espaços em expressoes e instruçoes

# Nao faça:

função( algo[ 1 ]), { outro: 2 } )

# FAÇA

funçao(algo[1]), {outro: 2})


# NAO FAÇA

algo (1)

# FAÇA

algo(1)


[7] - Termine sempre uma instruçao com uma nova linha

Ex:

print('algo')

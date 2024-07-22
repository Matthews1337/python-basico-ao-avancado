"""
Escopo de variaveis

Dois casos de escopo

1 - Variaveis globais;
     - Variaveis globais sao reconhecidas, ou seja , seu escopo compreende todo o programa.


2 - Variaveis locais;
    -variaveis locais sao reconhecias apenas no bloco onde foram declaradas, ou seja , seu escopo
    esta limitado ao bloco onde foi declarada.


para declarar variaveis em Python fazemos:

nome_da_variavel = valor_da_variavel
"""

numero = 21


if numero > 10:
    novo = numero + 10 # a variavel esta declarada dentro do bloco if. portanto, é local
    print(novo)

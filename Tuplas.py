"""
Tuplas (tuple)

Tuplas são bastante parecidas com listas

Existem basicamente duas diferenças básicas:

1 - As tuplas são representadas por parenteses ()

2 - As tuplas são imutáveis: isso significa que ao se criar uma tupla ela nao muda. Toda operação em uma tupla gera uma nova tupla


# CUIDADO 1 : As tuplas são representadas por (), mas veja:

tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)

print(type(tupla1))


tupla2 = 1, 2, 3, 4, 5, 6,
print(tupla2)

print(type(tupla2))


# CUIDADO 2 : Tuplas com 1 elemento

tupla3 = (1)  # Não é uma tupla

print(tupla3)

print(type(tupla3))


tupla4 = (1,) # É uma tupla

print(tupla4)

print(type(tupla4))


tupla5 = 2,

print(tupla5)

print(type(tupla5))


# CONCLUSÃO: PODEMOS CONCLUIR QUE TUPLAS SÃO DEFINIDAS PELA VIRGULA E NÃO PELO USO DO PARENTESES

(4) -> Não é uma tupla
(4,)-> É uma tupla
4, -> É uma tupla



#podemos gerar uma tupla dinamicamente com range (inicio, fim, passo)

tupla = tuple(range(11))
print(tupla)
print(type(tupla))


# Desempacotamento de tupla

tupla = ('Geek University', 'Programação em Python: Essencial')

escola, curso = tupla

print(escola)
print(curso)

# Gera erro (ValueError) se colocarmos um numero diferente de elementos para desempacotar.

# Métodos para adição e remoçao de elementos nas tuplas não existem, dado o fato das tuplas serem imutaveis


# SOMA* , Valor Máximo*, Valor Mínimo* e tamanho

# * Se os valores forem dados inteiros ou reais


tupla = (1, 2, 3, 4, 5, 6)

print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))


# CONCATENAÇÃO DE TUPLAS

tupla1 = (1, 2, 3)
print(tupla1)

tupla2 = (4, 5, 6)
print(tupla2)

print(tupla1 + tupla2)  #Tuplas são imutaveis

print(tupla1)
print(tupla2)


tupla3 = tupla1 + tupla2
print(tupla3)

tupla1 = tupla1 + tupla2 # Tuplas sao imutaveis mas podemos sobrescrever seus valores


# VERIFICAR SE DETERMINADO ELEMENTO ESTA NA TUPLA

tupla = (1, 2, 3)

print(3 in tupla)


# ITERANDO EM TUPLA


tupla = (1, 2, 3)

for n in tupla:
    print(n)


for indice, valor in enumerate(tupla):
    print(indice, valor)



# CONTANDO ELEMENTOS DENTRO DE UMA TUPLA

tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b')

print(tupla.count('c'))

escola = tuple('Geek university')
print(escola)

print(escola.count('e'))



# DICAS NA UTILIZAÇÃO DE TUPLAS

# DEVEMOS UTILIZAR TUPLAS SEMPRE QUE NAO PRECISARMOS MODIFICAR OS DADOS CONTIDOS EM UMA COLEÇAO

        # EXEMPLO 1


meses =  ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')


# O ACESSO A ELEMENTOS DE UMA TUPLA TAMBÉM É SEMELHANTE A DE UMA LISTA

print(meses[5])


   # ITERAR COM WHILE
i = 0

while i < len(meses):
    print(meses[i])
    i = i + 1

# VERIFICAMOS EM QUAL INDICE UM ELEMENTO ESTA NA TUPLA

print(meses.index('Junho'))


# OBS: CASO O ELEMENTO NAO EXISTA, SERA GERADO ValueError.



# SLICING

# tupla[inicio:fim:passo]

print(meses[5:9])



"""

meses =  ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')




# POR QUE UTILIZAR TUPLAS?

# - TUPLAS SÃO MAIS RAPIDAS DO QUE LISTAS.
# - TUPLAS DEIXAM SEU CODIGO MAIS SEGURO*

# *ISSO PORQUE TRABALHAR COM ELEMENTOS IMUTAVEIS TRAZ SEGURANÇA PARA O CODIGO


# COPIANDO UMA TUPLA PARA OUTRA

tupla = (1 ,2 ,3)
print(tupla)

nova = tupla # NA TUPLA NAO TEMOS O PROBLEMA DE SHALLOW COPY
print(nova)
print(tupla)

outra = (4, 5, 6)

nova = nova + outra

print(nova)
print(tupla)



"""
Ranges

 - Precisamos conhecer o Loop For para usar ranges.
 - Precisamos conhecer o range para trabalhar melhor com loops for.

 Ranges são utilizados para gerar sequencias numericas, nao de forma aleatoria,
 mas sim de maneira especificada.

 Formas gerais :
 # Forma 1

 range(valor_de_parada)
 OBS: Valor_de_parada nao inclusive (inicio padrao 0, e passo de 1 em 1)


# Forma 2
range(valor_de_inicio, valor_de_parada)
OBS: valor_de_parada nao inclusive (inicio especificado pelo usuario, e passo de 1 em 1)


# Forma 3

range(valor_de_inicio, valor_de_parada, passo)
OBS: Valor de parada nao inclusive (inicio especificado pelo usuario, e passo especificado pelo usuario)

# Forma 4 (inverso)

range(valor_final, valor_de_inicio, passo)

OBS: Valor de parada nao inclusive (inicio especificado pelo usuario, e passo especificado pelo usuario)

"""

# Forma 1
"""
for num in range(11):
    print(num, end='')

"""

# Forma 2
""""
for num in range(4, 11):
    print(num)
"""

# Forma 3
"""
for num in range(0, 20, 3):
    print(num)
"""

# Forma 4
"""
for num in range(10 , 0, -1):
    print(num)
"""


"""
saindo de loops com break

Funciona da mesma forma que nas linguagens C ou Java

Utilizamos o break para sair de loops de maneira projetada

"""

# Exemplo 1
"""
for numero in range(1, 11):
    if numero == 6:
        break
    else:
        print(numero)
print('sai do loop')
"""


# Exemplo 2

while True:
    comando = input('digite para sair: ')
    if comando == "sair":
        break
    else:
        print('digite "sair" ')
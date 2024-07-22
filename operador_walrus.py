"""
O operador Walrus permite fazer a atribuição e retorno de valor em uma única expressão.


variavel := expressao

"""


# sem operador walrus

nome = "Matheus"
print(nome)


# com operador walrus

print(nome := 'Matheus')

# Python 3.7

cesta = []

# fruta = input('Informe a fruta: ')
# 
# while fruta != 'jaca':
    # cesta.append(fruta)
    # fruta = input('Informe a fruta: ')



# Python 3.8


while(fruta := input('Informe a fruta: ')) != 'jaca':
    cesta.append(fruta)




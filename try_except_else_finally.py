"""
DICA DE QUANDO E ONDE TRATAR O CODIGO

TODA ENTRADA DEVE SER TRATADA!

"""

num = None

try:
    num = int(input("informe um numero: \n"))
except ValueError as e:
    print(f"erro voce digitou um valor {num} incorreto do tipo {type(num)}")




try:
    num = int(input("informe um numero: \n"))
except ValueError as e:
    print(f"erro voce digitou um valor {num} incorreto" )
finally:
    print("executando o finally")

# OBS: O finally geralmente é utilizado para fechar ou desalocar recursos
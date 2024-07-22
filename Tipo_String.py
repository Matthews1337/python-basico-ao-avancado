"""
Em Python , um dado é considerado tipo String sempre que:

- Estiver entre aspas simples -> 'uma string', '234' , 'True' , '42.7'

- Estiver entre aspas Duplas ->  "uma string", "234" , "True", "42.7"

- Estiver entre aspas simples triplas -> '''uma string''', '''234''' , '''True''' , '''42.7'''

"""
# - Estiver entre aspas duplas triplas -> """uma string""", """234""", """True""" , """42.7"""

"""
nome = "Matheus"
print(nome)
print(type(nome))

nome = "Abreu's cabaré"
print(nome)
print(type(nome))  

"""
# [0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10, 11 ,12, 13 ,14
# [M , A , T , H , E , U , S ,' ', F , O , N , S , E , C , A
"""
nome = 'Matheus Fonseca'
print (type(nome))
print (nome[0:7])
"""

# [::-1] -> comece do primeiro elemento  va ate o ultimo elemento e inverta
"""
nome = 'Matheus Fonseca'
print (nome[::-1])
"""

nome = 'abreu mama o matheus'
# print (nome.upper())  # poe todas as letras em maiuscula

# print (nome.lower())  # poe todas as letras em minuscula

# print (nome.split())  # Separa todas as palavras


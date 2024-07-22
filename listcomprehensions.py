# List Comprehension 

# PRIMEIRAMENTE TEMOS QUE SETAR UMA NOVA VARIAVEL PARA PODER ARMAZENAR AS INFORMAÇOES
# LOGO DEPOIS COLOCAM0S O QUE QUEREMOS FAZER, POR EXEMPLO MULTIPLICAR OU PEGAR UM ELEMENTO DE UM OBJETO



# minha_lista = [1, 2, 3]

# double =[item * 2 for item in minha_lista]
#  for item in minha_lista:
#     double.append(item * 2)
# print(double)



# users = [{'nome': 'Matheus','idade': 25 }, {'nome': 'Caio','idade': 23 }, {'nome': 'Pedro','idade': 21 }]

#  user_name = [usuario['nome'] for usuario in users]


# user_name = [usuario['nome'] for usuario in users if usuario ['idade'] > 22 ]

# print(user_name)


# user_groups = [
#     [
#         {'nome': 'Matheus', 'idade': 25},
#         {'nome': 'Caio', 'idade': 23}
#     ],
#     [
#         {'nome': 'Emmanuel', 'idade': 20},
#         {'nome': 'Luan', 'idade': 26}
#     ],
#     [
#         {'nome': 'Pedro', 'idade': 30},
#         {'nome': 'Tripinha', 'idade': 28}
#     ]
# ]

# person = [pessoa['nome'] for group in user_groups for pessoa in group if pessoa['idade'] > 23 ]

# print(person)











x = 1
y = 1
z = 1
n = 2



list = [[i,j,k] 
        for i in range(0, x+1)
        for j in range(0, y+1)
        for k in range(0, n+1)
        if i+j+k !=n
        ]
print(list)
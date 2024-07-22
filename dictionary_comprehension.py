"""
Dictionary comprehension


                                                             EXEMPLOS:

                                                             
numeros = [1, 2, 3, 4, 5]

quadrados = {valor: valor ** 2 for valor in numeros}

print(quadrados)


-------------------------------------------------------------------------------------------

numeros = {'a': 2, 'b': 3, 'c': 4, 'd': 5}

quadrados = {chave: valor ** 2 for chave, valor in numeros.items() }

print(quadrados)

-------------------------------------------------------------------------------------------


chaves = "abcde"
valor = [1,2,3,4,5]

mistura = {chaves[i]: valor[i] for i in range(0, len(chaves))}

print(mistura)

-------------------------------------------------------------------------------------------




"""
# EXEMPLO COM LOGICA CONDICIONAL

numeros = [1, 2, 3, 4, 5]

res = {num: ('par' if num % 2 == 0 else 'impar')for num in numeros}

print(res)
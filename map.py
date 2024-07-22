"""
com MAP podemos fazer mapeamento de valores para funcao

def area(r):
    #Calcula a area de um circulo com raio 'r' 
    return math.pi * (r ** 2)

print(area(2))
print(area(5.3))

------------------------------------------------------------------------------

"""



import math


def area(r):
    #Calcula a area de um circulo com raio 'r' 
    return math.pi * (r ** 2)

print(area(2))
print(area(5.3))


raios = [2, 5, 7.1, 0.3, 10, 44]

# forma comum

areas = []

for r in raios:
    areas.append(area(r))

print(areas)



# FORMA 2 - MAP


# MAP É UMA FUNCAO QUE RECEBE DOIS PARAMETROS: O PRIMEIRO A FUNCAO, O SEGUNDO UM ITERAVEL. RETORNA UM MAP OBJECT


areas = map(area, raios)

print(areas)

print(type(areas))


print(list(areas))

# forma 3 - Map com Lambda

print(list(map(lambda r: math.pi * (r ** 2), raios)))

#OBS: APOS UTILIZAR A FUNCAO MAP(), DEPOIS DA PRIMEIRA UTILIZACAO DO RESULTADO, ELE ZERA



# EXEMPLO

valores = [1, 2, 3, 4, 5, 6]

def mult(valor):
    vl_mult = valor * 10
    return vl_mult

nvos_valores = list(map(mult, valores))

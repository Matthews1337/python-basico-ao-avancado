"""
1 - Escolha um numero de 0 a 10
2 - Caso chute um numero baixo o programa deve avisar para chutar mais alto
3 - Caso chute um numero alto o programa deve avisar para chutar mais baixo
4 -  caso acerte o numero, o programa deve recomeçar
5 - caso erre o numero o programa deve pedir pro usuario tentar novamente
"""

import random


x = random.randint(1, 10)
y = int(input('ADIVINHE O NUMERO'))
print(x)


while True:
    if x > y:
        print("chute mais alto")
    elif x < y:
        print('chute mais baixo')
    else :
        print(f'parabens vc acertou', {x})


















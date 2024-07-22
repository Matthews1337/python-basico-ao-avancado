"""
POO - O método super()

O método super() se refere á super classe

"""

class Animal:
    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especie = especie

    def faz_som(self, som):
        print(f'{self.__nome} faz {som}')

    
class Gato(Animal):

    def __init__(self, nome, especie, raca):
        super().__init__(nome, especie)
        self.__raca = raca




animal1 = Gato('Garfield', 'Persa', 'Negra')
animal1.faz_som('miau')

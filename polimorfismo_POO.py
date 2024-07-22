"""
POO - Polimorfismo

poli = muitas
morfo = formas

polimorfismo = muitas formas


"""


class Animal:
    def __init__(self, nome):
        self.__nome = nome

    def falar(self):
        raise NotImplementedError('Classe filha deve implementar este método.')
    
    def comer(self):
        print(f'{self.__nome} está comendo.')


class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} está latindo.')


class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} está miando.')


class Rato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} está falando') # Aqui se da o polimorfismo, todos os animais estão falando algo diferente

# Testes


garfield = Gato('Garfield')

garfield.comer()
garfield.falar()


pluto = Cachorro('Pluto')

pluto.comer()
pluto.falar()


mickey = Rato('Mickey')

mickey.comer()
mickey.falar() # NotImplementedError , Precisa-se implementar o metodo na classe Rato, como nas outras classes
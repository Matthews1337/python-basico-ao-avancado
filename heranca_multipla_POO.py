"""
POO - Herança multipla 

Herança múltipla nada mais é do que a possibilidade de uma classe herdar de múltiplas classes,
fazendo com que a classe herde todos os atributos e métodos de todas as classes herdadas.

#OBS: A herança múltipla pode ser feita de duas maneiras:
    - Por multiderivação Direta;
    - Por multiderivação Indireta.

"""

# Exemplo 1 : Multi derivação direta

class Base1:
    pass

class Base2:
    pass

class Base3:
    pass

class MultiDerivada(Base1, Base2, Base3):
    pass



# Exemplo 2 : Multi derivação indireta


class Base1:
    pass

class Base2(Base1):
    pass

class Base3(Base2):
    pass

class MultiDerivada(Base3): # Está herdando as bases 1 e 2 indiretamente
    pass




class Animal:
    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f'Olá, eu sou {self.__nome}!'
    


class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self._nome} está nadando.'
    
    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} do mar'
    

class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    
    def andar(self):
        return f'{self._nome} está andando.'
    
    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} da terra'
    

class Pinguim(Terrestre, Aquatico): # Pela lei da Method Resolution Order (MRO) o método cumprimentar que será gerado primeiro é o da classe Terrestre, justamente pq é o primeiro

    def __init__(self, nome):
        super().__init__(nome)

    



alex = Pinguim('Alex')

print(alex.cumprimentar()) # Printou o cumprimentar() da classe Terrestre 


print(f'Tux é instância de Pinguim?  {isinstance(alex, Pinguim)}') # True
print(f'Tux é instância de Aquatico?  {isinstance(alex, Aquatico)}') # True
print(f'Tux é instância de Terrestre?  {isinstance(alex, Terrestre)}') # True
print(f'Tux é instância de Animal?  {isinstance(alex, Animal)}') # True
print(f'Tux é instância de object?  {isinstance(alex, object)}') # True

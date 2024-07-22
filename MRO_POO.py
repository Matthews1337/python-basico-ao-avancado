"""
POO - MRO - Method Resolution Order


Method Resolution Order (Resolução de Ordem de Métodos), é a ordem de execução dos métodos (quem será executado primeiro).

Em Python, a gente pode conferir a ordem de execução dos métodos de 3 formas;
    - Via propriedade da classe __mro__
    - Via função built-in mro()
    - Via help

"""


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
    

class Pinguim(Aquatico,Terrestre): # Pela lei da Method Resolution Order (MRO) o método cumprimentar que será gerado primeiro é o da classe Terrestre, justamente pq é o primeiro

    def __init__(self, nome):
        super().__init__(nome)




alex = Pinguim('Alex')
'''
class Pinguim(Terrestre, Aquatico)
    pass


print(alex.cumprimentar()) # Printou o cumprimentar() da classe Terrestre 

'''
print(alex.cumprimentar()) # Printou o cumprimentar() da classe Aquatico

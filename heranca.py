"""
POO - Herança ( Inheritance)

A ideia de herança é de reaproveitar código. Tabém estender nossas classe.

OBS: Com a herança, a partir de uma classe existente, nós extendemos outra classe
que passa a herdar atributos e métodos da classe herdada.


Cliente
    - nome
    - sobrenome
    - cpf
    - renda

Funcionario
    - nome
    - sobrenome
    - cpf
    - matricula    

    

Perguntar: Existe alguma entidade (classe) genérica o suficiente para encapsular os atributos e métodos comuns a outras entidades?


OBS: Quando uma classe herda de outra classe ela herda todos os atributos e métodos da classe herdada

Quando uma classe herda de outra classe, a classe herdada é conhecida como:
    (Pessoa)
    - super Classe
    - Classe Mãe
    - Classe Pai
    - Classe base
    - Classe genérica

    
Quando uma classe herda de outra classe, ela é camada de :
    (Cliente, Funcionario)
    - Sub Classe
    - Classe Filha
    - Classe Específica







Sobrescrita de métodos (Overriding) ocorre quando reescrevemos/reimplementamos um método presente na super classe em classes filhas
"""


class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome} com o cpf: {self.__cpf}'





class Cliente(Pessoa):
    """
    Cliente herda de Pessoa
    """
    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda





class Funcionario(Pessoa):
    """
    Funcionario herda de Pessoa
    """
    def __init__(self,nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        # Pessoa.__init__(self, nome, sobrenome, cpf) # Forma nao comum de acessar dados da supeclasse
        self.__matricula = matricula

    # def nome_completo(self):
    #     return super().nome_completo() #Chamando o metodo nome_completo

    def nome_completo(self):
        return f'Funcionario: {self._Pessoa__nome} {self._Pessoa__sobrenome} com a matricula : {self.__matricula}'
    


cliente1 = Cliente(nome='Matheus', sobrenome='Fonseca', cpf='071.903.551.11',renda=4000)

funcionario1 = Funcionario(nome='Matheus', sobrenome='Fonseca', cpf='071.903.551.11', matricula=1)

print(funcionario1.nome_completo())
print(funcionario1._Pessoa__nome)

print(funcionario1.__dict__) # Podemos ver de qual classe vem os atributos
print(funcionario1.nome_completo()) 

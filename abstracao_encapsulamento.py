"""
POO -> Abstração e Encapsulamento

O grande objetivo da POO é encapsular nosso código dentro de um grupo lógico e hiearquico utilizando classes

Encapsular -> cápsula


                        Classe

|------------------------------------------------|
|                                                |
|                 Atributos e métodos            |
|                                                |
|------------------------------------------------|


# RELEMBRANDO Atributos/métodos privados em Python

Imagine que temos uma classe chamada Pessoa, contendo
um atributo chamado __nome e um metodo privado
chamado __falar()

Esses elementos privados so devem ser acessados dentro da classe.
Mas Python nao bloqueia este acesso fora da classe. Com Python acontece
um fenomeno chamado Name Mangling, que faz uma alteração na forma de se acessar os elementos privados, conforme:

_Classe__elemento

Exemplo - Acessando elementos privados fora da classe:

instancia._Pessoa__nome




# ABSTRAÇÃO, em POO é o ato de expor apenas dados relevantes de uma classe, escondendo atributos e métodos privados de usuário

# Encapsular -> privar o que não é importante para o usuário


"""



class Conta:
    contador = 100
    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador = self.__numero

    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}')

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("Valor precisa ser positivo")

    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
            else:
                print("Saldo insuficiente")
        else:
            print("Valor precisa ser positivo")

    def transferir(self, valor, conta_destino):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
                conta_destino.__saldo += valor
            else:
                print("Saldo insuficiente")
        else:
            print("Valor precisa ser positivo")
        print(f"Foi transferido o valor de {valor} para {conta_destino._Conta__titular}")
        print(f"Saldo atualizado: {self.__saldo}")



user1 = Conta('Matheus', 2000, 7000)
user2 = Conta('Caio', 6000, 10000)


user1.extrato()
user2.extrato()

user1.transferir(valor=250, conta_destino=user2)

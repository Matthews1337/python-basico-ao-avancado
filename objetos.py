"""
POO - Objetos

Objetos -> São instancias da classe. Ou seja, após o mapeamento do objeto do mundo real para a sua representação computacional, devemos poder criar quantos objetos forem necessarios
Podemos pensar nos objetos/ instancias de uma classe como variaveis do tipo definido na classe

"""


class Lampada:

    def __init__(self, cor, luminosidade, voltagem):
        self.__cor=cor
        self.__luminosidade=luminosidade
        self.__voltagem=voltagem
        self.__ligada=False
    


class ContaCorrente:
    contador = 4999

    def __init__(self, limite, saldo, cliente):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        self.__cliente = cliente
        ContaCorrente.contador = self.__numero
    
    def mostra_cliente(self):
        print(f"o nome do cliente é {self.__cliente._Usuario__nome}")
        print(f"o saldo do cliente {self.__cliente._Usuario__nome} {self.__cliente._Usuario__sobrenome} é de: {self.__saldo}")



class Usuario:
    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha



user1 = Usuario(nome='Matheus', sobrenome='Fonseca',email='Mat@hotmail.com',senha='123')

cc_user1 = ContaCorrente(cliente=user1,limite=7000,saldo=500)

cc_user1.mostra_cliente()
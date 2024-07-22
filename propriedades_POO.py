"""
POO - Propriedades - Properties


Em linguagens de pogramação como o Java, ao declararmos atributos privados nas classes, 
costumamos criar métodos públicos para manipulação desses atributos. Esses métodos
são conhecidos como getters e setters, onde os getters retornam o valor do atributo
e os setters alteram o valor do atributo.


"""



class Conta:
    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador = self.__numero

    @property # @property funciona como fossem os getters de java, dando possibilidade de acessar a propriedade diretamente
    def numero(self):
        return self.__numero
    """
    A diferença em usar a @property é que nao precisa de parametros, por exemplo:
    Conta1.numero() -> sem property
    Conta1.numero -> com property

    OBS: sempre que for usar @property, colocar os parametros do constructor como private, por exemplo (__nome)
    """


    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def limite(self):
        return self.__limite
    

    @limite.setter # para fazermos um setter, precisamos informar o nome do método .setter
    def limite(self, valor):
        self.__limite = valor


    @property # Também podemos usar as properties como atributos, por exemplo um atributo de valor total
    def valor_total(self):
        return self.__saldo + self.__limite
    

    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente {self.__titular}'
    
    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor

    def get_saldo(self):
        return self.__saldo
    



conta1 = Conta('Matheus', 5000, 7000)
conta2 = Conta('DjJean011', 10000, 20000)


print(conta1.extrato())
print(conta1.saldo)
print(conta1.limite)
conta1.limite = 15000
print(conta1.limite)
print(conta1.valor_total)


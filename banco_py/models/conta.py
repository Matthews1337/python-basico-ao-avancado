from models.cliente import Cliente

from utils.helper import formata_float_str_moeda

class Conta:

    codigo: int = 1000

    def __init__(self, cliente: Cliente) -> None:
        self.__numero = Conta.codigo
        self.__cliente = cliente
        self.__saldo = 0.0
        self.__limite = 100.0
        self.__saldo_total = self._calcula_saldo_total
        Conta.codigo += 1

    def __str__(self):
        return f" Número da conta: {self.numero} \nCliente: {self.cliente.nome} \nSaldo total: {formata_float_str_moeda(self.__saldo_total)}"
    
    @property
    def numero(self)-> int:
        return self.__numero
    
    @property
    def cliente(self)-> Cliente:
        return self.__cliente

    @property
    def saldo(self)-> float:
        return self.__saldo
    
    @saldo.setter
    def saldo(self, valor: float)-> None:
        self.__saldo = valor


    @property
    def limite(self)-> float:
        return self.__limite
    
    @limite.setter
    def limite(self, valor: float)-> None:
        self.__limite = valor
    

    @property
    def saldo_total(self)-> float:
        return self.__saldo_total 
    
    @saldo_total.setter
    def saldo_total(self, valor: float)-> None:
        self.__saldo_total = valor

    @property
    def _calcula_saldo_total(self)-> float:
        return self.__saldo + self.__limite
    
    


    def depositar(self, valor:float)-> None:
        if valor > 0:
            self.saldo = self.saldo + valor
            self.saldo_total = self._calcula_saldo_total
            print("Depósito efetuado com sucesso!")
        else:
            print("Erro ao tentar efetuar o depósito. Tente novamente!")


    def sacar(self,valor: float)-> None:
        if valor > 0 and self.saldo_total >= valor:
            if self.saldo >= valor:
                self.saldo = self.saldo - valor
                self.saldo_total = self._calcula_saldo_total
            else:
                restante: float = self.saldo - valor
                self.limite = self.limite + restante
                self.saldo = 0.0
                self.saldo_total = self._calcula_saldo_total
            print("Saque realizado com sucesso!")
        else:
            print("Saque não realizado. Tente novamente!")


    def transferir(self, conta_destino: object, valor: float)-> None:
        if valor > 0 and self.saldo_total >= valor:
            if self.saldo >= valor:
                self.saldo = self.saldo - valor
                self.saldo_total = self._calcula_saldo_total
                conta_destino.saldo = conta_destino.saldo + valor
                conta_destino.saldo_total = conta_destino._calcula_saldo_total
            else:
                restante: float = self.saldo - valor
                self.saldo = 0.0
                self.limite = self.limite + restante
                self.saldo_total = self._calcula_saldo_total
                conta_destino.saldo = conta_destino.saldo + valor
                conta_destino.saldo_total = conta_destino._calcula_saldo_total
            print("Tranferência realizada com sucesso!")                
        else:
            print("Transferência não realizada. Tente novamente!")
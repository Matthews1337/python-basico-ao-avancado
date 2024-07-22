"""
1 -  Crie uma classe pessoa, contendo nome, data de nascimento e email.
Crie as propriedades getter e setters para os atributos e um método para imprimir os dados de uma pessoa

"""
from datetime import date

class Pessoa:
    def __init__(self, nome: str, dt_nascimento: date, email: str):
        self.__nome: str = nome
        self.__dt_nascimento: date = dt_nascimento
        self.__email: str = email

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def dt_nascimento(self):
        return self.__dt_nascimento

    @dt_nascimento.setter
    def dt_nascimento(self, dt_nascimento: date):
        self.__dt_nascimento = dt_nascimento

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email


    
    def imprimir(self) -> None:
        print(f'Nome: {self.nome}')
        print(f'E-mail: {self.email}')
        print(f"Data Nascimento: {self.dt_nascimento.strftime('%d/%m/%Y')}")

    # def imprimir(self) -> None:
    #     print(self.__nome)



if __name__ == "__main__":
    pessoa1 = Pessoa(nome="Matheus", dt_nascimento=(date(1997, 10, 15)), email='mat_@hotmail.com')

    pessoa1.imprimir()


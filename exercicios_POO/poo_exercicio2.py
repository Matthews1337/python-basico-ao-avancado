"""
2 - Crie uma classe Agenda que pode armazenar contatos e seja possivel realizar as seguintes operações

    a) armazenar_contato(contato:contato)
    b) excluir_contato(contato:contato)
    c) buscar_contato(nome:str); //Informa em que posição da agenda está o contato
    d) imprimir_agenda(); //Imprime todos os contatos da agenda
    e) imprimi_contato(indice:int); // Imprime os dados do contato informado pelo índice

"""
from poo_exercicio1 import Pessoa
from datetime import date

class Agenda:

    

    def __init__(self):
        self.__contatos: list[Pessoa] = []
        
    @property
    def contatos(self) -> list[Pessoa]:
        return self.__contatos

    
    def armazenar(self, contato: Pessoa) -> None:
        self.contatos.append(contato)
        # print(f'{contato.nome} salvo com sucesso!')
        

    def excluir_contato(self, contato: Pessoa) -> None:
        self.contatos.remove(contato)
    
    
    
    def imprimir(self) -> None:
        print(f'Nome: {self.nome}')
        print(f'E-mail: {self.email}')
        print(f'Data Nascimento: {self.data_nascimento}')




    def buscar_contato(self, nome: str) -> None:
        for indice, contato in enumerate(self.contatos):
            if contato.nome == nome:
                print(f"O contato {nome} está na posição {indice} da agenda")

        
    

    def imprimir_agenda(self) -> None:
        for contato in self.contatos:
           contato.imprimir()


    def imprimir_contato(self, indice: int) -> None:
        self.contatos[indice].imprimir()

    


if __name__ == "__main__":
    contato1: Pessoa = Pessoa(nome="Abreu", dt_nascimento=date(1998, 5, 10),email="abreu@hotmail.com")
    contato2: Pessoa = Pessoa(nome="Thales", dt_nascimento=date(1998, 7, 20),email="thales@hotmail.com")
    contato3: Pessoa = Pessoa(nome="Pedro", dt_nascimento=date(1999, 2, 15),email="pedro@hotmail.com")

    agenda = Agenda()
    agenda.armazenar(contato1)
    agenda.armazenar(contato2)
    agenda.armazenar(contato3)

    agenda.imprimir_agenda()
    
    agenda.imprimir_contato(2)

    agenda.buscar_contato('Abreu')

    agenda.excluir_contato(contato3)



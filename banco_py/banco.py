from typing import List
from time import sleep

from models.cliente import Cliente
from models.conta import Conta


contas: List[Conta] = []

def main():
    menu()


def menu()-> None:
    print("""
=================Bem-Vindo=================
Selecione uma opção:
          1 - Criar Conta
          2 - Efetuar saque
          3 - Efetuar depósito
          4 - Efetuar transferência
          5 - Listar contas
          6 - Sair do sistema
""")
    
    opcao: int = int(input())

    if opcao == 1:
        criar_conta()
    elif opcao == 2:
        efetuar_saque()
    elif opcao == 3:
        efetuar_deposito()
    elif opcao == 4:
        efetuar_transferencia()
    elif opcao == 5:
        listar_contas()
    elif opcao == 6:
        print("Saindo do sistema...")
        sleep(1)
    else:
        print("Opção Inválida!")
        sleep(1)
        menu()


def criar_conta()-> None:
    print("Informe os dados do cliente: ")
    nome: str = input("Nome do cliente: ")
    email: str = input("Email do cliente: ")
    cpf: str = input("CPF do cliente: ")
    data_nascimento: str = input("Data de nascimento do cliente: ")

    cliente: Cliente = Cliente(nome=nome, email=email, cpf=cpf, data_nascimento=data_nascimento)

    conta: Conta = Conta(cliente)

    contas.append(conta)

    print("Conta criada com sucesso!")
    print("Dados da conta:")
    print(conta)
    sleep(1)
    menu()




def efetuar_saque()-> None:
    
    if len(contas) > 0:
        numero: int = int(input("Informe o número da sua conta: "))
        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor = float(input("Informe o valor do saque: "))
            conta.sacar(valor)
        else:
            print(f"Conta {numero} não foi encontrada!")
    else:
        print("Não há contas cadastradas!")
    sleep(1)
    menu()


def efetuar_deposito()-> None:
    if len(contas) > 0:
        numero: int = int(input("Informe o número da sua conta: "))
        conta: Conta = buscar_conta_por_numero(numero)
        if conta:
            valor = float(input("Informe o valor do depósito: "))
            conta.depositar(valor)
        else:
            print(f"Conta {numero} não foi encontrada!")
    else:
        print("Não há contas cadastradas")
    menu()


def efetuar_transferencia()-> None:
    if len(contas) > 0:
        numero_o: int = int(input("Informe o número da sua conta: "))
        conta_o: Conta = buscar_conta_por_numero(numero_o)
        if conta_o is not None:
            numero_d: int = int(input("Informe o número da conta para transferência: "))
            conta_d: Conta = buscar_conta_por_numero(numero_d)
            if conta_d is not None:
                valor: float = float(input("Infome o valor da transferência: "))
                conta_o.transferir(conta_d, valor)
                print(f"Transferência de {valor} realizada com sucesso!")
            else:
                print(f"Conta destino {numero_d} não foi encontrada!")
        else:
            print(f"A sua conta com número {numero_o} não foi encontrada!")
    else:
        print("Não há contas cadastradas!")
    sleep(1)
    menu()


def listar_contas()-> None:
    if len(contas) > 0:
        print("Listagem de contas")

        for conta in contas:
            print(conta)
            print("===============")
            sleep(1)

    else:
        print("Não existem contas cadastradas!")
    sleep(1)
    menu()


def buscar_conta_por_numero(numero: int)-> Conta:
    contaa: Conta = None

    if len(contas) > 0:
        for conta in contas:
            if conta.numero == numero:
                contaa = conta
        return contaa


if __name__ == "__main__":
    main()
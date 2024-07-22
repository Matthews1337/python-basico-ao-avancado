
from typing import List, Dict
from time import sleep
from models.produto import Produto
from utils.helper import formata_float_str_moeda

produtos: List[Produto] = []

carrinho: List[Dict[Produto, int]] = []

def main()-> None:
    menu()


def menu() -> None:
    print("""Selecione uma opção abaixo: 
1 - Cadastrar produto 
2 - Listar produto
3 - Comprar produto
4 - Visualizar carrinho
5 - Fechar pedido
6 - Sair do sistema
""")
    
    opcao: int = int(input())
    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produto()
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print("Saindo do sistema...")
        sleep(2)
        exit(0)
    else:
        print("Opção inválida. Tente novamente.")
        sleep(2)
        menu()
    

def cadastrar_produto()-> None:
    print("=======Cadastro de Produtos======= \n")

    nome: str = input("Informe o nome do produto: ")
    preco: float = float(input("Informe o preço do produto: "))

    produto: Produto = Produto(nome, preco)
    produtos.append(produto)

    print(f" O produto {Produto.nome} foi cadastrado com sucesso!!!")
    sleep(2)
    menu()


def listar_produto()-> None:
    if len(produtos) > 0:
        print("=======Lista de Produtos======= \n")
        for produto in produtos:
            print(produto)
            print('-----------------------')
            sleep(1)
    else:
        print("Não há produtos cadastrados")
    sleep(2)
    menu()

def comprar_produto()-> None:
    if len(produtos) > 0:
        print("Informe o código do produto que deseja adicionar ao carrinho: ")
        print('---------------------------------------------------------------')
        print("=================Produtos Disponíveis=================")
        for produto in produtos:
            print(produto)
            print("---------")
            sleep(1)
        codigo: int = int(input())
        produto: Produto = pega_produto_por_codigo(codigo)

        if produto != 0:
            if len(carrinho) > 0 :
                tem_no_carrinho: bool = False
                for item in carrinho:
                    quant: int = item.get(produto)
                    if quant > 0:
                        item[produto] = quant + 1
                        print(f"Quantidade: {item[produto]}")
                        tem_no_carrinho = True
                        sleep(2)
                        menu()
                if not tem_no_carrinho:
                    prod = {produto: 1}
                    carrinho.append(prod)
                    print(f"O produto {produto.nome} foi adicionado ao carrinho.")
                    sleep(2)
                    menu()
            else:
                item = {produto: 1}
                carrinho.append(item)
                print(f"O produto {produto.nome} foi adicionado ao carrinho.")
                sleep(2)
                menu()
        else:
            print(f"O produto com código {codigo} não foi encontrado!")
            sleep(2)
            menu()
    else:
        print("Não há produtos!!")

def visualizar_carrinho()-> None:
    if len(carrinho) > 0:
        print("Produtos no carrinho: ")
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                print('-----------------')
    else:
        print("Ainda não existem itens no carrinho!")
    sleep(2)
    menu()



def fechar_pedido()-> None:
    if len(carrinho) > 0:
        valor_total: float = 0
        print("Produtos do carrinho")
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f"Quantidade: {dados[1]}")
                valor_total += dados[0].preco * dados[1]
                print("=======================")
                sleep(1)
        print(f"Sua fatura é {formata_float_str_moeda(valor_total)} ")
        carrinho.clear()
        sleep(5)
    else:
        print("Não há produtos no carrinho")
    sleep(2)
    menu()


def pega_produto_por_codigo(codigo: int)-> Produto:
    p: Produto = None

    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
    return p


if __name__ == '__main__':
    main()
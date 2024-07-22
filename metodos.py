"""
POO - Métodos

Métodos (Funções) -> Representam os comportamentos do objeto. Ou seja, as ações que este objeto pode realizar no seu sistema

Em Python, dividimos os métodos, assim como os atributos, em 2 grupos: Métodos de instância e Métodos de classe

O método __init__ é um método especial chamado de construtor, ele é responsável por construir o objeto a partir da classe

OBS: Todo elemento em Python que inicia e finaliza com duplo underline, é chamado de dunder (double underline)

OBS: Os métodos/funções dunder em Python são chamados de métodos mágicos

"""
# Métodos de Instância

from passlib.hash import pbkdf2_sha256 as cryp

class Lampada:
    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False


class ContaCorrente:

    contador = 1234
    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id


class Usuario:
    def __init__(self, nome, email, senha):
        self.__nome = nome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds= 200000, salt_size=16)

    def correr(self):
        print(f'{self.__nome} está correndo!')

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False
    


# nome = input("Digite seu nome: ")
# email = input("Digite seu email: ")
# senha = input("Digite seu senha: ")
# confirm_senha = input("Confirme a senha: ")


# if senha == confirm_senha:
#     usuario1 = Usuario(nome, email, senha)
#     print(f"usuario criado com sucesso. Senha cryptografada: {usuario1._Usuario__senha}")
# else:
#     print("As senhas não conferem!")



# senha1 = input("Senha de acesso: ")

# if usuario1.checa_senha(senha1):
#     print("Acesso permitido!")
# else:
#     print("Acesso negado!")







# Métodos de classe


class Usuarios:

    contador = 0

    @classmethod # Se usa para dizer que é um metodo de classe
    def total_usuarios(cls):
        print(f"Temos {cls.contador} usuarios no sistema")

        # Métodos de classe nao conseguem acessar atributos de instancia


    def __init__(self, nome, email, senha):
        self.__id = Usuarios.contador + 1
        self.__nome = nome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds= 200000, salt_size=16)
        Usuarios.contador = self.__id


"""
Alem dos metodos de classe e de instancias nos temos os metodos estaticos

"""

# Metodo estatico



class Carro:

    @staticmethod # decorator para classificar como metodo estatico. Em metodos estaticos nao temos acesso a instancia do objeto e nem a classe
    def definicao():
        return 'GGWP'
    
    @classmethod # decorator para classificar como metodo de classe
    def total_usuarios(cls):
        return f'total de carro(s){cls.contador}'

    contador = 0

    def __init__(self, marca, modelo, ano):
        self.__id= Carro.contador +1
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        Carro.contador = self.__id


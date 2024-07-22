"""
POO - Classes

Em POO, Classes nada mais sao do que modelos dos objetos do mundo real sendo representados computacionalmente.

Imagine que voce queira faazer um sistema para automatizar o controle das lampadas da sua casa


Classes podem conter:
    atributos -> Representam as caracteristicas do objeto. Ou seja, pleos atributos conseguimos representar computacionalmente os estados de um objeto. No caso da lampada
    , possivelmente iriamos queer saber se a lampada é 110v ou 220v, se ela é branca, amarela, vemelha... , qual a luminisodade e etc.

    métodos (funções) -> Representam os comportamentos do objeto. Ou seja, as ações que este objeto pode realizar no seu sistema. No caso da lampada, por exemplo, um comportamento
    comum que muito provavelmente iriamos querer representar no nosso sistema é o de ligar e desligar a mesma


Quando estamos planejando um software e definimos quais classes teremos que ter no sistema, chamamos estes objetos deque serao mapeados de entidade

Em Python, por convenção, ficou estabelecido que, todo atributo de uma classe é público.
Ou seja, pode ser acessado em todo o projeto.
Caso queiramos demonstrar que determinado atributo deve ser tratado como privado, ou seja,  que deve ser acessado/utilizado somente dentro da propria classe onde esta 
declarado, utiliza-se __ duplo underscore no inicio de seu nome.

Isso é conhecido como Name Mangling.

"""


class Teste:
    def __init__(self, nome, idade, salario):
        self.__salario = salario # Atributo privado
        self.nome = nome # Atributo publico
        self.idade = idade

    def ver_salario(self):
        print(self.__salario) # Dentro da classe podemos imprimir normalmente o atributo privado


user = Teste(nome='Matheus', idade=26, salario=1400)


# print(dir(user))
print(user._Teste__salario) # Forma de conseguir enxergar um atributo privado

print(user.ver_salario())



# OBS: É apenas uma convenção, ou seja, a linguagem Python nao vai impedir que façamos acesso aos atributos sinalizados como privados fora da classe



"""
Atributos de classe

Atributos de classe, são atributos, declarados diretamente na classe, ou seja, 
fora do construtor. Geralmente já inicializamos um valor, e este valor é compartilhada entre todas
as instâncias da classe. Ou seja, ao invés de cada instância da classe ter seus próprios valores
como é o caso dos atributos de instacia, com os atributos de classe todas as instâncias terão
o mesmo valor para este atributo.

"""


class Produto:
    #atributo de classe
    imposto = 1.05 # OBS: Em linguagens como o Java, estes atributos são chamados de atributos estaticos
    contador= 0

    def __init__(self, nome, valor, descricao):
        self.id = Produto.contador + 1
        self.nome = nome
        self.valor = (valor * Produto.imposto)
        self.descricao = descricao
        Produto.contador = self.id



produto1 = Produto(nome='Playstation', valor=1200, descricao='Playstation 5')

print(produto1.nome)
print(produto1.valor)


"""
Criando um atributo dinamico em tempo de execução
"""


produto1.peso = '2kg' # Note que na classe produto nao existem o atributo peso




print(f"nome do produto: {produto1.nome}, peso: {produto1.peso}")
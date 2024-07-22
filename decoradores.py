"""
Decoradores - Decorators

O que são decorators ?

 - Decorators São funções,
 - Decorators envolvem outras funções e aprimoram seus comportamentos,
 - Decorators também são exemplos de Higher Order Functions,
 - Decorators tem uma sintaxe própria, usando "@" (syntact Sugar / Açucar sintático)


"""


# Decorators como funções (Sintaxe não recomendada / sem açúcar sintático)

def seja_educado(funcao):
    def sendo_educado():
        print("Foi um prazer conhecer você")
        funcao()
        print("Tenha um bom dia e até a próxima")
    return sendo_educado

def saudacao():
    print("Seja bem vindo ao curso de Python!")


teste = seja_educado(saudacao) # decorando manualmente

teste()


print('---------------------------------------')

# Decorators com Syntax sugar

def seja_educado_mesmo(funcao):
    def sendo_educado_mesmo():
        print("Foi um prazer conhecer você")
        funcao()
        print("Tenha um bom dia e até a próxima")
    return sendo_educado_mesmo


@seja_educado_mesmo
def meu_nome():
    print("Meu nome é Rafael")

meu_nome()

print('---------------------------------------')





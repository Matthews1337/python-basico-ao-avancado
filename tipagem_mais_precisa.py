"""
Literal type
Union
Final
Typed dictionaries
Protocols
"""

# Literal type

from typing import Literal, Union

def pegar_status(usuario: str) -> Literal['conectado' ,'desconectado']:
    pass

def calculav1(operacao: str, num1: int, num2: int)-> None:

    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '*':
        return num1 * num2
    else:
        raise ValueError(f" Operação inválida: {operacao!r}")
    


calculav1('+', 4, 5)
calculav1('-', 4, 5)
calculav1('*', 4, 5)
# calculav1('/', 4, 5)# ValueError


def calculav2(operacao: Literal['+', '-', '*'], num1: int, num2: int)-> None:

    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '*':
        return num1 * num2
    else:
        raise ValueError(f" Operação inválida: {operacao!r}")
    


def soma(num1: int, num2: int)-> Union[str, int]:
    resultado: int = num1 + num2

    if resultado > 50:
        return f"{resultado} é muito grande"
    else:
        return resultado
    

# TypedDict -> Dicionarios tipados

from typing import TypedDict

class CursoPython(TypedDict):
    nome: str
    ano: int


geek = CursoPython(nome='Geek-University', ano='2024')

print(geek)
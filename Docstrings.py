"""
Documentando funções com Docstrings

OBS: Podemos ter acesso a documentação de uma função em Python utilizando a propriedade especial __doc__

Podemos ainda fazer acesso a documentação com a função help()

"""


# Exemplos

def diz_oi():
    """Uma função simples que retorna a string 'oi!' """
    return 'oi!'


def exponencial(numero, potencia=2):
    """
    função que retorna por padrao o quadrado de 'numero' á 'potencia' informada
    :param numero: (numero que desejamos gerar o exponencial)
    :param potencia: (potencia que queremos gerar o exponencial. por padrao é 2)
    :return: retorna o exponencial de 'numero' por 'potencia'
    """
    return numero ** potencia
"""
JSON e Pickle

JSON -> Java Script Object Notation

API -> São meios de comunicação entre os serviços oferecidos por empresas (Twitter, Facebook, Youtubr...)

import json

ret = json.dumps(['produto'], {'Playstation': ('2TB, 'Novo', '220V', 2340)})

print(type(ret))
print(ret)

"""
import json
import jsonpickle

ret = json.dumps(['produto', {'Playstation': ('2TB', 'Novo', '220V', 2340)}])

# print(type(ret))
# print(ret)

class Gato:

    def __init__(self, nome, raca) -> None:
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome
    
    @property
    def raca(self):
        return self.__raca
    

garfield = Gato(nome='Garfield', raca="vira-lata")


print(garfield.__dict__)
ret = json.dumps(garfield.__dict__)

print(ret)

# with open('garfield.json', 'w') as arquivo:
#     # conteudo = arquivo.read()
#     ret = jsonpickle.encode(garfield)
#     arquivo.write(ret)


with open('garfield.json', 'r') as arquivo:
    conteudo = arquivo.read()
    garfield = jsonpickle.decode(conteudo)
    print(garfield.nome)
    print(garfield.raca)



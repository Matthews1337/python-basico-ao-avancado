"""
POO - Métodos mágicos

Métodos mágicos sao todos os metodos que utilizam dunder

Ex: __init__()

__repr__ -> REpresentação do objeto

"""

class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __repr__(self): # Modificando um metodo da classe objeto padrao do Python, através de polimorfismo
        return f'{self.titulo} escrito por  {self.autor}'

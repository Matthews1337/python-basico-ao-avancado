"""
Unittest - Antes e apos hooks

hooks -> são os testes em si, ou seja, a execução dos testes

setup() -> é executado antes de cada método de teste. É útil para criarmos instâncias de objetos e outros dados;

tearDown() -> é executado ao final de cada método de teste. É útil para excluir dados ou fechar conexões com banco de dados

"""

import unittest

class ModuloTest(unittest.TestCase):
    def setUp(self):
        print("Setup executado antes de cada método de teste")

    def test_primeiro(self):
        pass

    def test_segundo(self):
        pass

    def tearDown(self) -> None:
        pass
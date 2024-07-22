from robo import Robo

import unittest

class RoboTestes(unittest.TestCase):
    
    def setUp(self): # para reutilizar as variaveis
        self.megaman = Robo("Mega man", bateria=50)
        print('SetUp sendo executado')

    def test_carregar(self):
        """Teste carregar bateria"""
        # megaman = Robo("Mega man", bateria=50) # Com o metodo setUp eu posso apagar estas variaveis
        self.megaman.carregar()
        self.assertEqual(self.megaman.bateria, 100)

    def test_dizer_nome(self):
        # megaman = Robo("Mega man", bateria=50)
        self.assertEqual(self.megaman.dizer_nome(), "Olá meu nome é Mega man")
        self.assertEqual(self.megaman.bateria, 49, )

    def tearDown(self):
        print('tearDown sendo executado')

if __name__ == "__main__":
    unittest.main()
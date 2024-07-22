import unittest


from atividades_unittest import comer,dormir

# python testes_unittest.py -v -> para ler as docstrings

class AtividadesTestes(unittest.TestCase):
    
    def test_comer(self):
        """ Testando a comida saudavel"""
        self.assertEqual(comer('quiabo', True), 'Estou comendo quiabo porque quero manter a forma')
        # self.assertEqual(comer(comida='Pizza', eh_saudavel=False), "Estou comendo pizza porque só se vive uma vez")

    def test_comer_gostosa(self):
        """ Testando a comida gostosa"""
        self.assertEqual(comer(comida='pizza', eh_saudavel=False), "Estou comendo pizza porque a gente vive uma vez")


    def test_dormir(self):
        """ Testando dormir pouco"""
        self.assertEqual(dormir(6), "Continuo cansado após dormir por 6 horas")


    def test_dormir_muito(self):
        """ Testando dormir muito"""
        self.assertEqual(dormir(9), "Ptz dormi 9 horas, estou atrasado")
    



if __name__ == "__main__":
    unittest.main()

    
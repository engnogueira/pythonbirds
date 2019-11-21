from unittest import TestCase
from OO.automovel.instrucoes_carro import Motor


class CarroTesteCase(TestCase):
    def teste_velocidade_inicial(self):
        motor=Motor()
        self.assertEqual(0, motor.velocidade)

    def teste_acelerar(self):
        motor=Motor()
        motor.acelerar()
        self.assertEqual(1, motor.velocidade)


if __name__ == '__main__':
    unittest.main()

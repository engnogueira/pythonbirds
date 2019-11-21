"""
Atividade de estudo de Classses
Criar um automovel que se move e tem direção, para tanto criar classes de motor e direção.
O automovel inicialmente se encontrará na situação de desligado e direção inicial : N-S , com sentido Norte
Cada vez que é solicitado mudança de direção o mesmo girará + 90º (direita) e - 90º (esquerda)
O automovel não têm marcha à re.
A velocidade máxima permitida pelo automovel é de 100 Km/h em direção frontal e de 20 km/h quando mudar a direção
O automovel se movimentará em MUV com aceleração escalar de 8m/s², aceleração referente a fazer de 0 a 10mm em 5s.
"""
from OO.automovel.motor import Motor
from OO.automovel.direcao import Direcao


class Carro:
    """
    Classe construtora do objeto automovel
    """
    def __init__(self, motor=Motor(), direcao=Direcao(), acelerar=0, ligar=False):
        """
        Função inicializadora do objeto automovel e instanciadora dos objetos motor e direção
        :param motor:
        :param direcao:
        :param acelerar:
        :param ligar:
        """
        self.motor = motor
        self.direcao = direcao
        self.acelerar = acelerar
        self.ligar = ligar
        # motor = Motor()
        # direcao = Direcao()
        # print(motor.__dict__)

    def ligar_carro(self):
        """
        Função responsável por ligar o automovel
        :return:
        """
        print('O automovel está ligado')
        self.ligar = True
        return self.motor.ligar_motor()

    def desligar_carro(self):
        """
        Função responsável por desligar o automovel
        :return:
        """
        print('O automovel está desligado')
        self.ligar = False
        return self.motor.desligar_motor()


if __name__ == '__main__':
    carro = Carro(Motor(), Direcao(), acelerar=0, ligar=False)
    print(carro.__dict__)
    carro.ligar_carro()
    carro.desligar_carro()

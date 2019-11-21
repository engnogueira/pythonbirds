"""
Atividade de estudo de Classses
Criar um automovel que se move e tem direção, para tanto criar classes de motor e direção.
O automovel inicialmente se encontrará na situação de desligado e direção inicial : N-S , com sentido Norte
Cada vez que é solicitado mudança de direção o mesmo girará + 90º (direita) e - 90º (esquerda)
O automovel não têm marcha à re.
A velocidade máxima permitida pelo automovel é de 100 Km/h em direção frontal e de 20 km/h quando mudar a direção
O automovel se movimentará em MUV com aceleração escalar de 8m/s², aceleração referente a fazer de 0 a 10mm em 5s.
"""


class Direcao:
    """
    Classe construtora do objeto direção
    :param norte = 'N'
    :param sul = 'S'
    :param leste = 'L'
    :param oeste = 'O'
    """

    def __init__(self, direita=False, esquerda=False, em_frente=True):
        """
        Classe inicializadora o objeto direção
        :param direita:
        :param esquerda:
        :param em_frente:
        """
        self.em_frente = em_frente
        self.direita = direita
        self.esquerda = esquerda
        print('O automovel começa em sua posição inicial, na direção Norte-Sul, sentido Norte')

    @staticmethod
    def virar_a_direita():
        """
        função responsável por virar a direção à direita em 90º
        :return:
        """
        print('Viramos o automovel 90º a direita')
        pass

    @staticmethod
    def virar_a_esquerda():
        """
        função responsável por virar a direção à esquerda em 90º
        :return:
        """
        print('Viramos o automovel 90º a esquerda')
        pass
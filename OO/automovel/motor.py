"""
Atividade de estudo de Classses
Criar um automovel que se move e tem direção, para tanto criar classes de motor e direção.
O automovel inicialmente se encontrará na situação de desligado e direção inicial : N-S , com sentido Norte
Cada vez que é solicitado mudança de direção o mesmo girará + 90º (direita) e - 90º (esquerda)
O automovel não têm marcha à re.
A velocidade máxima permitida pelo automovel é de 100 Km/h em direção frontal e de 20 km/h quando mudar a direção
O automovel se movimentará em MUV com aceleração escalar de 8m/s², aceleração referente a fazer de 0 a 10mm em 5s.
"""


class Motor:
    """
    Classe construtora do objeto motor
    """
    def __init__(self, ligado=False, velocidade=0):
        """
        Função inicializadora do objeto motor
        :param ligado:
        :param velocidade:
        """
        self.ligado = ligado
        self.velocidade = velocidade

    def ligar_motor(self):
        """
        Função responsável por ligar o motor do automovel quando o automovel está ligado
        :return:
        """
        print('O motor do automovel foi acionado')
        self.ligado = True
        return self.ligado

    def desligar_motor(self):
        """
        Função responsável por desligar o motor do automovel quando o automovel está desligado
        :return:
        """
        print('O motor do automovel foi desligado')
        self.ligado = False
        return self.ligado

    def acelerar(self, acelerar):
        """
        Função responsável por acelerar o motor e consequentemente aumentar a sua velocidade
        :param acelerar:
        :return:
        """

    def frear(self, frear):
        """
        Função responsável por desacelerar o automovel, consequentemente reduzindo a sua velocidade
        :param frear:
        :return:
        """
        pass
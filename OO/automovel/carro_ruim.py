"""
Atividade de estudo de Classses
Criar um automovel que se move e tem direção, para tanto criar classes de motor e direção.
O automovel inicialmente se encontrará na situação de desligado e direção inicial : N-S , com sentido Norte
Cada vez que é solicitado mudança de direção o mesmo girará + 90º (direita) e - 90º (esquerda)
O automovel não têm marcha à re.
A velocidade máxima permitida pelo automovel é de 100 Km/h em direção frontal e de 20 km/h quando mudar a direção
O automovel se movimentará em MUV com aceleração escalar de 8m/s², aceleração referente a fazer de 0 a 10mm em 5s.
"""


class Carro:
    """
    Classe construtora do objeto automovel
    """
    global aceleracao
    global desaceleracao
    aceleracao = 8
    desaceleracao = 0
    tempo = 0
    velocidade = 0
    acelerando = False

    def __init__(self, motor, ligar=False):
        # noinspection SpellCheckingInspection
        """
        Função inicializadora do objeto automovel e instanciadora dos objetos motor e direção
        :param ligar:
        """
        self.motor = motor
        self.ligar = ligar

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

    def acelerar(self):
        """
        Função responsável por acelerar o motor e consequentemente aumentar a sua velocidade
        :return:
        """
        Carro.acelerando = True
        if not Carro.acelerando:
            Carro.tempo += 1
            Carro.velocidade = (aceleracao * Carro.tempo) * 3600 / 1000  # Velocidade em Km/h
            Motor.motor_acelerando()
        Carro.acelerando = False
        desaceleracao = -2 * aceleracao
        Motor.motor_desacelerando(desaceleracao)

    def freiar(self):
        """
        Função responsável por freiar e consequentemente desacelerar o motor diminuindo a sua velocidade
        :return:
        """
        Carro.acelerando = False
        if Carro.acelerando:
            Carro.tempo += 1
            Carro.velocidade = (aceleracao * Carro.tempo) * 3600 / 1000  # Velocidade em Km/h
            Motor.motor_acelerando()
        Carro.acelerando = False
        desaceleracao = -2 * aceleracao
        Motor.motor_desacelerando(desaceleracao)


class Motor(Carro):
    """
    Classe construtora do objeto motor
    """
    def __init__(self, ligado=False):
        """
        Função inicializadora do objeto motor
        :param ligado:
        """
        self.ligado = ligado
        super().__init__(self)

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

    def motor_acelerando():
        """
        Função responsável por desaacelerar o motor e consequentemente aumentar a sua velocidade
        :return:
        """
        if not carro.motor.ligado:
            print('O automovel está desligado portanto não pode acelerar')
        if Carro.velocidade > 100:
            print('Velocidade acima de 100 km/h, necessário frear urgentemente')
            Carro.desaceleracao = -2*Carro.aceleracao
            self.motor_desacelerando(Carro.desaceleracao)
        print(f'Velocidade atual é de {Carro.velocidade} km/h')

    def motor_desacelerando(desaceleracao):
        """
        Função responsável por desacelerar o automovel, consequentemente reduzindo a sua velocidade
        :param desaceleracao:
        :return:
        """
        if not carro.motor.ligado:
            print('O automovel está desligado portanto não pode desacelerar')
        if Carro.velocidade > 100:
            print('Velocidade acima de 100 km/h, continuar freiando até velocidade de 100 Km/h')
            Carro.desaceleracao = -2 * Carro.aceleracao
            Motor.motor_desacelerando(desaceleracao)
        print(f'Velocidade atual é de {Carro.velocidade} km/h')


class Direcao(Carro):
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
        super().__init__(self)
        self.em_frente = em_frente
        self.direita = direita
        self.esquerda = esquerda

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


if __name__ == '__main__':
    carro = Carro(Motor(), ligar=True)
    print(carro.__dict__)
    carro.ligar_carro()
    carro.motor.acelerar()
    carro.motor.acelerar()
    carro.motor.acelerar()
    carro.motor.acelerar()

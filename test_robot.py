from abstract_robot import AbstractRobot

class TestRobot(AbstractRobot):

    def posicao_00(self):
        print('Robô jogou na posição 00')

    def posicao_01(self):
        print('Robô jogou na posição 01')

    def posicao_02(self):
        print('Robô jogou na posição 02')

    def posicao_10(self):
        print('Robô jogou na posição 10')

    def posicao_11(self):
        print('Robô jogou na posição 11')

    def posicao_12(self):
        print('Robô jogou na posição 12')

    def posicao_20(self):
        print('Robô jogou na posição 20')

    def posicao_21(self):
        print('Robô jogou na posição 21')

    def posicao_22(self):
        print('Robô jogou na posição 22')

    def pegar_ficha(self):
        print('Robô pegou ficha!')

    def soltar_ficha(self):
        print('Robô soltou ficha.')

    def voltar_base(self):
        print('Robô voltou posição base!')

    def intermediaria_rampa(self):
        print('Robô em posição intermediária na rampa!')

    def pos_pegar(self):
        print('Robo na posição de coletar ficha.')

    def intermediaria_tabuleiro(self):
        print('Robô em posição intermediária tabuleiro!')

    def pos_pegar(self):
        print('Robô na posição de pegar ficha')

    def jogada_robo(self, jogada_robo_linha, jogada_robo_coluna):
        self.conectar()
        self.intermediaria_tabuleiro()
        self.intermediaria_rampa()
        self.pos_pegar()
        self.pegar_ficha()
        self.intermediaria_rampa()
        self.intermediaria_tabuleiro()
        if jogada_robo_linha == 0:
            if jogada_robo_coluna == 0:
                self.posicao_00()
            elif jogada_robo_coluna == 1:
                self.posicao_01()
            elif jogada_robo_coluna == 2:
                self.posicao_02()
            else:
                print('Você não deveria ver este erro no terminal...')
        elif jogada_robo_linha == 1:
            if jogada_robo_coluna == 0:
                self.posicao_10()
            elif jogada_robo_coluna == 1:
                self.posicao_11()
            elif jogada_robo_coluna == 2:
                self.posicao_12()
            else:
                print('Você não deveria ver este erro no terminal...')
        elif jogada_robo_linha == 2:
            if jogada_robo_coluna == 0:
                self.posicao_20()
            elif jogada_robo_coluna == 1:
                self.posicao_21()
            elif jogada_robo_coluna == 2:
                self.posicao_22()
            else:
                print('Você não deveria ver este erro no terminal...')
        else:
            print('Você não deveria ver este erro no terminal...')
        self.soltar_ficha()
        self.intermediaria_tabuleiro()
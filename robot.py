from pyniryo2 import *
from abstract_robot import AbstractRobot

class Robot(AbstractRobot):
    def __init__(self):
        self.robot = None #atributo que é o objeto NiryoRobot
        self.calibrated = False
        self.p00 = PoseObject(
            x = 0.2715,
            y = -0.0734,
            z = 0.0944,
            roll = -1.638,
            pitch = 1.542,
            yaw = -1.484)
        
        self.p01 = PoseObject(
            x = 0.2780,
            y = -0.0142,
            z = 0.0942,
            roll = -2.001,
            pitch = 1.543,
            yaw = -1.843)
        
        self.p02 = PoseObject(
            x = 0.2734,
            y = 0.0544,
            z = 0.0914,
            roll = -1.020,
            pitch = 1.541,
            yaw = -0.840)
        
        self.p10 = PoseObject(
            x = 0.339,
            y = -0.070,
            z = 0.087,
            roll = -1.480,
            pitch = 1.461,
            yaw = -1.391)
        
        self.p11 = PoseObject(
            x = 0.3372,
            y = -0.0131,
            z = 0.0979,
            roll = -0.999,
            pitch = 1.521,
            yaw = -0.829)
        
        self.p12 = PoseObject(
            x = 0.3357,
            y = 0.0550,
            z = 0.0886,
            roll = -1.532,
            pitch = 1.498,
            yaw = -1.343)
        
        self.p20 = PoseObject(
            x = 0.3956,
            y = -0.0709,
            z = 0.0894,
            roll = -1.768,
            pitch = 1.449,
            yaw = -1.628)
        
        self.p21 = PoseObject(
            x = 0.3958,
            y = -0.0136,
            z = 0.0903,
            roll = -1.645,
            pitch = 1.486,
            yaw = -1.504)
        
        self.p22 = PoseObject(
            x = 0.3934,
            y = 0.0515,
            z = 0.0881,
            roll = -1.123,
            pitch = 1.480,
            yaw = -0.964)
        
        self.base = PoseObject(
            x = 0,
            y = 0,
            z = 0,
            roll = 0,
            pitch = 0,
            yaw = 0)
        
        self.int_rampa = PoseObject(
            x = -0.0022,
            y = -0.2298,
            z = 0.1838,
            roll = -0.196,
            pitch = 1.069,
            yaw = -1.594)
        
        self.pospegar = PoseObject(
            x = -0.0035,
            y = -0.2552,
            z = 0.1177,
            roll = -0.195,
            pitch = 1.251,
            yaw = -1.597)
        
        self. int_tab = PoseObject(
            x = 0.3315,
            y = -0.0123,
            z = 0.1557,
            roll = -0.912,
            pitch = 1.506,
            yaw = -0.781)

    def conectar(self): #pra os testes funcionarem, tivemos que conectar
        # e em seguida calibrar o robô!
          
        self.robot = NiryoRobot("169.254.200.200")
        if self.calibrated == False:
            teste_calibracao_robo = self.robot.arm.need_calibration()
            #buscar se precisa de calibração. true se precisa, false se já estiver
            # calibrado.
            if teste_calibracao_robo: #se verdadeiro, iniciar calibração automática
                self.robot.arm.calibrate_auto()
                if self.robot.arm.learning_mode.value:
                    self.robot.arm.set_learning_mode(False)
                    #self.robot.arm.move_to_home_pose() #Outra maneira de sair do learning mode
            else:
                print('Robô calibrado!')

    def desconectar(self):
        self.robot.end()

    def posicao_00(self):    
        self.robot.arm.move_pose(self.p00)

    def posicao_01(self):
        self.robot.arm.move_pose(self.p01)

    def posicao_02(self):
        self.robot.arm.move_pose(self.p02)

    def posicao_10(self): #corrigir os dados! Repetido de 02
        self.robot.arm.move_pose(self.p10)

    def posicao_11(self):
        self.robot.arm.move_pose(self.p11)

    def posicao_12(self):
        self.robot.arm.move_pose(self.p12)

    def posicao_20(self):      
        self.robot.arm.move_pose(self.p20)

    def posicao_21(self):   
        self.robot.arm.move_pose(self.p21)

    def posicao_22(self):
        self.robot.arm.move_pose(self.p22)

    def pegar_ficha(self):
        self.robot.tool.close_gripper(
            speed=500,
            max_torque_percentage=100,
            hold_torque_percentage=30,
            callback=None)
    
    def soltar_ficha(self):
        self.robot.tool.open_gripper(
            speed=500,
            max_torque_percentage=100,
            hold_torque_percentage=30,
            callback=None)
    
    def voltar_base(self):
        self.robot.arm.move_pose(self.base)

    def intermediaria_rampa(self):
        self.robot.arm.move_pose(self.int_rampa)
    
    def pos_pegar(self):
        self.robot.arm.move_pose(self.pospegar)

    def intermediaria_tabuleiro(self):
        self.robot.arm.move_pose(self.int_tab)


    def jogada_robo(self,jogada_robo_linha,jogada_robo_coluna):
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


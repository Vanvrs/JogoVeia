from pyniryo2 import *
from robot import Robot

#teste = NiryoRobot("169.254.200.200")


teste = Robot()

teste.conectar()
teste.robot.arm.calibrate_auto()
teste.robot.arm.move_to_home_pose()
#teste.desconectar()
teste.intermediaria_tabuleiro()
teste.intermediaria_rampa()
teste.pos_pegar()
teste.pegar_ficha()
teste.intermediaria_rampa()
teste.soltar_ficha()
teste.intermediaria_rampa()
teste.intermediaria_tabuleiro()
teste.posicao_00()
teste.posicao_01()
teste.posicao_02()
teste.posicao_10()
teste.posicao_11()
teste.posicao_12()
teste.posicao_20()
teste.posicao_21()
teste.posicao_22()
teste.intermediaria_tabuleiro()
teste.voltar_base()
teste.desconectar()
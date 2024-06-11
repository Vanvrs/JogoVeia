import tkinter as tk
from tkinter import messagebox
import random

from robot import Robot
#from test_robot import TestRobot

robot = Robot() #criando a instância do robô real
#robot = TestRobot()

class JogoDaVea:
    def __init__(self):
        #configura interface gráfica
        self.janela = tk.Tk()
        self.janela.title("Jogo da Véa")
        self.janela.configure(bg="#d9f1ff")

        titulo = tk.Label(self.janela, text="Jogo da Véa!", font=("Comic Sans MS", 20, "bold"))
        titulo.pack(pady=10)

        self.turno = "X"

        largura_janela = 500
        altura_janela = 600 #alterado de 500 para 600, para mostrar o botão de Reiniciar jogo.
        largura_tela = self.janela.winfo_screenwidth()
        altura_tela = self.janela.winfo_screenheight()
        x_pos = (largura_tela - largura_janela) // 2
        y_pos = (altura_tela - altura_janela) // 2
        self.janela.geometry(f"{largura_janela}x{altura_janela}+{x_pos}+{y_pos}")

#Travar o redimensionamento da janela gerada pelo Tkinter
#https://stackoverflow.com/questions/21958534/how-can-i-prevent-a-window-from-being-resized-with-tkinter
        self.janela.resizable(width=False, height=False)

        frame_central = tk.Frame(self.janela)
        frame_central.pack(expand=True)


        #configura tabuleiro
        self.tabuleiro = [[" " for _ in range(3)] for _ in range(3)]


        #Define botões para ler os eventos de clique na interface gráfica e faz a varredura para
        #buscar qual dos botões foi acionado

        self.botoes = []
        for i in range(3):
            linha = []
            for j in range(3):
                botao = tk.Button(frame_central, text=" ", font=("Comic Sans MS", 20, "bold"), width=6, height=3,
                                  command=lambda x=i, y=j: self.jogada(x, y)) #executa self.jogada() quando pressiona botao
                botao.grid(row=i, column=j, padx=5, pady=5)
                linha.append(botao)
            self.botoes.append(linha)

        #Define botão de reiniciar partida

        reiniciar_btn = tk.Button(self.janela, text="Reiniciar", font=("Comic Sans MS", 14, "bold"),
                                  command=self.resetar)
        reiniciar_btn.pack(side="top", fill="x", padx=10, pady=(10, 0))

    def jogada(self, x, y):
        if self.tabuleiro[x][y] == " ": #se não houver jogada registrada, registra o 'X' ou 'O'.
            self.tabuleiro[x][y] = self.turno
            self.botoes[x][y].configure(text=self.turno)    # aqui define o texto do botão
            self.botoes[x][y].config(state="disabled")  # aqui trava o botão para evitar jogada ilegal
            if self.ifvitoria():
                messagebox.showinfo("Cabôsse, o que era doce!", f"O jogador {self.turno} venceu do donzelo!")
                #self.ifjogo()
                jogada_robo = False # Se o jogador humano vencer ou jogar o empate, não precisa acionar o robô!
            elif self.ifempate():
                messagebox.showinfo("Acabou, tabacudo.", "Deu véa, vai ter que rolar a nega!")
                #self.ifjogo()
                jogada_robo = False  # Se o jogador humano vencer ou jogar o empate, não precisa acionar o robô!
            else: #se não teve vitória, nem empate, então mudar jogador
                self.turno = "O" if self.turno == "X" else "X" #alterna o jogador aqui
                jogada_robo = True # O jogador humano nem vence nem joga o empate, precisa acionar o robô!

#Pra facilitar a lógica, uma jogada é composta de um clique humano e uma jogada do robô
#determinar a comunicação com o robô na inicialização
#determinar métodos para posicionar o robô na posição de coletar peça,
#e mover para cada uma das 9 posições do tabuleiro
 
            jogada_robo_linha = random.randrange(0,3)
            jogada_robo_coluna = random.randrange(0,3)
            
            while jogada_robo:
                if self.tabuleiro[jogada_robo_linha][jogada_robo_coluna] == ' ':
                    self.tabuleiro[jogada_robo_linha][jogada_robo_coluna] = self.turno
                    self.botoes[jogada_robo_linha][jogada_robo_coluna].configure(text=self.turno)
                    # aqui define o texto do botão
                    self.botoes[jogada_robo_linha][jogada_robo_coluna].config(state="disabled")
                    # aqui trava o botão para evitar jogada ilegal

                    #A jogada foi validada e registrada no GUI
                    #Agora comandar o robô para realizar a jogada
                    #Com a lista de ações do robô, será melhor criar um método chamando essas etapas
                    robot.jogada_robo(jogada_robo_linha,jogada_robo_coluna)

                    if self.ifvitoria():
                        messagebox.showinfo("Cabôsse, o que era doce!", f"O jogador {self.turno} venceu do donzelo!")
                        #self.ifjogo()
                        jogada_robo = False
                        
                    elif self.ifempate():
                        messagebox.showinfo("Acabou, tabacudo.", "Deu véa, vai ter que rolar a nega!")
                        #self.ifjogo()
                        jogada_robo = False
                    else: #se não teve vitória, nem empate, então mudar jogador
                        self.turno = "O" if self.turno == "X" else "X" #alterna o jogador aqui
                        jogada_robo = False
                else: #jogada do robô foi inválida, repetir a jogada!
                    jogada_robo_linha = random.randrange(0,3)
                    jogada_robo_coluna = random.randrange(0,3)
                    jogada_robo = True



    def ifvitoria(self):
        for i in range(3):
            if self.tabuleiro[i][0] == self.tabuleiro[i][1] == self.tabuleiro[i][2] != " ":
                return True #confere linhas
            if self.tabuleiro[0][i] == self.tabuleiro[1][i] == self.tabuleiro[2][i] != " ":
                return True #confere colunas
        if self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] != " ":
            return True #confere diagonal descendente
        if self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0] != " ":
            return True #confere diagonal ascendente
        return False

    def ifempate(self):
        for i in range(3):
            for j in range(3):
                if self.tabuleiro[i][j] == " ": #se todas posições estiverem preenchidas, é empate
                    return False
        return True

    def resetar(self):
        self.turno = "X"
        self.tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.botoes[i][j].configure(text=" ", state="normal")

app = JogoDaVea()
app.janela.mainloop()


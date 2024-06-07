import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import sqlite3

class JogoDaVéa:
    def __init__(self):
        self.janela = tk.Tk() 
        self.janela.title("Jogo da Véa")
        self.janela.configure(bg="#d9f1ff")

        titulo = tk.Label(self.janela, text="Jogo da Véa!", font=("Comic Sans MS", 20, "bold"))
        titulo.pack(pady=10)

        self.turno = "X"

        largura_janela = 500
        altura_janela = 500
        largura_tela = self.janela.winfo_screenwidth()
        altura_tela = self.janela.winfo_screenheight()
        x_pos = (largura_tela - largura_janela) // 2
        y_pos = (altura_tela - altura_janela) // 2
        self.janela.geometry(f"{largura_janela}x{altura_janela}+{x_pos}+{y_pos}")

        frame_central = tk.Frame(self.janela)
        frame_central.pack(expand=True)

        self.tabuleiro = [[" " for _ in range(3)] for _ in range(3)]

        self.botoes = []
        for i in range(3):
            linha = []
            for j in range(3):
                botao = tk.Button(frame_central, text=" ", font=("Comic Sans MS", 20, "bold"), width=6, height=3,
                                  command=lambda x=i, y=j: self.jogada(x, y))
                botao.grid(row=i, column=j, padx=5, pady=5)
                linha.append(botao)
            self.botoes.append(linha)

        reiniciar_btn = tk.Button(self.janela, text="Reiniciar", font=("Comic Sans MS", 14, "bold"),
                                  command=self.resetar)
        reiniciar_btn.pack(side="top", fill="x", padx=10, pady=(10, 0))

        self.conexao = sqlite3.connect("jogo_véa!.db")
        self.criar_tabela()

        self.carregar_jogo()

    def criar_tabela(self):
        cursor = self.conexao.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS jogo (id INTEGER PRIMARY KEY, turno TEXT, tabuleiro TEXT)")

    def carregar_jogo(self):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM jogo ORDER BY id DESC LIMIT 1")
        resultado = cursor.fetchone()
        if resultado:
            self.turno = resultado[1]
            self.tabuleiro = eval(resultado[2])
            self.atualizar_tabuleiro()

    def salvar_jogo(self):
        cursor = self.conexao.cursor()
        cursor.execute("INSERT INTO jogo (turno, tabuleiro) VALUES (?, ?)", (self.turno, str(self.tabuleiro)))
        self.conexao.commit()

    def jogada(self, x, y):
        if self.tabuleiro[x][y] == " ":
            self.tabuleiro[x][y] = self.turno
            self.botoes[x][y].configure(text=self.turno)
            self.botoes[x][y].config(state="disabled")
            if self.ifvitoria():
                messagebox.showinfo("Cabôsse, o que era doce!", f"O jogador {self.turno} venceu do donzelo!")
                self.ifjogo()
            elif self.ifempate():
                messagebox.showinfo("Acabou, tabacudo.", "Deu véa, vai ter que rolar a nega!")
                self.ifjogo()
            else:
                self.turno = "O" if self.turno == "X" else "X"
                self.salvar_jogo()

    def ifvitoria(self):
        for i in range(3):
            if self.tabuleiro[i][0] == self.tabuleiro[i][1] == self.tabuleiro[i][2] != " ":
                return True
            if self.tabuleiro[0][i] == self.tabuleiro[1][i] == self.tabuleiro[2][i] != " ":
                return True
        if self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] != " ":
            return True
        if self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0] != " ":
            return True
        return False

    def ifempate(self):
        for i in range(3):
            for j in range(3):
                if self.tabuleiro[i][j] == " ":
                    return False
        return True

    def resetar(self):
        self.turno = "X"
        self.tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.botoes[i][j].configure(text=" ", state="normal")

app = JogoDaVéa()
app.janela.mainloop()


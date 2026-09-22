import tkinter as tk
import random


class JogoAdivinhacao:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Jogo de Adivinhação")
        self.janela.geometry("800x800")
        self.janela.resizable(False, False)

        self.numero_secreto = None
        self.limite = None
        self.tentativas = None
        self.numeros_usados = []

        self.mostrar_tela_dificuldade()

    def limpar_tela(self):
        for widget in self.janela.winfo_children():
            widget.destroy()

    def mostrar_tela_dificuldade(self):
        self.limpar_tela()

        titulo = tk.Label(
            self.janela,
            text="JOGO DE ADIVINHAÇÃO",
            font=("Arial", 22, "bold")
        )
        titulo.pack(pady=40)

        instrucoes = tk.Label(
            self.janela,
            text="Escolha uma dificuldade:",
            font=("Arial", 14)
        )
        instrucoes.pack(pady=10)

        tk.Button(
            self.janela,
            text="Fácil",
            width=20,
            command=lambda: self.iniciar_jogo(1)
        ).pack(pady=5)

        tk.Button(
            self.janela,
            text="Médio",
            width=20,
            command=lambda: self.iniciar_jogo(2)
        ).pack(pady=5)

        tk.Button(
            self.janela,
            text="Difícil",
            width=20,
            command=lambda: self.iniciar_jogo(3)
        ).pack(pady=5)

    def iniciar_jogo(self, dificuldade):
        if dificuldade == 1:
            self.limite = 50
            self.tentativas = 10

        elif dificuldade == 2:
            self.limite = 100
            self.tentativas = 7

        elif dificuldade == 3:
            self.limite = 500
            self.tentativas = 5

        self.numero_secreto = random.randint(1, self.limite)
        self.numeros_usados = []

        self.mostrar_jogo()

    def mostrar_jogo(self):
        self.limpar_tela()

        titulo = tk.Label(
            self.janela,
            text="JOGO DE ADIVINHAÇÃO",
            font=("Arial", 22, "bold")
        )
        titulo.pack(pady=20)

        instrucoes = tk.Label(
            self.janela,
            text=f"Tente adivinhar um número entre 1 e {self.limite}"
        )
        instrucoes.pack(pady=5)

        self.status = tk.Label(
            self.janela,
            text=f"Tentativas restantes: {self.tentativas}",
            font=("Arial", 12)
        )
        self.status.pack(pady=10)

        self.entrada = tk.Entry(
            self.janela,
            font=("Arial", 16),
            justify="center"
        )
        self.entrada.pack(pady=10)

        self.botao_tentar = tk.Button(
            self.janela,
            text="Tentar",
            width=15,
            command=self.tentar
        )
        self.botao_tentar.pack(pady=5)

        self.mensagem = tk.Label(
            self.janela,
            text="",
            font=("Arial", 12),
            wraplength=400
        )
        self.mensagem.pack(pady=15)

        self.historico = tk.Label(
            self.janela,
            text="Histórico: nenhum palpite ainda",
            wraplength=400
        )
        self.historico.pack(pady=10)

        self.entrada.focus()

        # Permite apertar Enter para fazer uma tentativa
        self.janela.bind("<Return>", self.tentar)

    def tentar(self, event=None):
        entrada = self.entrada.get()

        if not entrada.isdigit():
            self.mensagem.config(
                text="Por favor, digite um número válido."
            )
            return

        palpite = int(entrada)

        if palpite < 1 or palpite > self.limite:
            self.mensagem.config(
                text=f"Digite um número entre 1 e {self.limite}."
            )
            return

        if palpite in self.numeros_usados:
            self.mensagem.config(
                text="Você já tentou esse número."
            )
            return

        self.numeros_usados.append(palpite)
        self.tentativas -= 1

        self.status.config(
            text=f"Tentativas restantes: {self.tentativas}"
        )

        self.historico.config(
            text=f"Histórico: {self.numeros_usados}"
        )

        self.entrada.delete(0, tk.END)

        if palpite == self.numero_secreto:
            self.mensagem.config(
                text="🎉 Parabéns! Você acertou!",
                font=("Arial", 14, "bold")
            )
            self.finalizar_jogo()
            return

        if palpite < self.numero_secreto:
            self.mensagem.config(
                text=f"O número secreto é maior que {palpite}."
            )
        else:
            self.mensagem.config(
                text=f"O número secreto é menor que {palpite}."
            )

        if self.tentativas == 0:
            self.mensagem.config(
                text=f"Suas tentativas acabaram!\n"
                     f"O número secreto era {self.numero_secreto}."
            )
            self.finalizar_jogo()

    def finalizar_jogo(self):
        self.botao_tentar.config(state=tk.DISABLED)
        self.entrada.config(state=tk.DISABLED)

        botao_novamente = tk.Button(
            self.janela,
            text="Jogar novamente",
            command=self.mostrar_tela_dificuldade
        )
        botao_novamente.pack(pady=10)

        botao_sair = tk.Button(
            self.janela,
            text="Sair",
            command=self.janela.destroy
        )
        botao_sair.pack(pady=5)


janela = tk.Tk()

jogo = JogoAdivinhacao(janela)

janela.mainloop()
import tkinter as tk

janela = tk.Tk()

janela.title("Jogo de Adivinhação")
janela.geometry("500x400")

label = tk.Label(janela, text="Jogo de adivinhação", font=('Arial', 18))
label.pack()
janela.mainloop()
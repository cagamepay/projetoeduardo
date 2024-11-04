# Implementação da interface do usuário e interações (exemplo básico)
import tkinter as tk

class UI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculatrix - Jogo")
        self.root.geometry("700x500")

    def show(self):
        tk.Label(self.root, text="Calculatrix - Jogo", font=("Arial", 20)).pack(pady=20)

        # Exemplos de botões de interação
        tk.Button(self.root, text="Iniciar Jogo", command=self.start_game).pack(pady=10)
        tk.Button(self.root, text="Sair", command=self.root.destroy).pack(pady=10)

        self.root.mainloop()

    def start_game(self):
        self.root.destroy()
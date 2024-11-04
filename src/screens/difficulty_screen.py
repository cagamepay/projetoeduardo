import tkinter as tk

class DifficultyScreen:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Escolha a Dificuldade")
        self.root.geometry("400x300")

    def show(self):
        tk.Label(self.root, text="Escolha a Dificuldade", font=("Helvetica Neue", 18)).pack(pady=20)

        easy_button = tk.Button(self.root, text="Fácil", command=self.start_game)
        easy_button.pack(pady=10)

        medium_button = tk.Button(self.root, text="Médio", command=self.start_game)
        medium_button.pack(pady=10)

        hard_button = tk.Button(self.root, text="Difícil", command=self.start_game)
        hard_button.pack(pady=10)

        self.root.mainloop()

    def start_game(self):
        from src.game.game import Game  # Importa aqui
        jogo = Game()
        jogo.start()
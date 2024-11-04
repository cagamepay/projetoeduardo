import tkinter as tk

class SubjectScreen:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Escolha a Matéria")
        self.root.geometry("400x300")

    def show(self):
        tk.Label(self.root, text="Escolha a Matéria", font=("Helvetica Neue", 18)).pack(pady=20)

        math_button = tk.Button(self.root, text="Matemática", command=self.start_game)
        math_button.pack(pady=10)

        portuguese_button = tk.Button(self.root, text="Português", command=self.start_game)
        portuguese_button.pack(pady=10)

        self.root.mainloop()

    def start_game(self):
        from src.game.game import Game  # Importa aqui
        jogo = Game()
        jogo.start()
import tkinter as tk

class GameScreen:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Jogo")
        self.root.geometry("600x400")

    def show(self):
        tk.Label(self.root, text="Bem-vindo ao Jogo!", font=("Helvetica Neue", 24)).pack(pady=20)
        # Aqui você pode adicionar a lógica do jogo

        self.root.mainloop()
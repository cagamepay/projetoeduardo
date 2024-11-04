import tkinter as tk

class SummaryScreen:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Resumo do Jogo")
        self.root.geometry("400x300")

    def show(self):
        tk.Label(self.root, text="Resumo do Jogo", font=("Helvetica Neue", 18)).pack(pady=20)
        # Aqui você pode adicionar a lógica para mostrar o resumo do jogo

        self.root.mainloop()
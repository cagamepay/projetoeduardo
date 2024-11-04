import tkinter as tk

class StartScreen:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculatrix - Bem-vindo ao Jogo Educacional!")
        self.root.geometry("700x500")
        self.root.configure(bg="#f0f0f0")

        self.canvas = tk.Canvas(self.root, width=700, height=500)
        self.canvas.pack(fill="both", expand=True)

        # Tente carregar a imagem de fundo
        try:
            self.bg_image = tk.PhotoImage(file="assets/images/logo.png")
            self.canvas.create_image(0, 0, image=self.bg_image, anchor="nw")
        except Exception as e:
            print("Imagem de fundo não encontrada:", e)
            self.bg_image = None  # Define bg_image como None se não for carregada

        self.setup_ui()  # Chama a configuração da interface independentemente do carregamento da imagem

    def setup_ui(self):
        title_label = tk.Label(
            self.root,
            text="Calculatrix",
            font=("Helvetica Neue", 44, "bold", "italic"),
            fg="#2E86C1",
            bg="#f0f0f0"
        )
        self.canvas.create_window(350, 100, window=title_label)

        start_button = tk.Button(
            self.root,
            text="Iniciar Jogo",
            font=("Helvetica Neue", 18, "bold"),
            bg="#5DADE2",
            fg="white",
            activebackground="#3498DB",
            activeforeground="white",
            relief="raised",
            bd=5,
            width=15,
            command=self.start_game
        )
        self.canvas.create_window(350, 300, window=start_button)

        welcome_message = tk.Label(
            self.root,
            text="Desafie seu conhecimento e aprenda brincando!",
            font=("Helvetica Neue", 14, "italic"),
            fg="#1F618D",
            bg="#f0f0f0"
        )
        self.canvas.create_window(350, 200, window=welcome_message)

        footer_label = tk.Label(
            self.root,
            text="Calculatrix © 2024 - Aprendizado Divertido para Todos",
            font=("Helvetica Neue", 10),
            fg="#839192",
            bg="#f0f0f0"
        )
        self.canvas.create_window(350, 480, window=footer_label)

        self.root.mainloop()  # Inicia o loop principal da interface

    def start_game(self):
        from src.game.game import Game  # Importa aqui
        jogo = Game()
        jogo.start()

# Para iniciar a tela inicial
if __name__ == "__main__":
    StartScreen()
class Game:
    def __init__(self):
        # Inicialização do jogo
        pass

    def start(self):
        from src.screens.start_screen import StartScreen  # Importa aqui
        start_screen = StartScreen()
        start_screen.show()
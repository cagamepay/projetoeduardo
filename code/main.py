import pygame
import sys
from settings import *
from level import Level
from tela_inicial.tela_inicial import *  # Corrige o import

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Sprout Land")
        self.clock = pygame.time.Clock()
        self.level = Level()
        self.running_game = False  # Flag para iniciar o loop principal do jogo
        self.main_menu = TelaInicial(self.screen)  # Instancia a tela inicial corretamente

    def run(self):
        while True:
            if not self.running_game:
                # Mostra a tela inicial enquanto o jogo não está rodando
                self.running_game = self.main_menu.run()
            else:
                # Loop principal do jogo
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                dt = self.clock.tick() / 1500
                self.level.run(dt)
                pygame.display.update()

if __name__ == "__main__":
    game = Game()
    game.run()

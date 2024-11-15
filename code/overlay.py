import pygame
from settings import *

class Overlay:
    def __init__(self, player):

        # general setup
        self.display_surface = pygame.display.get_surface()
        self.player = player

        # imports
        overlay_path = 'graphics/overlay/'
        self.seeds_surf = {seed: pygame.image.load(f'{overlay_path}{seed}.png').convert_alpha() for seed in player.seeds}

        # font setup
        self.font = pygame.font.Font(None, 28)  # Tamanho da fonte aumentado

    def display(self):
        # seeds image
        seed_surf = self.seeds_surf[self.player.selected_seed]
        seed_rect = seed_surf.get_rect(midbottom=OVERLAY_POSITIONS['seed'])
        self.display_surface.blit(seed_surf, seed_rect)

        # seeds count with shadow effect
        seed_count = self.player.seed_inventory[self.player.selected_seed]
        
        # Renderizando o texto da borda em preto
        count_surf_black = self.font.render(str(seed_count), True, (0, 0, 0))
        count_rect_black = count_surf_black.get_rect(midbottom=(seed_rect.midbottom[0], seed_rect.midbottom[1] - 150))
        
        # Renderizando o texto principal em branco
        count_surf_white = self.font.render(str(seed_count), True, (255, 255, 255))
        count_rect_white = count_surf_white.get_rect(midbottom=(seed_rect.midbottom[0], seed_rect.midbottom[1] - 152))
        
        # Exibindo a borda preta primeiro e, em seguida, o texto branco
        self.display_surface.blit(count_surf_black, count_rect_black)
        self.display_surface.blit(count_surf_white, count_rect_white)

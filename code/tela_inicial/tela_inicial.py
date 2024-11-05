import pygame
import sys

# Configurações de tela e cores
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
WHITE = (255, 255, 255)
LIGHT_GRAY = (200, 200, 200)
SHADOW_COLOR = (50, 50, 50)

class TelaInicial:
    def __init__(self, screen):
        self.screen = screen
        self.background = pygame.image.load(r"C:\Users\c0mbe\OneDrive\Área de Trabalho\stardw\PyDew-Valley\code\tela_inicial\background.png")
        self.background = pygame.transform.scale(self.background, (SCREEN_WIDTH, SCREEN_HEIGHT))

        # Carregar fontes e imagens
        try:
            self.title_font = pygame.font.Font(r"C:\Users\c0mbe\OneDrive\Área de Trabalho\stardw\PyDew-Valley\code\tela_inicial\drake.otf", 72)
            self.start_button_font = pygame.font.Font(r"C:\Users\c0mbe\OneDrive\Área de Trabalho\stardw\PyDew-Valley\code\tela_inicial\drake.otf", 48)
            self.settings_button_font = pygame.font.Font(r"C:\Users\c0mbe\OneDrive\Área de Trabalho\stardw\PyDew-Valley\code\tela_inicial\drake.otf", 40)
            self.help_button_font = pygame.font.Font(r"C:\Users\c0mbe\OneDrive\Área de Trabalho\stardw\PyDew-Valley\code\tela_inicial\drake.otf", 36)
            self.credits_button_font = pygame.font.Font(r"C:\Users\c0mbe\OneDrive\Área de Trabalho\stardw\PyDew-Valley\code\tela_inicial\drake.otf", 32)
        except FileNotFoundError:
            print("Fonte 'drake.otf' não encontrada.")
            pygame.quit()
            sys.exit()

        button_image_path = r"C:\Users\c0mbe\OneDrive\Área de Trabalho\stardw\PyDew-Valley\code\tela_inicial\button.png"
        self.button_image = pygame.image.load(button_image_path)
        self.button_image = pygame.transform.scale(self.button_image, (300, 80))
        self.title_y = 100  # Posição do título

    def draw_button(self, text, position, font, hovered=False):
        # Ajusta a imagem do botão no hover
        scaled_button = pygame.transform.scale(self.button_image, (320, 85)) if hovered else self.button_image
        button_rect = scaled_button.get_rect(center=position)
        self.screen.blit(scaled_button, button_rect)

        # Desenha o texto centralizado no botão
        text_color = LIGHT_GRAY if hovered else WHITE
        text_surf = font.render(text, True, text_color)
        text_rect = text_surf.get_rect(center=button_rect.center)
        self.screen.blit(text_surf, text_rect)
        
        return button_rect

    def run(self):
        # Exibe a tela inicial e aguarda o clique nos botões
        self.screen.blit(self.background, (0, 0))

        # Desenha o título com sombra
        title_text = self.title_font.render("Ethan Drake", True, WHITE)
        shadow_text = self.title_font.render("Ethan Drake", True, SHADOW_COLOR)
        self.screen.blit(shadow_text, (SCREEN_WIDTH // 2 - shadow_text.get_width() // 2 + 5, self.title_y + 5))
        self.screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, self.title_y))

        # Posição do mouse e hover nos botões
        mouse_pos = pygame.mouse.get_pos()

        # Criação dos botões com fontes e tamanhos específicos
        start_button = self.draw_button("Iniciar Jogo", (SCREEN_WIDTH // 2, 300), self.start_button_font, hovered=pygame.Rect(self.draw_button("Iniciar Jogo", (SCREEN_WIDTH // 2, 300), self.start_button_font)).collidepoint(mouse_pos))
        settings_button = self.draw_button("Configuracoes", (SCREEN_WIDTH // 2, 400), self.settings_button_font, hovered=pygame.Rect(self.draw_button("Configurações", (SCREEN_WIDTH // 2, 400), self.settings_button_font)).collidepoint(mouse_pos))
        help_button = self.draw_button("Ajuda", (SCREEN_WIDTH // 2, 500), self.help_button_font, hovered=pygame.Rect(self.draw_button("Ajuda", (SCREEN_WIDTH // 2, 500), self.help_button_font)).collidepoint(mouse_pos))
        credits_button = self.draw_button("Creditos", (SCREEN_WIDTH // 2, 600), self.credits_button_font, hovered=pygame.Rect(self.draw_button("Créditos", (SCREEN_WIDTH // 2, 600), self.credits_button_font)).collidepoint(mouse_pos))

        # Loop de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Verifica cliques em cada botão
                if start_button.collidepoint(event.pos):
                    print("Iniciar Jogo clicado")
                    return "iniciar_jogo"
                elif settings_button.collidepoint(event.pos):
                    print("Configurações clicado")
                    return "configuracoes"
                elif help_button.collidepoint(event.pos):
                    print("Ajuda clicado")
                    return "ajuda"
                elif credits_button.collidepoint(event.pos):
                    print("Créditos clicado")
                    return "creditos"

        pygame.display.flip()
        return None

# Código principal para executar a tela inicial
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Tela Inicial")
    tela_inicial = TelaInicial(screen)

    # Loop principal
    while True:
        action = tela_inicial.run()
        if action == "iniciar_jogo":
            print("Jogo iniciado!")
            break
        elif action == "configuracoes":
            print("Abrir Configurações...")
            # Adicione lógica para abrir a tela de configurações aqui
        elif action == "ajuda":
            print("Abrir Ajuda...")
            # Adicione lógica para abrir a tela de ajuda aqui
        elif action == "creditos":
            print("Abrir Créditos...")
            # Adicione lógica para abrir a tela de créditos aqui

if __name__ == "__main__":
    main()

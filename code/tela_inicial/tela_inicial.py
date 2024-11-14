import pygame
import sys

# Configurações de tela e cores
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
WHITE = (255, 255, 255)
LIGHT_GRAY = (200, 200, 200)
DARK_GRAY = (100, 100, 100)
YELLOW = (255, 223, 0)
SHADOW_COLOR = (50, 50, 50)
MODAL_BACKGROUND = (30, 30, 30)
MODAL_BORDER = (255, 215, 0)
MODAL_SHADOW = (20, 20, 20)
RESOLUCOES = [(800, 800), (1024, 768), (1280, 720), (1920, 1080)]


Caminhos = {
    "title_font": r"C:\\Users\\c0mbe\\OneDrive\\Área de Trabalho\stardw\\PyDew-Valley\\code\\tela_inicial\\drake.otf",
    "button_image": r"C:\\Users\\c0mbe\\OneDrive\\Área de Trabalho\stardw\\PyDew-Valley\\code\\tela_inicial\\button.png",
    "background_image": r"C:\\Users\\c0mbe\\OneDrive\\Área de Trabalho\stardw\\PyDew-Valley\\code\\tela_inicial\\background.png"
}

class TelaInicial:
    def __init__(self, screen):
        self.screen = screen
        self.resolucao_atual = 0
        self.language = "English"
        self.update_dimensions()

        try:
            self.title_font = pygame.font.Font(Caminhos["title_font"], 72)
            self.start_button_font = pygame.font.Font(Caminhos["title_font"], 48)
            self.settings_button_font = pygame.font.Font(Caminhos["title_font"], 40)
            self.help_button_font = pygame.font.Font(Caminhos["title_font"], 36)
            self.credits_button_font = pygame.font.Font(Caminhos["title_font"], 32)
        except FileNotFoundError:
            print("Fonte 'drake.otf' não encontrada.")
            pygame.quit()
            sys.exit()

        self.button_image = pygame.image.load(Caminhos["button_image"])
        self.update_button_image()
        self.title_y = 100  # Posição do título

    def update_dimensions(self):
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = RESOLUCOES[self.resolucao_atual]
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.background = pygame.image.load(Caminhos["background_image"])
        self.background = pygame.transform.scale(self.background, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

    def update_button_image(self):
        button_width = int(300 * (self.SCREEN_WIDTH / 800))
        button_height = int(80 * (self.SCREEN_HEIGHT / 800))
        self.button_image = pygame.transform.scale(self.button_image, (button_width, button_height))

    def draw_button(self, text, position, font, hovered=False):
        button_width = int(300 * (self.SCREEN_WIDTH / 800))
        button_height = int(80 * (self.SCREEN_HEIGHT / 800))
        scaled_button = pygame.transform.scale(self.button_image, (int(button_width * 1.1), int(button_height * 1.1))) if hovered else self.button_image
        button_rect = scaled_button.get_rect(center=position)
        self.screen.blit(scaled_button, button_rect)
        text_color = LIGHT_GRAY if hovered else WHITE
        text_surf = font.render(text, True, text_color)
        text_rect = text_surf.get_rect(center=button_rect.center)
        self.screen.blit(text_surf, text_rect)
        return button_rect

    def draw_back_button(self):
        # Definir estilo do botão de voltar
        button_width, button_height = 100, 50
        button_color = DARK_GRAY
        text_color = WHITE
        hover_color = (170, 170, 170)
        position = (20, 20)
        font = pygame.font.Font(None, 40)
        text = "< Back" if self.language == "English" else "< Voltar"

        mouse_pos = pygame.mouse.get_pos()
        hovered = position[0] <= mouse_pos[0] <= position[0] + button_width and position[1] <= mouse_pos[1] <= position[1] + button_height

        color = hover_color if hovered else button_color
        back_button_rect = pygame.Rect(position, (button_width, button_height))
        pygame.draw.rect(self.screen, color, back_button_rect, border_radius=10)

        text_surf = font.render(text, True, text_color)
        text_rect = text_surf.get_rect(center=back_button_rect.center)
        self.screen.blit(text_surf, text_rect)

        return back_button_rect

    def draw_credits_modal(self):
        # Definir dimensões e estilo do modal
        modal_width, modal_height = 600, 400
        modal_x = (self.SCREEN_WIDTH - modal_width) // 2
        modal_y = (self.SCREEN_HEIGHT - modal_height) // 2
        modal_rect = pygame.Rect(modal_x, modal_y, modal_width, modal_height)

        # Desenhar sombra do modal
        shadow_offset = 10
        shadow_rect = pygame.Rect(modal_x + shadow_offset, modal_y + shadow_offset, modal_width, modal_height)
        pygame.draw.rect(self.screen, MODAL_SHADOW, shadow_rect, border_radius=20)

        # Desenhar fundo do modal
        pygame.draw.rect(self.screen, MODAL_BACKGROUND, modal_rect, border_radius=20)
        pygame.draw.rect(self.screen, MODAL_BORDER, modal_rect, 5, border_radius=20)

        # Carregar título do modal
        title_font = pygame.font.Font(Caminhos["title_font"], 50)
        title_text = title_font.render("Creditos", True, YELLOW)
        title_rect = title_text.get_rect(center=(modal_x + modal_width // 2, modal_y + 50))
        self.screen.blit(title_text, title_rect)

        # Carregar nomes dos créditos
        credit_font = pygame.font.Font(Caminhos["title_font"], 36)
        credit_names = ["Thiago", "Thiago", "Thiago", "Thiago"]
        for i, name in enumerate(credit_names):
            name_text = credit_font.render(name, True, WHITE)
            name_rect = name_text.get_rect(center=(modal_x + modal_width // 2, modal_y + 120 + i * 60))
            self.screen.blit(name_text, name_rect)

        # Adicionar uma linha decorativa horizontal para melhor estética
        line_y = modal_y + 90
        pygame.draw.line(self.screen, MODAL_BORDER, (modal_x + 20, line_y), (modal_x + modal_width - 20, line_y), 3)

    def run(self):
        self.screen.blit(self.background, (0, 0))
        title_text = self.title_font.render("Ethan Drake", True, WHITE)
        shadow_text = self.title_font.render("Ethan Drake", True, SHADOW_COLOR)
        self.screen.blit(shadow_text, (self.SCREEN_WIDTH // 2 - shadow_text.get_width() // 2 + 5, self.title_y + 5))
        self.screen.blit(title_text, (self.SCREEN_WIDTH // 2 - title_text.get_width() // 2, self.title_y))

        mouse_pos = pygame.mouse.get_pos()
        start_button_text = "Start Game" if self.language == "English" else "Iniciar Jogo"
        settings_button_text = "Settings" if self.language == "English" else "Configuracoes"
        help_button_text = "Help" if self.language == "English" else "Ajuda"
        credits_button_text = "Credits" if self.language == "English" else "Creditos"

        start_button = self.draw_button(start_button_text, (self.SCREEN_WIDTH // 2, int(300 * (self.SCREEN_HEIGHT / 800))), self.start_button_font, hovered=pygame.Rect(self.draw_button(start_button_text, (self.SCREEN_WIDTH // 2, int(300 * (self.SCREEN_HEIGHT / 800))), self.start_button_font)).collidepoint(mouse_pos))
        settings_button = self.draw_button(settings_button_text, (self.SCREEN_WIDTH // 2, int(400 * (self.SCREEN_HEIGHT / 800))), self.settings_button_font, hovered=pygame.Rect(self.draw_button(settings_button_text, (self.SCREEN_WIDTH // 2, int(400 * (self.SCREEN_HEIGHT / 800))), self.settings_button_font)).collidepoint(mouse_pos))
        help_button = self.draw_button(help_button_text, (self.SCREEN_WIDTH // 2, int(500 * (self.SCREEN_HEIGHT / 800))), self.help_button_font, hovered=pygame.Rect(self.draw_button(help_button_text, (self.SCREEN_WIDTH // 2, int(500 * (self.SCREEN_HEIGHT / 800))), self.help_button_font)).collidepoint(mouse_pos))
        credits_button = self.draw_button(credits_button_text, (self.SCREEN_WIDTH // 2, int(600 * (self.SCREEN_HEIGHT / 800))), self.credits_button_font, hovered=pygame.Rect(self.draw_button(credits_button_text, (self.SCREEN_WIDTH // 2, int(600 * (self.SCREEN_HEIGHT / 800))), self.credits_button_font)).collidepoint(mouse_pos))
        back_button = self.draw_back_button()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    print("Iniciar Jogo clicado" if self.language == "Portuguese" else "Start Game clicked")
                    return "iniciar_jogo"
                elif settings_button.collidepoint(event.pos):
                    print("Configurações clicado" if self.language == "Portuguese" else "Settings clicked")
                    return "configuracoes"
                elif help_button.collidepoint(event.pos):
                    print("Ajuda clicado" if self.language == "Portuguese" else "Help clicked")
                    return "ajuda"
                elif credits_button.collidepoint(event.pos):
                    print("Créditos clicado" if self.language == "Portuguese" else "Credits clicked")
                    self.draw_credits_modal()
                    pygame.display.flip()
                    pygame.time.wait(3000)  # Espera 3 segundos para visualizar o modal
                elif back_button.collidepoint(event.pos):
                    print("Voltar clicado" if self.language == "Portuguese" else "Back clicked")
                    return "voltar"

        pygame.display.flip()
        return None

class TelaConfiguracoes:
    def __init__(self, screen, background):
        self.screen = screen
        self.background = background
        self.resolucao_atual = 0
        self.volume = 25  # Volume inicial
        self.musica = True
        self.saida_audio = "Auto"
        self.dynamic_range = "Medium"
        self.language = "English"
        self.subtitles = True
        
        # Carregar fonte
        try:
            self.font = pygame.font.Font(Caminhos["title_font"], 36)
        except FileNotFoundError:
            print("Fonte 'drake.otf' não encontrada.")
            pygame.quit()
            sys.exit()

        self.update_dimensions()

    def update_dimensions(self):
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = RESOLUCOES[self.resolucao_atual]
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.background = pygame.transform.scale(self.background, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

    def draw_slider(self, label, value, position):
        label_surface = self.font.render(label, True, WHITE)
        self.screen.blit(label_surface, position)
        slider_rect = pygame.Rect(position[0] + 300, position[1] + 10, 200, 10)
        pygame.draw.rect(self.screen, LIGHT_GRAY, slider_rect)
        fill_width = int(slider_rect.width * (value / 100))
        pygame.draw.rect(self.screen, YELLOW, (slider_rect.x, slider_rect.y, fill_width, slider_rect.height))
        return slider_rect

    def draw_toggle(self, label, state, position):
        label_surface = self.font.render(label, True, WHITE)
        self.screen.blit(label_surface, position)
        toggle_rect = pygame.Rect(position[0] + 300, position[1], 100, 40)
        pygame.draw.rect(self.screen, DARK_GRAY if not state else YELLOW, toggle_rect, border_radius=20)
        state_text = "ON" if state else "OFF"
        state_surface = self.font.render(state_text, True, WHITE)
        self.screen.blit(state_surface, (toggle_rect.x + 25, toggle_rect.y + 5))
        return toggle_rect

    def draw_back_button(self):
        # Definir estilo do botão de voltar
        button_width, button_height = 120, 50
        button_color = DARK_GRAY
        text_color = WHITE
        hover_color = (170, 170, 170)
        position = (20, 20)
        font = pygame.font.Font(None, 40)
        text = "< Back" if self.language == "English" else "< Voltar"

        mouse_pos = pygame.mouse.get_pos()
        hovered = position[0] <= mouse_pos[0] <= position[0] + button_width and position[1] <= mouse_pos[1] <= position[1] + button_height

        color = hover_color if hovered else button_color
        back_button_rect = pygame.Rect(position, (button_width, button_height))
        pygame.draw.rect(self.screen, SHADOW_COLOR, back_button_rect.move(5, 5), border_radius=10)  # Sombra
        pygame.draw.rect(self.screen, color, back_button_rect, border_radius=10)

        text_surf = font.render(text, True, text_color)
        text_rect = text_surf.get_rect(center=back_button_rect.center)
        self.screen.blit(text_surf, text_rect)

        return back_button_rect

    def draw_resolution_options(self, position):
        label_surface = self.font.render("Resolução" if self.language == "Portuguese" else "Resolution", True, WHITE)
        self.screen.blit(label_surface, position)
        res_rects = []
        for i, res in enumerate(RESOLUCOES):
            res_text = f"{res[0]}x{res[1]}"
            color = YELLOW if i == self.resolucao_atual else LIGHT_GRAY
            res_surface = self.font.render(res_text, True, color)
            res_position = (position[0] + 300, position[1] + i * 50)
            res_rect = res_surface.get_rect(topleft=res_position)
            self.screen.blit(res_surface, res_rect)
            res_rects.append((res_rect, i))
        return res_rects

    def run(self):
        running = True
        while running:
            self.screen.blit(self.background, (0, 0))
            config_text = self.font.render("Configurações" if self.language == "Portuguese" else "Settings", True, WHITE)
            self.screen.blit(config_text, (self.screen.get_width() // 2 - config_text.get_width() // 2, 20))

            # Volume
            volume_label = "Volume Principal" if self.language == "Portuguese" else "Master Volume"
            volume_slider = self.draw_slider(volume_label, self.volume, (100, 100))
            # Música
            musica_label = "Música" if self.language == "Portuguese" else "Music"
            musica_button = self.draw_toggle(musica_label, self.musica, (100, 180))
            # Saída de áudio
            output_label = "Saída de Áudio" if self.language == "Portuguese" else "Audio Output"
            output_position = (100, 260)
            self.screen.blit(self.font.render(output_label, True, WHITE), output_position)
            self.screen.blit(self.font.render(self.saida_audio, True, YELLOW), (output_position[0] + 300, output_position[1]))

            # Idioma
            language_label = "Idioma" if self.language == "Portuguese" else "Language"
            language_button = self.draw_toggle(language_label, self.language == "Portuguese", (100, 340))

            # Subtítulos
            subtitles_label = "Legendas" if self.language == "Portuguese" else "Subtitles"
            subtitles_button = self.draw_toggle(subtitles_label, self.subtitles, (100, 420))

            # Resolução
            res_options = self.draw_resolution_options((100, 500))

            # Botão de voltar
            back_button = self.draw_back_button()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if musica_button.collidepoint(event.pos):
                        self.musica = not self.musica
                    elif language_button.collidepoint(event.pos):
                        self.language = "Portuguese" if self.language == "English" else "English"
                    elif subtitles_button.collidepoint(event.pos):
                        self.subtitles = not self.subtitles
                    elif volume_slider.collidepoint(event.pos):
                        self.volume = int((event.pos[0] - volume_slider.x) / volume_slider.width * 100)
                    elif back_button.collidepoint(event.pos):
                        print("Voltar clicado" if self.language == "Portuguese" else "Back clicked")
                        return
                    for res_rect, i in res_options:
                        if res_rect.collidepoint(event.pos):
                            self.resolucao_atual = i
                            self.update_dimensions()
                elif event.type == pygame.MOUSEMOTION:
                    if pygame.mouse.get_pressed()[0] and volume_slider.collidepoint(event.pos):
                        self.volume = max(0, min(100, int((event.pos[0] - volume_slider.x) / volume_slider.width * 100)))

            pygame.display.flip()

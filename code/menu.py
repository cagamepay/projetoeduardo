import pygame
from settings import *
from timer import Timer

class Menu1:
    def __init__(self, player, toggle_menu, questions=None, correct_indices=None):
        self.player = player
        self.toggle_menu = toggle_menu
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font('font/LycheeSoda.ttf', 50)

        # Propriedades de exibição
        self.width = 600
        self.space = 10
        self.padding = 8

        # Configurações de quiz
        
        self.questions = [
    ("Qual é a capital da França?", ["Mbappe", "Londres", "Roma", "Madri"], 0),
    ("O Calebe é gay?", ["sim", "não", "nem um pouco", "talvez"], 0),
    ("O Bernardo gosta de tomar de ladinho?", ["sim", "não", "às vezes", "nunca"], 3),
    ("Qual é a sobremesa favorita do Calebe?", ["Pudim", "Sorvete", "Brigadeiro", "Nenhuma, ele prefere salgado"], 3),
    ("O que o Calebe nunca recusa?", ["pinto", "Um debate político", "Um rolê aleatório", "Uma partida de videogame"], 0),
    ("Onde o Calebe passa mais tempo?", ["Academia", "putero", "Faculdade", "Na balada"], 1),
    ("Qual é o esporte favorito do Calebe?", ["Futebol", "Xadrez", "Natação", "Ele não gosta muito de esportes"], 3),
    ("O que o Calebe faz aos domingos?", ["Dormir o dia todo", "Estudar", "Ver série", "Sair com amigos"], 0),
    ("Qual é o prato preferido do Calebe?", ["droga", "Hambúrguer", "Sushi", "Churrasco"], 1),
    ("Quem é o maior rival do Calebe?", ["Bernardo", "O sono", "Trabalhos da faculdade", "A preguiça"], 2),
]


        self.correct_indices = correct_indices or []
        self.current_index = 0

        self.timer = Timer(200)
        self.setup_current_question()

    def setup_current_question(self):
        if self.current_index < len(self.questions):
            self.question, self.options, self.correct_index = self.questions[self.current_index]
            self.index = 0
            
            # Superfície de texto para a pergunta
            self.question_surf = self.font.render(self.question, False, 'Black')
            self.question_rect = self.question_surf.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4))

            # Superfícies de texto para as opções do quiz
            self.text_surfs = [self.font.render(option, False, 'Black') for option in self.options]
            self.menu_top = SCREEN_HEIGHT / 2 - (len(self.text_surfs) * (self.font.get_height() + self.padding) + (len(self.text_surfs) - 1) * self.space) / 2
        else:
            print("Fim do quiz!")
            self.toggle_menu()  # Sai do menu após todas as perguntas

    def input(self):
        keys = pygame.key.get_pressed()
        self.timer.update()

        if keys[pygame.K_ESCAPE]:
            self.toggle_menu()

        if not self.timer.active:
            if keys[pygame.K_UP]:
                self.index = (self.index - 1) % len(self.options)
                self.timer.activate()

            if keys[pygame.K_DOWN]:
                self.index = (self.index + 1) % len(self.options)
                self.timer.activate()

            if keys[pygame.K_SPACE]:
                self.timer.activate()
                
                # Verifica se a resposta está correta
                if self.index == self.correct_index:
                    print("Correto!")
                    self.current_index += 1
                    self.setup_current_question()  # Configura a próxima pergunta
                else:
                    print("Incorreto!")
                
                # Sai do menu após responder
                self.toggle_menu()  # Você pode comentar isso se quiser continuar no quiz sem sair

    def show_entry(self, text_surf, top, selected):
        # Fundo da opção
        bg_rect = pygame.Rect(SCREEN_WIDTH / 2 - self.width / 2, top, self.width, text_surf.get_height() + (self.padding * 2))
        pygame.draw.rect(self.display_surface, 'White', bg_rect, 0, 4)

        # Texto da opção
        text_rect = text_surf.get_rect(center=bg_rect.center)
        self.display_surface.blit(text_surf, text_rect)

        # Indicador de seleção
        if selected:
            pygame.draw.rect(self.display_surface, 'Black', bg_rect, 4, 4)

    def update(self):
        self.input()
        
        # Exibe a pergunta
        self.display_surface.blit(self.question_surf, self.question_rect)

        # Exibe as opções
        for i, text_surf in enumerate(self.text_surfs):
            top = self.menu_top + i * (text_surf.get_height() + (self.padding * 2) + self.space)
            self.show_entry(text_surf, top, self.index == i)
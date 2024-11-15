import pygame
from settings import *
from timer import Timer

class Menu2:
    def __init__(self, player, toggle_menu, questions=None, correct_indices=None):
        self.player = player
        self.toggle_menu = toggle_menu
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font('font/LycheeSoda.ttf', 50)

        # Configurações de exibição do menu
        self.width = 600
        self.space = 10
        self.padding = 8

        # Perguntas e opções do quiz
        self.questions = [
    ("O Calebe já se apaixonou por alguém na balada?", ["Sim", "Não", "Talvez", "Só pelas bebidas"], 0),
    ("Qual a opinião do Calebe sobre 'ficar'?", ["Ótimo", "Não sou fã", "Depende da pessoa", "Prefiro um namoro sério"], 0),
    ("O Calebe já deu um 'olá' para um desconhecido(a) de forma ousada?", ["Sim", "Não", "Eu acho que sim", "Só quando está bêbado"], 0),
    ("O que o Calebe faria em uma noite romântica?", ["Jantar à luz de velas", "Ir ao cinema", "Ver Netflix e pedir pizza", "Apostaria num rolezinho picante"], 3),
    ("O Calebe já se arrependeu de um beijo?", ["Sim", "Não", "Só quando era jovem", "Nunca, todos são inesquecíveis"], 2),
    ("Qual o segredo mais picante do Calebe?", ["Ele nunca conta", "Já teve um crush proibido", "Aquela história com a amiga", "Ele se acha um romântico"], 1),
    ("Se o Calebe fosse uma sobremesa, qual seria?", ["Sorvete quente", "Chocolate derretido", "Torta de morango", "Mousse de maracujá picante"], 3),
    ("O Calebe já fez algo espontâneo e atrevido?", ["Sim", "Não", "Quem sabe?", "Só quando está com coragem"], 0),
    ("Qual tipo de flerte o Calebe mais usa?", ["O olhar", "O humor", "A gentileza", "O 'deixa comigo'"], 3),
    ("O Calebe já recebeu uma cantada inusitada?", ["Sim", "Não", "Só de amigos", "Ele é quem dá as cantadas"], 0),
    ("Se o Calebe tivesse que escolher entre amor e diversão, o que escolheria?", ["Amor", "Diversão", "Os dois, ao mesmo tempo", "Não escolhe, curte os dois"], 2),
]


        self.correct_indices = correct_indices or []
        self.current_index = 0

        # Temporizador para controlar a entrada de usuário
        self.timer = Timer(200)
        self.setup_current_question()

    def setup_current_question(self):
        """Configura a pergunta e as opções atuais"""
        if self.current_index < len(self.questions):
            self.question, self.options, self.correct_index = self.questions[self.current_index]
            self.index = 0  # Índice da opção selecionada

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
        """Processa entradas do usuário para navegação no menu"""
        keys = pygame.key.get_pressed()
        self.timer.update()

        if keys[pygame.K_ESCAPE]:
            self.toggle_menu()  # Sai do menu

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
                else:
                    print("Incorreto!")

                # Avança para a próxima pergunta
                self.current_index += 1
                self.setup_current_question()

    def show_entry(self, text_surf, top, selected):
        """Desenha cada opção do menu com destaque para a selecionada"""
        bg_rect = pygame.Rect(SCREEN_WIDTH / 2 - self.width / 2, top, self.width, text_surf.get_height() + (self.padding * 2))
        pygame.draw.rect(self.display_surface, 'White', bg_rect, 0, 4)
        text_rect = text_surf.get_rect(center=bg_rect.center)
        self.display_surface.blit(text_surf, text_rect)

        # Indicador de seleção
        if selected:
            pygame.draw.rect(self.display_surface, 'Black', bg_rect, 4, 4)

    def update(self):
        """Atualiza o menu, lidando com entrada e exibição"""
        self.input()
        
        # Exibe a pergunta
        self.display_surface.blit(self.question_surf, self.question_rect)

        # Exibe as opções
        for i, text_surf in enumerate(self.text_surfs):
            top = self.menu_top + i * (text_surf.get_height() + (self.padding * 2) + self.space)
            self.show_entry(text_surf, top, self.index == i)

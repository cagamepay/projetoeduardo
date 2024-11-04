# Implementação do gerenciador de informações do jogador (exemplo básico)
class Player:
    def __init__(self):
        self.name = ""
        self.score = 0

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_score(self, score):
        self.score = score

    def get_score(self):
        return self.score
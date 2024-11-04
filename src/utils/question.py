# Implementação da estrutura de perguntas (exemplo básico)
class Question:
    def __init__(self, question, answers, correct):
        self.question = question
        self.answers = answers
        self.correct = correct
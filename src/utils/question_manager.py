# Implementação do gerenciador de perguntas (exemplo básico)
class QuestionManager:
    def __init__(self):
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)

    def get_question(self, index):
        return self.questions[index]
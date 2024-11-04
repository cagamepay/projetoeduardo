# Implementação de lógica e perguntas de matemática (exemplo básico)
class Math:
    def __init__(self):
        self.questions = [
            {"question": "2 + 2 =", "answers": ["3", "4", "5"], "correct": "4"},
            {"question": "5 - 1 =", "answers": ["3", "4", "6"], "correct": "4"},
            # Adicione mais perguntas aqui
        ]

    def get_question(self, index):
        return self.questions[index]
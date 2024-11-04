# Implementação de lógica e perguntas de português (exemplo básico)
class Portuguese:
    def __init__(self):
        self.questions = [
            {"question": "Qual é o nome do autor de 'O Guarani'?", "answers": ["José de Alencar", "Machado de Assis", "Euclides da Cunha"], "correct": "José de Alencar"},
            {"question": "Qual é o nome do personagem principal de 'O Alienista'?", "answers": ["Simão Bacamarte", "Bento Santiago", "D. Quixote"], "correct": "Simão Bacamarte"},
            # Adicione mais perguntas aqui
        ]

    def get_question(self, index):
        return self.questions[index]
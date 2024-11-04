from utils.question import Question

class Subject:
    def __init__(self, name):
        self.name = name
        self.questions = []

    def add_questions(self, questions):
        self.questions.extend(questions)

class Math(Subject):
    def __init__(self):
        super().__init__("Matemática")
        self .add_questions([
            Question("Quanto é 2 + 2?", "4"),
            Question("Quanto é 3 * 3?", "9")
        ])

class Science(Subject):
    def __init__(self):
        super().__init__("Ciências")
        self.add_questions([
            Question("Qual é o maior planeta do Sistema Solar?", "Júpiter"),
            Question("O que as plantas produzem na fotossíntese?", "Oxigênio")
        ])

class History(Subject):
    def __init__(self):
        super().__init__("História")
        self.add_questions([
            Question("Quem foi o primeiro presidente dos EUA?", "George Washington"),
            Question("Em que ano o homem pisou na Lua pela primeira vez?", "1969")
        ])
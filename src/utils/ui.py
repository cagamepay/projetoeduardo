import tkinter as tk
from tkinter import messagebox

class Interface:
    def __init__(self, game):
        self.game = game
        self.root = tk.Tk()
        self.root.title("Calculatrix")

    def show_subject_menu(self, subjects):
        self.clear_screen()
        tk.Label(self.root, text="Escolha uma Matéria", font=("Arial", 18)).pack(pady=20)

        for subject in subjects:
            button = tk.Button(self.root, text=subject, font=("Arial", 14), width=20,
                               command=lambda s=subject: self.start_subject(s))
            button.pack(pady=10)

        self.root.mainloop()

    def start_subject(self, subject):
        self.clear_screen()
        self.game.select_subject(subject)
        self.show_question()

    def show_question(self):
        question = self.game.get_current_question()
        if not question:
            self.show_final_score()
            return

        tk.Label(self.root, text=question.text, font=("Arial", 14)).pack(pady=20)
        answer_entry = tk.Entry(self.root, font=("Arial", 14))
        answer_entry.pack(pady=10)

        submit_button = tk.Button(self.root, text="Responder", font=("Arial", 14),
                                  command=lambda: self.submit_answer(answer_entry.get()))
        submit_button.pack(pady=20)

    def submit_answer(self, answer):
        result = self.game.check_answer(answer)
        if result:
            messagebox.showinfo("Resultado", "Correto! Parabéns!")
        else:
            messagebox.showinfo("Resultado", "Errado! Vamos tentar outra vez.")

        self.clear_screen()
        self.show_question()

    def show_final_score(self):
        tk.Label(self.root, text="Jogo Finalizado!", font=("Arial", 18)).pack(pady=20)
        tk.Label(self.root, text=f"Sua pontuação: {self.game.player.score}", font=("Arial", 14)).pack(pady=10)
        tk.Button(self.root, text="Sair", font=("Arial", 14), command=self.root.quit).pack(pady=20)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
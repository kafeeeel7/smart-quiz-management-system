import tkinter as tk
from tkinter import messagebox
import random

questions = {
    "Python": [
        {"question1":"Who developed Python?","options":["Dennis Ritchie","Guido van Rossum","James Gosling","Linus Torvalds"],"answer":1},
        {"question":"Which symbol is used for comments?","options":["//","#","/*","&"],"answer":1},
        {"question":"Which keyword defines a function?","options":["function","def","fun","define"],"answer":1},
        {"question":"Which data type stores True/False?","options":["int","float","bool","str"],"answer":2},
        {"question":"Which function takes user input?","options":["scan()","cin()","input()","get()"],"answer":2},
        {"question":"Python is a ____ language.","options":["Compiled","Interpreted","Assembly","Machine"],"answer":1},
        {"question":"List starts indexing from?","options":["0","1","-1","2"],"answer":0},
        {"question":"Which is mutable?","options":["tuple","string","list","int"],"answer":2},
        {"question":"File extension of Python?","options":[".java",".cpp",".py",".c"],"answer":2},
        {"question":"Which loop repeats while condition is true?","options":["for","while","switch","case"],"answer":1},
    ],
    "Science": [
        {"question":"Formula of water?","options":["CO2","H2O","O2","NaCl"],"answer":1},
        {"question":"Red Planet?","options":["Earth","Mars","Venus","Jupiter"],"answer":1},
        {"question":"Plants absorb?","options":["Oxygen","Hydrogen","Carbon Dioxide","Nitrogen"],"answer":2},
        {"question":"Unit of force?","options":["Pascal","Joule","Newton","Watt"],"answer":2},
        {"question":"The Sun is a?","options":["Planet","Moon","Star","Comet"],"answer":2},
        {"question":"Human heart has how many chambers?","options":["2","3","4","5"],"answer":2},
        {"question":"Gas essential for breathing?","options":["Oxygen","Nitrogen","Helium","Hydrogen"],"answer":0},
        {"question":"Speed of light is approximately?","options":["3x10^8 m/s","300 m/s","3000 m/s","3x10^6 m/s"],"answer":0},
        {"question":"Nearest star to Earth?","options":["Sirius","Sun","Polaris","Alpha Centauri"],"answer":1},
        {"question":"Boiling point of water?","options":["50°C","75°C","100°C","150°C"],"answer":2},
    ],
    "GK": [
        {"question":"Capital of India?","options":["Mumbai","Delhi","Kolkata","Chennai"],"answer":1},
        {"question":"Father of the Nation?","options":["Nehru","Gandhi","Patel","Bose"],"answer":1},
        {"question":"How many states in India?","options":["28","29","30","31"],"answer":0},
        {"question":"National animal of India?","options":["Lion","Tiger","Elephant","Leopard"],"answer":1},
        {"question":"Largest ocean?","options":["Indian","Atlantic","Pacific","Arctic"],"answer":2},
        {"question":"National flag has how many colors?","options":["2","3","4","5"],"answer":2},
        {"question":"Currency of India?","options":["Dollar","Rupee","Euro","Yen"],"answer":1},
        {"question":"Taj Mahal is in?","options":["Delhi","Agra","Jaipur","Mumbai"],"answer":1},
        {"question":"India became independent in?","options":["1945","1946","1947","1948"],"answer":2},
        {"question":"Largest continent?","options":["Europe","Africa","Asia","Australia"],"answer":2},
    ]
}

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Quiz Management System")
        self.root.geometry("700x500")

        self.name = ""
        self.score = 0
        self.current = 0
        self.time_left = 10

        self.welcome_screen()

    def clear(self):
        for w in self.root.winfo_children():
            w.destroy()

    def welcome_screen(self):
        self.clear()

        tk.Label(self.root, text="SMART QUIZ MANAGEMENT SYSTEM",
                 font=("Arial", 20, "bold")).pack(pady=30)

        tk.Label(self.root, text="Enter Your Name").pack()
        self.name_entry = tk.Entry(self, width=30) if False else tk.Entry(self.root, width=30)
        self.name_entry.pack(pady=10)

        tk.Button(self.root, text="Start", command=self.category_screen).pack(pady=20)

    def category_screen(self):
        self.name = self.name_entry.get().strip()
        if not self.name:
            messagebox.showerror("Error", "Please enter your name.")
            return

        self.clear()

        tk.Label(self.root, text="Choose Category",
                 font=("Arial", 18, "bold")).pack(pady=20)

        for cat in ["Python", "Science", "GK"]:
            tk.Button(self.root, text=cat, width=20,
                      command=lambda c=cat: self.start_quiz(c)).pack(pady=10)

    def start_quiz(self, category):
        self.category = category
        self.score = 0
        self.current = 0

        self.quiz_questions = random.sample(questions[category], 5)

        self.show_question()

    def show_question(self):
        self.clear()

        if self.current >= len(self.quiz_questions):
            self.show_result()
            return

        self.time_left = 10

        q = self.quiz_questions[self.current]

        self.q_label = tk.Label(
            self.root,
            text=f"Question {self.current+1} of {len(self.quiz_questions)}\n\n{q['question']}",
            font=("Arial", 14),
            wraplength=600
        )
        self.q_label.pack(pady=20)

        self.timer_label = tk.Label(self.root, text="Time Left: 10", font=("Arial", 12))
        self.timer_label.pack()

        self.answer_var = tk.IntVar(value=-1)

        for i, option in enumerate(q["options"]):
            tk.Radiobutton(
                self.root,
                text=option,
                variable=self.answer_var,
                value=i,
                font=("Arial", 11)
            ).pack(anchor="w", padx=150)

        tk.Button(self.root, text="Next", command=self.next_question).pack(pady=20)

        self.update_timer()

    def update_timer(self):
        self.timer_label.config(text=f"Time Left: {self.time_left} sec")

        if self.time_left > 0:
            self.time_left -= 1
            self.timer_job = self.root.after(1000, self.update_timer)
        else:
            self.next_question()

    def next_question(self):
        try:
            self.root.after_cancel(self.timer_job)
        except:
            pass

        selected = self.answer_var.get()
        correct = self.quiz_questions[self.current]["answer"]

        if selected == correct:
            self.score += 1

        self.current += 1
        self.show_question()

    def show_result(self):
        self.clear()

        percentage = (self.score / len(self.quiz_questions)) * 100

        if percentage >= 90:
            msg = "Outstanding Performance! 🌟"
        elif percentage >= 70:
            msg = "Great Job! 👍"
        elif percentage >= 50:
            msg = "Good Effort! 😊"
        else:
            msg = "Keep Practicing! 📚"

        with open("scores.txt", "a") as f:
            f.write(f"{self.name} - {self.category} - {self.score}/5\n")

        tk.Label(self.root, text="Quiz Completed",
                 font=("Arial", 20, "bold")).pack(pady=20)

        tk.Label(self.root,
                 text=f"Name: {self.name}\nCategory: {self.category}\nScore: {self.score}/5\nPercentage: {percentage:.0f}%\n\n{msg}",
                 font=("Arial", 14)).pack(pady=20)

        tk.Button(self.root, text="Play Again",
                  command=self.category_screen).pack(pady=10)

        tk.Button(self.root, text="Exit",
                  command=self.root.destroy).pack(pady=10)

root = tk.Tk()
app = QuizApp(root)
root.mainloop()

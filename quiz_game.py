import tkinter as tk
from tkinter import messagebox

# Quiz data
questions = [
    [
        "What is the correct way to define a class in Python?",
        "define class MyClass:",
        "class MyClass:",
        "class = MyClass:",
        "MyClass class:",
        2
    ],
    [
        "Which method is used to initialize object attributes in Python?",
        "__main__()",
        "__create__()",
        "__init__()",
        "constructor()",
        3
    ],
    [
        "What will this print?\nclass A:\n    def __init__(self):\n        print('A created')\na = A()",
        "None",
        "A created",
        "init",
        "Error",
        2
    ],
    [
        "What keyword is used to inherit from a class in Python?",
        "extends",
        "inherits",
        "derives",
        "class Child(Parent)",
        4
    ],
    [
        "What is the output of bool([]) in Python?",
        "True",
        "None",
        "False",
        "Error",
        3
    ]
]

prizes = [10, 20, 30, 40, 50]

# Game state
current_question = 0
score = 0

# Functions
def load_question():
    q = questions[current_question]
    question_label.config(text=q[0])
    option1.config(text=q[1])
    option2.config(text=q[2])
    option3.config(text=q[3])
    option4.config(text=q[4])
    score_label.config(text=f"Score: {score}")

def check_answer(choice):
    global current_question, score

    correct_answer = questions[current_question][5]

    if choice == correct_answer:
        score += prizes[current_question]
        messagebox.showinfo("Correct", "Correct answer!")
        current_question += 1

        if current_question < len(questions):
            load_question()
        else:
            messagebox.showinfo("Game Over", f"Quiz completed!\nFinal Score: {score}")
            root.destroy()
    else:
        messagebox.showerror("Wrong", f"Wrong answer!\nFinal Score: {score}")
        root.destroy()

# GUI setup
root = tk.Tk()
root.title("Interactive Python Quiz Game")
root.geometry("600x400")
root.resizable(False, False)

title_label = tk.Label(root, text="Python Quiz Game", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

score_label = tk.Label(root, text="Score: 0", font=("Arial", 12))
score_label.pack()

question_label = tk.Label(root, text="", font=("Arial", 12), wraplength=500, justify="left")
question_label.pack(pady=20)

option1 = tk.Button(root, width=40, command=lambda: check_answer(1))
option1.pack(pady=5)

option2 = tk.Button(root, width=40, command=lambda: check_answer(2))
option2.pack(pady=5)

option3 = tk.Button(root, width=40, command=lambda: check_answer(3))
option3.pack(pady=5)

option4 = tk.Button(root, width=40, command=lambda: check_answer(4))
option4.pack(pady=5)

load_question()
root.mainloop()

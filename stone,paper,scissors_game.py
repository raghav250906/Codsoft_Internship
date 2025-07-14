import tkinter as tk
from tkinter import messagebox
import random

class StonePaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("🎮 Stone Paper Scissors Game")
        self.root.geometry("400x500")
        self.root.configure(bg="#fdfcdc")

        self.choices = ["Stone 🪨", "Paper 📜", "Scissors ✂️"]

        # Title Label
        tk.Label(root, text="Let's Play!", font=("Comic Sans MS", 20, "bold"), bg="#fdfcdc", fg="#ff006e").pack(pady=20)

        # Display User Choice
        self.user_choice_label = tk.Label(root, text="Your Choice: ❔", font=("Helvetica", 15), bg="#fdfcdc")
        self.user_choice_label.pack(pady=10)

        # Display Computer Choice
        self.comp_choice_label = tk.Label(root, text="Computer Choice: ❔", font=("Helvetica", 15), bg="#fdfcdc")
        self.comp_choice_label.pack(pady=10)

        # Result Display
        self.result_label = tk.Label(root, text="", font=("Arial", 18, "bold"), bg="#fdfcdc", fg="#00b4d8")
        self.result_label.pack(pady=20)

        # Buttons Frame
        btn_frame = tk.Frame(root, bg="#fdfcdc")
        btn_frame.pack(pady=20)

        # Choice Buttons
        self.create_button(btn_frame, "Stone 🪨", "#ffcc29", "#6a040f", 0)
        self.create_button(btn_frame, "Paper 📜", "#a0c4ff", "#1d3557", 1)
        self.create_button(btn_frame, "Scissors ✂️", "#bdb2ff", "#3c096c", 2)

        # Restart Button
        restart = tk.Button(root, text="🔄 Restart", font=("Arial", 12, "bold"), width=15,
                            bg="#90be6d", fg="#264653", command=self.restart)
        restart.pack(pady=20)

    def create_button(self, parent, text, bg, fg, idx):
        btn = tk.Button(parent, text=text, width=12, font=("Arial", 11, "bold"),
                        bg=bg, fg=fg, command=lambda idx=idx: self.play(idx))
        btn.grid(row=0, column=idx, padx=8)

    def play(self, user_index):
        user_choice = self.choices[user_index]
        comp_choice = random.choice(self.choices)

        self.user_choice_label.config(text=f"Your Choice: {user_choice}")
        self.comp_choice_label.config(text=f"Computer Choice: {comp_choice}")

        result = self.check_winner(user_choice, comp_choice)
        self.result_label.config(text=result)

    def check_winner(self, user, comp):
        if user == comp:
            return "😎 It's a Tie!"
        elif (user == "Stone 🪨" and comp == "Scissors ✂️") or \
             (user == "Paper 📜" and comp == "Stone 🪨") or \
             (user == "Scissors ✂️" and comp == "Paper 📜"):
            return "🎉 You Win!"
        else:
            return "💻 Computer Wins!"

    def restart(self):
        self.user_choice_label.config(text="Your Choice: ❔")
        self.comp_choice_label.config(text="Computer Choice: ❔")
        self.result_label.config(text="")

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    app = StonePaperScissors(root)
    root.mainloop()
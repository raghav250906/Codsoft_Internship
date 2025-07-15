import tkinter as tk

class ColorfulCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator 🧮")
        self.root.geometry("350x500")
        self.root.configure(bg="#fefae0")

        self.expression = ""

        # Display screen
        self.display = tk.Entry(root, font=("Arial", 24), border=5, relief="groove",
                                bg="#fff", fg="#333", justify="right")
        self.display.pack(padx=20, pady=20, ipadx=8, ipady=20, fill="x")

        # Frame for buttons
        btn_frame = tk.Frame(root, bg="#fefae0")
        btn_frame.pack()

        # List of button labels
        buttons = [
            ["7", "8", "9", "÷"],
            ["4", "5", "6", "×"],
            ["1", "2", "3", "-"],
            ["C", "0", "=", "+"]
        ]

        # Create buttons dynamically
        for r, row in enumerate(buttons):
            for c, char in enumerate(row):
                btn = tk.Button(btn_frame, text=char, font=("Arial", 18, "bold"),
                                width=5, height=2, bd=0,
                                bg="#a0c4ff", fg="#1d3557",
                                activebackground="#457b9d", activeforeground="white",
                                command=lambda ch=char: self.click(ch))
                btn.grid(row=r, column=c, padx=5, pady=5)

                # Hover effect (changes background on hover)
                btn.bind("<Enter>", lambda e, b=btn: b.config(bg="#457b9d", fg="white"))
                btn.bind("<Leave>", lambda e, b=btn: b.config(bg="#a0c4ff", fg="#1d3557"))

    def click(self, char):
        if char == "C":
            self.expression = ""
            self.display.delete(0, tk.END)
        elif char == "=":
            try:
                exp = self.expression.replace("÷", "/").replace("×", "*")
                result = eval(exp)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
                self.expression = str(result)  # allow chaining calculations
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error!")
                self.expression = ""
        else:
            self.expression += char
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    ColorfulCalculator(root)
    root.mainloop()

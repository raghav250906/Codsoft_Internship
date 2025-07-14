import tkinter as tk

class SimpleCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("🖩 Simple Calculator by Raghav")
        self.root.geometry("350x500")
        self.root.configure(bg="#fef9ef")

        # Entry box for calculations
        self.input_text = tk.StringVar()
        self.entry = tk.Entry(root, textvariable=self.input_text, font=("Arial", 22), bd=5, relief="groove", justify="right", bg="#f1faee", fg="#1d3557")
        self.entry.pack(fill="both", ipadx=8, ipady=20, padx=10, pady=20)

        # Button frame
        btn_frame = tk.Frame(root, bg="#fef9ef")
        btn_frame.pack()

        # List of buttons in grid style
        buttons = [
            ('7', '#ffb703'), ('8', '#ffb703'), ('9', '#ffb703'), ('/', '#ff006e'),
            ('4', '#ffb703'), ('5', '#ffb703'), ('6', '#ffb703'), ('*', '#ff006e'),
            ('1', '#ffb703'), ('2', '#ffb703'), ('3', '#ffb703'), ('-', '#ff006e'),
            ('C', '#e63946'), ('0', '#ffb703'), ('=', '#06d6a0'), ('+', '#ff006e')
        ]

        # Create buttons dynamically
        row, col = 0, 0
        for (text, color) in buttons:
            btn = tk.Button(btn_frame, text=text, font=("Arial", 18, "bold"), width=6, height=3,
                            bg=color, fg="white", bd=0,
                            activebackground="#1d3557", activeforeground="white",
                            command=lambda t=text: self.on_click(t))
            btn.grid(row=row, column=col, padx=5, pady=5)

            col += 1
            if col > 3:
                col = 0
                row += 1

    def on_click(self, button_text):
        if button_text == "C":
            self.input_text.set("")
        elif button_text == "=":
            try:
                result = eval(self.input_text.get())
                self.input_text.set(str(result))
            except:
                self.input_text.set("Error")
        else:
            current = self.input_text.get()
            self.input_text.set(current + button_text)

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleCalculator(root)
    root.mainloop()

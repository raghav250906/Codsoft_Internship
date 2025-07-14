import tkinter as tk
from tkinter import messagebox
# Main app class
class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🌟 Raghav's To‑Do App")
        self.root.geometry("450x500")
        self.root.configure(bg="#fefae0")  # Light pastel background

        self.tasks = []  # list to store tasks

        # Title
        tk.Label(root, text="📝 My Daily Task List", font=("Comic Sans MS", 18, "bold"),
                 fg="#d62828", bg="#fefae0").pack(pady=10)

        # Frame for list and scrollbar
        main_frame = tk.Frame(root, bg="#fefae0")
        main_frame.pack()

        self.listbox = tk.Listbox(main_frame, width=40, height=12, font=("Segoe UI", 12),
                                  fg="#000", bg="#f9f9f9", selectbackground="#b5ead7")
        self.listbox.pack(side=tk.LEFT, padx=(10, 0), pady=10)

        scroll = tk.Scrollbar(main_frame)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.config(yscrollcommand=scroll.set)
        scroll.config(command=self.listbox.yview)

        # Entry to type task
        self.task_input = tk.Entry(root, font=("Segoe UI", 12), width=30, bd=2,
                                   bg="#e0f7fa", fg="#00695c")
        self.task_input.pack(pady=10)

        # Buttons frame
        btns = tk.Frame(root, bg="#fefae0")
        btns.pack(pady=10)

        self.make_button(btns, "➕ Add", "#bbf7d0", "#065f46", self.add_task, 0)
        self.make_button(btns, "❌ Delete", "#fecaca", "#7f1d1d", self.delete_task, 1)
        self.make_button(btns, "✅ Mark Done", "#bae6fd", "#1e3a8a", self.mark_done, 2)

        # Footer
        tk.Label(root, text="✨ Created by Raghav Rana | Internship Task", font=("Arial", 9),
                 bg="#fefae0", fg="#888").pack(pady=15)

    def make_button(self, parent, text, bg, fg, command, col):
        btn = tk.Button(parent, text=text, font=("Segoe UI", 10, "bold"), width=12,
                        bg=bg, fg=fg, bd=0, activebackground=fg, activeforeground="white",
                        command=command, cursor="hand2")
        btn.grid(row=0, column=col, padx=6)

        # Add hover effect
        btn.bind("<Enter>", lambda e: btn.config(bg=fg, fg="white"))
        btn.bind("<Leave>", lambda e: btn.config(bg=bg, fg=fg))

    # Add new task
    def add_task(self):
        task = self.task_input.get().strip()
        if task:
            self.tasks.append(task)
            self.listbox.insert(tk.END, f"📌 {task}")
            self.task_input.delete(0, tk.END)
        else:
            messagebox.showwarning("Wait!", "Please type something to add.")

    # Delete selected task
    def delete_task(self):
        selected = self.listbox.curselection()
        if selected:
            idx = selected[0]
            self.listbox.delete(idx)
            self.tasks.pop(idx)
        else:
            messagebox.showinfo("Tip", "Select a task to delete it!")

    # Mark selected task as done
    def mark_done(self):
        selected = self.listbox.curselection()
        if selected:
            idx = selected[0]
            task = self.tasks[idx]
            if "✔" not in task:
                updated = f"{task} ✔"
                self.tasks[idx] = updated
                self.listbox.delete(idx)
                self.listbox.insert(idx, f"✅ {updated}")
        else:
            messagebox.showinfo("Tip", "Click a task to mark it done!")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop() 
    
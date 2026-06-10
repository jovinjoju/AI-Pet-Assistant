import tkinter as tk

class PetUI:
    def __init__(self, handle_command):
        self.root = tk.Tk()
        self.root.title("AI Pet")
        self.root.geometry("350x400")

        self.label = tk.Label(self.root, text="😊", font=("Arial", 80))
        self.label.pack()

        self.status = tk.Label(self.root, text="Idle")
        self.status.pack()

        self.entry = tk.Entry(self.root, width=30)
        self.entry.pack(pady=10)

        self.button = tk.Button(self.root, text="Send", command=self.send_command)
        self.button.pack()

        self.handle_command = handle_command

    # ✅ ADD THESE FUNCTIONS PROPERLY
    def hide_pet(self):
        self.root.withdraw()

    def show_pet(self):
        self.root.deiconify()

    def send_command(self):
        command = self.entry.get()
        self.entry.delete(0, tk.END)
        self.handle_command(command)

    def update_emotion(self, emotion):
        emojis = {
            "happy": "😊",
            "sleepy": "😴",
            "excited": "🤩",
            "angry": "😡"
        }
        self.label.config(text=emojis.get(emotion, "🙂"))

    def update_status(self, text):
        self.status.config(text=text)

    def run(self):
        self.root.mainloop()
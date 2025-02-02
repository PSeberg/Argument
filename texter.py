pip install tk

texts = [
    {
        "title": "Text 1",
        "content": """Här är en argumenterande text där författaren diskuterar fördelarna med att använda mobiltelefoner i skolan. Tes: Mobiltelefoner är användbara i skolan för att underlätta lärandet. Sakargument: De gör det lättare att få information snabbt. Känsloargument: Det känns bra att kunna kommunicera med föräldrar och vänner även under lektionerna. Motargument: Mobiltelefoner kan vara distraherande. Skribentens yrke: En lärare nämns i slutet av texten.""",
        "answers": {
            "tes": "Mobiltelefoner är användbara i skolan för att underlätta lärandet.",
            "sakargument": "De gör det lättare att få information snabbt.",
            "känsloargument": "Det känns bra att kunna kommunicera med föräldrar och vänner.",
            "motargument": "Mobiltelefoner kan vara distraherande.",
            "yrke": "En lärare nämns i slutet av texten."
        }
    },
    # Lägg till fler texter här enligt samma struktur
]

import tkinter as tk
from tkinter import messagebox

class TextAnalyzerApp:
    def __init__(self, root, texts):
        self.root = root
        self.texts = texts
        self.current_text = 0  # Håller reda på vilken text som visas
        self.selected_answers = {
            "tes": None,
            "sakargument": None,
            "känsloargument": None,
            "motargument": None,
            "yrke": None
        }
        self.create_widgets()

    def create_widgets(self):
        self.text_label = tk.Label(self.root, text=self.texts[self.current_text]["content"], justify="left", wraplength=500)
        self.text_label.pack(pady=10)

        self.choices_frame = tk.Frame(self.root)
        self.choices_frame.pack(pady=10)

        # Knappar för varje alternativ
        self.create_choice_button("tes", "Tes", self.texts[self.current_text]["answers"]["tes"])
        self.create_choice_button("sakargument", "Sakargument", self.texts[self.current_text]["answers"]["sakargument"])
        self.create_choice_button("känsloargument", "Känsloargument", self.texts[self.current_text]["answers"]["känsloargument"])
        self.create_choice_button("motargument", "Motargument", self.texts[self.current_text]["answers"]["motargument"])
        self.create_choice_button("yrke", "Yrke", self.texts[self.current_text]["answers"]["yrke"])

        # Knapp för att få feedback
        self.feedback_button = tk.Button(self.root, text="Kontrollera val", command=self.show_feedback)
        self.feedback_button.pack(pady=10)

    def create_choice_button(self, label, option_name, correct_answer):
        button = tk.Button(self.choices_frame, text=option_name, command=lambda: self.select_option(label, correct_answer))
        button.pack(side="left", padx=5)

    def select_option(self, label, correct_answer):
        self.selected_answers[label] = correct_answer
        print(f"{label} selected: {correct_answer}")  # Debug-utskrift

    def show_feedback(self):
        feedback = ""
        for key, value in self.selected_answers.items():
            if value == self.texts[self.current_text]["answers"][key]:
                feedback += f"{key.capitalize()} rätt!\n"
            else:
                feedback += f"{key.capitalize()} fel!\n"
        
        messagebox.showinfo("Feedback", feedback)

        # Nästa steg: välj om användaren vill fortsätta till nästa text eller göra om
        next_buttons = tk.Frame(self.root)
        next_buttons.pack(pady=10)

        next_button = tk.Button(next_buttons, text="Nästa text", command=self.next_text)
        next_button.pack(side="left", padx=5)

        retry_button = tk.Button(next_buttons, text="Gör om text", command=self.retry_text)
        retry_button.pack(side="left", padx=5)

    def next_text(self):
        self.current_text += 1
        if self.current_text < len(self.texts):
            self.update_text()
        else:
            messagebox.showinfo("Slut", "Du har slutfört alla texter!")
            self.root.quit()

    def retry_text(self):
        self.selected_answers = {key: None for key in self.selected_answers}
        self.update_text()

    def update_text(self):
        self.text_label.config(text=self.texts[self.current_text]["content"])
        for widget in self.choices_frame.winfo_children():
            widget.destroy()
        self.create_widgets()

def main():
    root = tk.Tk()
    root.title("Argumentationsanalys")
    app = TextAnalyzerApp(root, texts)
    root.mainloop()

if __name__ == "__main__":
    main()

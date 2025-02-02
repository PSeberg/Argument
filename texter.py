pip install flask

from flask import Flask, render_template, request

app = Flask(__name__)

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
    # More texts can be added here
]

@app.route('/')
def index():
    return render_template('index.html', texts=texts)

@app.route('/check', methods=['POST'])
def check_answers():
    selected_answers = request.form
    feedback = []

    # Check if the selected answers are correct
    for key, selected in selected_answers.items():
        correct_answer = texts[0]["answers"].get(key)
        feedback.append(f"{key.capitalize()}: {'Correct' if selected == correct_answer else 'Incorrect'}")

    return render_template('feedback.html', feedback=feedback)

if __name__ == "__main__":
    app.run(debug=True)

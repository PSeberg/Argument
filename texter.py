import streamlit as st

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
]

def get_user_input():
    st.title(texts[0]["title"])
    st.write(texts[0]["content"])

    tes = st.text_input("What is the thesis (tes)?")
    sakargument = st.text_input("What is the factual argument (sakargument)?")
    känsloargument = st.text_input("What is the emotional argument (känsloargument)?")
    motargument = st.text_input("What is the counter-argument (motargument)?")
    yrke = st.text_input("What is the profession mentioned (yrke)?")

    if st.button('Submit'):
        feedback = ""
        feedback += f"Tes: {'Correct' if tes == texts[0]['answers']['tes'] else 'Incorrect'}\n"
        feedback += f"Sakargument: {'Correct' if sakargument == texts[0]['answers']['sakargument'] else 'Incorrect'}\n"
        feedback += f"Känsloargument: {'Correct' if känsloargument == texts[0]['answers']['känsloargument'] else 'Incorrect'}\n"
        feedback += f"Motargument: {'Correct' if motargument == texts[0]['answers']['motargument'] else 'Incorrect'}\n"
        feedback += f"Yrke: {'Correct' if yrke == texts[0]['answers']['yrke'] else 'Incorrect'}\n"

        st.text(feedback)

if __name__ == "__main__":
    get_user_input()

import streamlit as st
import random

# Nya texter
texts = [
    {
        "title": "Inför mobilförbud i skolan",
        "content": """I dagens samhälle är mobiltelefoner en självklar del av ungdomars vardag...""",
        "answers": {
            "tes": "Mobiltelefoner stör undervisningen och bör förbjudas i skolan.",
            "sakargument": "Studier visar att elever som inte använder mobiltelefoner under lektionstid presterar bättre.",
            "känsloargument": "Lärare får ständigt tjata på elever att lägga undan telefonerna, vilket tar tid och energi från undervisningen.",
            "motargument": "Vissa menar att mobiltelefoner kan användas som hjälpmedel i undervisningen, till exempel för att slå upp fakta."
        }
    },
    {
        "title": "Obligatorisk idrott varje dag i skolan",
        "content": """Allt fler unga lever ett stillasittande liv...""",
        "answers": {
            "tes": "Elever bör ha idrott varje dag för att förbättra hälsa och inlärning.",
            "sakargument": "Studier visar att fysisk aktivitet förbättrar koncentration och minne.",
            "känsloargument": "En kort idrottslektion mitt på dagen skulle ge en chans att släppa pressen, röra på sig och må bättre.",
            "motargument": "En del menar att vissa elever inte gillar idrott och att det därför inte bör vara obligatoriskt varje dag."
        }
    }
]

# Hämta nuvarande index från session_state
if "index" not in st.session_state:
    st.session_state.index = 0

text = texts[st.session_state.index]

st.title(text["title"])
st.write(text["content"])

# Funktion för att skapa svarsalternativ en gång per text
def initialize_options():
    if "options" not in st.session_state or st.session_state.text_id != st.session_state.index:
        st.session_state.text_id = st.session_state.index
        st.session_state.options = {}

        for key in text["answers"]:
            correct_answer = text["answers"][key]
            options = list(text["answers"].values())  # Hämta alla svar
            options.remove(correct_answer)  # Ta bort det korrekta svaret
            wrong_answers = random.sample(options, 2)  # Välj två slumpmässiga felaktiga svar
            final_options = [correct_answer] + wrong_answers  # Skapa lista med tre alternativ
            random.shuffle(final_options)
            st.session_state.options[key] = final_options  # Spara i session_state

# Kör funktionen för att säkerställa att alternativen är fasta
initialize_options()

# Skapa svarsalternativ baserade på den aktuella texten
selected_tes = st.radio("Välj tes:", st.session_state.options["tes"], key="tes")
selected_sakargument = st.radio("Välj sakargument:", st.session_state.options["sakargument"], key="sakargument")
selected_kansloargument = st.radio("Välj känsloargument:", st.session_state.options["känsloargument"], key="känsloargument")
selected_motargument = st.radio("Välj motargument:", st.session_state.options["motargument"], key="motargument")

if st.button("Kontrollera svar"):
    correct = sum([
        selected_tes == text["answers"]["tes"],
        selected_sakargument == text["answers"]["sakargument"],
        selected_kansloargument == text["answers"]["känsloargument"],
        selected_motargument == text["answers"]["motargument"]
    ])
    st.write(f"Du fick {correct}/4 rätt.")
    if correct == 4:
        st.success("Bra jobbat!")
    else:
        st.warning("Försök igen.")

if st.button("Försök igen"):
    st.experimental_rerun()

if st.button("Fortsätt till nästa text"):
    st.session_state.index = (st.session_state.index + 1) % len(texts)  # Gå till nästa text
    st.session_state.options = {}  # Återställ alternativen
    st.experimental_rerun()

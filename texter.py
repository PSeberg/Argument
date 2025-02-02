import streamlit as st
import random

# Nya texter
texts = [
    {
        "title": "Inför mobilförbud i skolan",
        "content": "I dagens samhälle är mobiltelefoner en självklar del av ungdomars vardag. De används för att hålla kontakten med vänner, spela spel och surfa på sociala medier. Men i klassrummet blir de ofta en distraktion. Trots att vissa argumenterar för att mobiler kan vara ett hjälpmedel i skolan, är nackdelarna betydligt fler än fördelarna.",
        "answers": {
            "tes": "Mobiltelefoner stör undervisningen och bör förbjudas i skolan.",
            "sakargument": "Studier visar att elever som inte använder mobiltelefoner under lektionstid presterar bättre.",
            "känsloargument": "Föreställ dig en elev som kämpar med att hänga med på lektionen, men istället lockas av ett nytt meddelande som plingar till i mobilen.",
            "motargument": "Vissa menar att mobiltelefoner kan användas som hjälpmedel i undervisningen."
        }
    },
    {
        "title": "Obligatorisk idrott varje dag i skolan",
        "content": "Allt fler unga lever ett stillasittande liv. Skärmtid ersätter fysisk aktivitet och många rör sig för lite. Samtidigt visar forskning att träning förbättrar både fysisk och mental hälsa.",
        "answers": {
            "tes": "Elever bör ha idrott varje dag för att förbättra hälsa och inlärning.",
            "sakargument": "Studier visar att fysisk aktivitet förbättrar koncentration och minne.",
            "känsloargument": "Tänk dig en elev som är stressad över prov och läxor. En kort idrottslektion mitt på dagen skulle ge en chans att släppa pressen.",
            "motargument": "En del menar att vissa elever inte gillar idrott och att det därför inte bör vara obligatoriskt varje dag."
        }
    },
    {
        "title": "Inför gratis kollektivtrafik för unga",
        "content": "Många ungdomar är beroende av kollektivtrafik för att ta sig till skolan, fritidsaktiviteter och vänner. Men för många familjer är det en stor kostnad att köpa månadskort.",
        "answers": {
            "tes": "Ungdomar ska ha rätt till gratis kollektivtrafik för att öka frihet och jämlikhet.",
            "sakargument": "I flera städer, som exempelvis Luxemburg, har man infört gratis kollektivtrafik och sett positiva effekter.",
            "känsloargument": "Tänk dig en elev som vill gå på en fotbollsträning eller besöka en vän, men inte har råd med bussen.",
            "motargument": "En del säger att gratis kollektivtrafik skulle bli för dyrt."
        }
    },
    {
        "title": "Skoluniform bör införas i svenska skolor",
        "content": "Varje dag möts ungdomar av pressen att ha rätt kläder. Märkeskläder och trender skapar en orättvis hierarki i skolan.",
        "answers": {
            "tes": "Skoluniform minskar klädhets och skapar en mer jämlik skola.",
            "sakargument": "En studie från University of Nevada visar att skoluniform kan förbättra sammanhållning och minska klädpressen.",
            "känsloargument": "Tänk dig en elev som blir retad för sina kläder eftersom de inte är 'rätt märke'.",
            "motargument": "Många hävdar att skoluniform tar bort elevernas möjlighet att uttrycka sin stil."
        }
    },
    {
        "title": "Skoldagar bör starta senare",
        "content": "Många ungdomar är trötta på morgnarna och har svårt att koncentrera sig under första lektionen. Forskning visar att tonåringar behöver mer sömn, men skolor börjar för tidigt.",
        "answers": {
            "tes": "Skoldagar bör börja senare för att passa tonåringars biologiska sömnbehov.",
            "sakargument": "Forskning från Harvard visar att elever som får börja skolan senare har bättre betyg och mår bättre.",
            "känsloargument": "Tänk dig att du måste vakna klockan sex varje morgon, trots att din kropp egentligen behöver sova längre.",
            "motargument": "Vissa säger att skoldagar då blir längre, men det kan lösas genom att minska onödiga håltimmar."
        }
    }
]

# Hämta nuvarande index från session_state
if "index" not in st.session_state:
    st.session_state.index = 0

text = texts[st.session_state.index]
st.title(text["title"])
st.write(text["content"])

# Funktion för att skapa svarsalternativ
all_answers = [t["answers"] for t in texts]
def get_options(correct_answer, key):
    options = [correct_answer]
    while len(options) < 3:
        option = random.choice(all_answers)[key]
        if option not in options:
            options.append(option)
    random.shuffle(options)
    return options

# Skapa svarsalternativ
selected_tes = st.radio("Välj tes:", get_options(text["answers"]["tes"], "tes"))
selected_sakargument = st.radio("Välj sakargument:", get_options(text["answers"]["sakargument"], "sakargument"))
selected_kansloargument = st.radio("Välj känsloargument:", get_options(text["answers"]["känsloargument"], "känsloargument"))
selected_motargument = st.radio("Välj motargument:", get_options(text["answers"]["motargument"], "motargument"))

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
        st.session_state.index = (st.session_state.index + 1) % len(texts)
        st.experimental_rerun()

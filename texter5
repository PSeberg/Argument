import streamlit as st
import random

# Argumenterande texter med svarsalternativ
texts = [
    {
        "title": "Inför mobilförbud i skolan",
        "content": """
I dagens samhälle är mobiltelefoner en självklar del av ungdomars vardag... (texten fortsätter)
""",
        "answers": {
            "tes": "Mobiltelefoner stör undervisningen och bör förbjudas i skolan.",
            "sakargument": "Studier visar att elever som inte använder mobiltelefoner under lektionstid presterar bättre.",
            "känsloargument": "Lärare får ständigt tjata på elever att lägga undan telefonerna, vilket tar tid och energi från undervisningen.",
            "motargument": "Vissa menar att mobiltelefoner kan användas som hjälpmedel i undervisningen, till exempel för att slå upp fakta."
        }
    },
    {
        "title": "Obligatorisk idrott varje dag i skolan",
        "content": """
Allt fler unga lever ett stillasittande liv... (texten fortsätter)
""",
        "answers": {
            "tes": "Elever bör ha idrott varje dag för att förbättra hälsa och inlärning.",
            "sakargument": "Studier visar att fysisk aktivitet förbättrar koncentration och minne.",
            "känsloargument": "En kort idrottslektion mitt på dagen skulle ge en chans att släppa pressen, röra på sig och må bättre.",
            "motargument": "En del menar att vissa elever inte gillar idrott och att det därför inte bör vara obligatoriskt varje dag."
        }
    },
    {
        "title": "Förläng skoldagarna för bättre inlärning",
        "content": """
Skolan är en plats för lärande, men trots det har många elever svårt att hinna med allt som krävs... (texten fortsätter)
""",
        "answers": {
            "tes": "Skoldagar bör förlängas för att förbättra inlärning och minska stress.",
            "sakargument": "Enligt en studie från Skolverket presterar elever i länder med längre skoldagar bättre på internationella kunskapstester.",
            "känsloargument": "Istället för att stressa igenom nya kapitel skulle elever få tid att verkligen förstå innehållet.",
            "motargument": "Motståndare till längre skoldagar menar att elever behöver fritid och återhämtning."
        }
    },
    {
        "title": "Gratis kollektivtrafik för ungdomar",
        "content": """
Varje dag tar hundratusentals ungdomar bussen eller tåget till skolan, träningen eller vänner... (texten fortsätter)
""",
        "answers": {
            "tes": "Kollektivtrafiken bör vara gratis för ungdomar.",
            "sakargument": "I Estlands huvudstad Tallinn, där kollektivtrafiken varit avgiftsfri sedan 2013, har biltrafiken minskat och fler väljer att åka buss eller spårvagn.",
            "känsloargument": "Föreställ dig en värld där ingen ungdom behöver oroa sig för biljettpriser eller krångliga resekort.",
            "motargument": "Vissa argumenterar för att fri kollektivtrafik skulle bli dyrt och att skattepengar kan användas bättre."
        }
    },
    {
        "title": "Förbjud energidrycker för ungdomar",
        "content": """
Energidrycker marknadsförs som något coolt och uppiggande, men bakom de färgglada burkarna döljer sig allvarliga hälsorisker... (texten fortsätter)
""",
        "answers": {
            "tes": "Energidrycker bör förbjudas för personer under 18 år.",
            "sakargument": "En rapport från Livsmedelsverket varnar för att energidrycker kan leda till hjärtklappning och högt blodtryck, särskilt för ungdomar.",
            "känsloargument": "Tänk dig en elev som dricker en energidryck för att orka koncentrera sig i skolan. Till en början känner hen sig pigg, men efter en stund kommer tröttheten och huvudvärken.",
            "motargument": "En del menar att det borde vara upp till individen att välja om man vill dricka energidrycker eller inte."
        }
    }
]

# Initialisera session_state
if "index" not in st.session_state:
    st.session_state.index = 0
    st.session_state.score = 0

# Visa aktuell text
if st.session_state.index < len(texts):
    current_text = texts[st.session_state.index]
    st.title(current_text["title"])
    st.write(current_text["content"])
    
    selected_option = st.radio("Vilket påstående beskriver vad argumentet är?", list(current_text["answers"].keys()))
    
    if st.button("Nästa text"):
        if selected_option and selected_option == current_text["answers"][selected_option]:
            st.session_state.score += 1  # Räkna poäng
        st.session_state.index += 1
        st.experimental_rerun()
else:
    st.title("Programmet är slut!")
    st.write(f"Ditt totala resultat blev: {st.session_state.score}/{len(texts)} poäng.")
    if st.button("Börja om"):
        st.session_state.index = 0
        st.session_state.score = 0
        st.experimental_rerun()

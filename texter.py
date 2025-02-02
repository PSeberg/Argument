import streamlit as st
import random

# Exempeltexter med rubriker kopplade till teserna och textstruktur utan markeringar
texts = [
    {
        "title": "Mobiltelefoner i skolan: En hjälp eller en fara?",
        "content": """Under de senaste åren har mobiltelefoner blivit allt vanligare i svenska skolor...""",
        "answers": {
            "tes": "Mobiltelefoner är användbara i skolan för att underlätta lärandet.",
            "sakargument": "Elever kan snabbt slå upp information på nätet, vilket gör att de kan arbeta snabbare och mer effektivt.",
            "känsloargument": "Det är viktigt för elever att ha mobiltelefoner i skolan av säkerhetsskäl.",
            "motargument": "Mobiltelefoner kan vara distraherande och påverka koncentrationen negativt."
        }
    },
    {
        "title": "Klimatförändringar: Vad kan vi göra för att stoppa dem?",
        "content": """Klimatförändringarna är ett av de största hoten mot vår planet...""",
        "answers": {
            "tes": "Människans aktivitet påverkar klimatet och vi måste agera nu för att stoppa klimatförändringar.",
            "sakargument": "Genom att minska utsläppen av växthusgaser kan vi bromsa uppvärmningen av planeten.",
            "känsloargument": "För många handlar det om att säkra en framtid för kommande generationer.",
            "motargument": "Klimatförändringar är en naturlig cykel och inte orsakad av människan."
        }
    },
    {
        "title": "Skoluniform: En lösning på mobbning?",
        "content": """Mobbning är ett stort problem i många skolor, och för att minska mobbning har vissa föreslagit...""",
        "answers": {
            "tes": "Skoluniformer kan minska mobbning genom att minska skillnader mellan elever.",
            "sakargument": "Skoluniformen skapar en mer jämlik miljö, där elever inte kan skilja sig åt genom sina kläder.",
            "känsloargument": "Att inte kunna välja sina egna kläder kan upplevas som ett hot mot deras personliga frihet.",
            "motargument": "Mobbning kan fortfarande förekomma på andra sätt, som genom kommentarer om utseende eller prestation."
        }
    }
]

# Funktion för att blanda svarsalternativ
def generate_options(correct_answer, all_answers):
    incorrect_answers = random.sample([a for a in all_answers if a != correct_answer], 2)
    options = [correct_answer] + incorrect_answers
    random.shuffle(options)
    return options

# Hämta nuvarande index från session_state
if "index" not in st.session_state:
    st.session_state.index = 0

text = texts[st.session_state.index]
st.title(text["title"])
st.write(text["content"])

all_tes = [t["answers"]["tes"] for t in texts]
all_sakargument = [t["answers"]["sakargument"] for t in texts]
all_kansloargument = [t["answers"]["känsloargument"] for t in texts]
all_motargument = [t["answers"]["motargument"] for t in texts]

selected_tes = st.radio("Välj tes:", options=generate_options(text["answers"]["tes"], all_tes))
selected_sakargument = st.radio("Välj sakargument:", options=generate_options(text["answers"]["sakargument"], all_sakargument))
selected_kansloargument = st.radio("Välj känsloargument:", options=generate_options(text["answers"]["känsloargument"], all_kansloargument))
selected_motargument = st.radio("Välj motargument:", options=generate_options(text["answers"]["motargument"], all_motargument))

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
        st.warning("Försök igen eller gå vidare.")

    if st.button("Gör om denna text"):
        st.rerun()
    
    if st.button("Fortsätt till nästa text"):
        if st.session_state.index < len(texts) - 1:
            st.session_state.index += 1
            st.rerun()
        else:
            st.write("Du har gått igenom alla texter!")

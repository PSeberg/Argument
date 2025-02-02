import streamlit as st
import random

# Nya texter
texts = [
    {
        "title": "Inför mobilförbud i skolan",
        "content": """
I dagens samhälle är mobiltelefoner en självklar del av ungdomars vardag. De används för att hålla kontakten med vänner, spela spel och surfa på sociala medier. Men i klassrummet blir de ofta en distraktion. Trots att vissa argumenterar för att mobiler kan vara ett hjälpmedel i skolan, är nackdelarna betydligt fler än fördelarna.

Föreställ dig en elev som kämpar med att hänga med på lektionen, men istället lockas av ett nytt meddelande som plingar till i mobilen. Hur ska hen kunna fokusera? Lärare får ständigt tjata på elever att lägga undan telefonerna, vilket tar tid och energi från undervisningen. Det är frustrerande både för lärare och de elever som faktiskt vill lära sig något.

Studier visar att elever som inte använder mobiltelefoner under lektionstid presterar bättre. En rapport från OECD har visat att länder med strikta regler kring mobilanvändning i skolan har högre genomsnittliga betyg. Genom att förbjuda mobiler skapar vi en bättre studiemiljö där alla får en chans att koncentrera sig.

Vissa menar att mobiltelefoner kan användas som hjälpmedel i undervisningen, till exempel för att slå upp fakta. Men faktum är att det redan finns datorer och läroböcker som fyller den funktionen. Dessutom kan skolan erbjuda surfplattor vid behov, utan att det leder till samma distraktioner som mobiltelefoner.

Att införa ett mobilförbud i skolan är en självklar lösning för att förbättra studiemiljön. Elever blir mer fokuserade, lärarna får en bättre arbetsmiljö och alla får ut mer av lektionerna. Det är dags att vi prioriterar utbildning framför skärmtid.
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
Allt fler unga lever ett stillasittande liv. Skärmtid ersätter fysisk aktivitet och många rör sig för lite. Samtidigt visar forskning att träning förbättrar både fysisk och mental hälsa. Ändå har många skolor bara idrott ett par gånger i veckan. Detta måste förändras – elever bör ha idrott varje dag!

Tänk dig en elev som är stressad över prov och läxor. En kort idrottslektion mitt på dagen skulle ge en chans att släppa pressen, röra på sig och må bättre. Idrott är inte bara träning för kroppen – det är också ett sätt att hantera stress och må bra mentalt.

Studier visar att fysisk aktivitet förbättrar koncentration och minne. Enligt en rapport från Karolinska Institutet presterar elever bättre i skolan när de rör sig regelbundet. Dessutom minskar risken för övervikt och livsstilssjukdomar om unga tränar varje dag.

En del menar att vissa elever inte gillar idrott och att det därför inte bör vara obligatoriskt varje dag. Men idrott handlar inte bara om tävling och prestation – det kan vara yoga, promenader eller dans. Det viktigaste är att röra på sig, och skolan bör erbjuda varierad träning som passar alla.

Att införa daglig idrott i skolan är en investering i elevernas hälsa och framtid. Genom att röra sig varje dag blir vi piggare, mår bättre och presterar bättre i skolan.
""",
        "answers": {
            "tes": "Elever bör ha idrott varje dag för att förbättra hälsa och inlärning.",
            "sakargument": "Studier visar att fysisk aktivitet förbättrar koncentration och minne.",
            "känsloargument": "En kort idrottslektion mitt på dagen skulle ge en chans att släppa pressen, röra på sig och må bättre.",
            "motargument": "En del menar att vissa elever inte gillar idrott och att det därför inte bör vara obligatoriskt varje dag."
        }
    }
]

# Spara nuvarande index och total poäng
if "index" not in st.session_state:
    st.session_state.index = 0
if "total_score" not in st.session_state:
    st.session_state.total_score = 0

# Om vi har gått igenom alla texter, visa slutsidan
if st.session_state.index >= len(texts):
    st.title("Grattis, du har slutfört programmet!")
    st.write(f"Din totala poäng: **{st.session_state.total_score}/{len(texts) * 4}**")
    st.write("Tack för att du deltog! 🎉")
    st.stop()  # Stoppar programmet här

# Annars, hämta aktuell text
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
    st.session_state.total_score += correct  # Lägg till poäng
    st.write(f"Du fick {correct}/4 rätt.")
    if correct == 4:
        st.success("Bra jobbat!")
    else:
        st.warning("Försök igen.")

if st.button("Fortsätt till nästa text"):
    st.session_state.index += 1
    st.rerun()

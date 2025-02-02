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
            "känsloargument": "Föreställ dig en elev som kämpar med att hänga med på lektionen, men istället lockas av ett nytt meddelande som plingar till i mobilen.",
            "motargument": "Vissa menar att mobiltelefoner kan användas som hjälpmedel i undervisningen."
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
            "känsloargument": "Tänk dig en elev som är stressad över prov och läxor. En kort idrottslektion mitt på dagen skulle ge en chans att släppa pressen.",
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

# Skapa svarsalternativ baserade på den aktuella texten
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


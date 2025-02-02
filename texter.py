import streamlit as st

# Exempeltexter med rubriker kopplade till teserna och textstruktur utan markeringar
texts = [
    {
        "title": "Mobiltelefoner i skolan: En hjälp eller en fara?",
        "content": """Under de senaste åren har mobiltelefoner blivit allt vanligare i svenska skolor. Medan vissa hävdar att mobiltelefoner kan vara till stor nytta för elever, finns det andra som menar att de skapar distraktioner och stör lärandet. För att förstå om mobiltelefoner verkligen är en hjälp eller en fara i skolmiljön måste vi överväga båda sidor av argumentet.

        För det första finns det de som anser att mobiltelefoner är ett kraftfullt verktyg för lärande. Elever kan snabbt slå upp information på nätet, vilket gör att de kan arbeta snabbare och mer effektivt. Dessutom kan mobiltelefoner användas för att ta anteckningar, lyssna på lärande-appar eller kommunicera med lärare och klasskamrater. På detta sätt kan mobiltelefoner bidra till att förbättra elevernas engagemang och interaktivitet i lärandeprocessen.

        Samtidigt måste vi ta hänsyn till de negativa effekterna som mobiltelefoner kan ha i klassrummet. Många elever använder sina telefoner för att chatta, titta på sociala medier eller spela spel under lektionerna, vilket kan påverka deras koncentration och lärande. Detta är ett problem som inte kan ignoreras, och därför bör det finnas striktare regler för användning av mobiltelefoner i skolan.

        Det finns också de som anser att det är viktigt för elever att ha mobiltelefoner i skolan av säkerhetsskäl. I en värld där oroligheter kan uppstå, kan mobiltelefoner ge eleverna en möjlighet att snabbt få kontakt med sina föräldrar eller vänner i händelse av en nödsituation. Detta känslomässiga argument belyser vikten av att känna sig trygg och säker.

        Avslutningsvis är det uppenbart att mobiltelefoner både har fördelar och nackdelar i skolmiljön. Det bästa är kanske att finna en balans, där mobiltelefoner får användas för lärande och säkerhet, men att strikta regler införs för att förhindra distraktioner. Med rätt balans kan mobiltelefoner vara en tillgång snarare än en nackdel i skolan."""
        ,
        "answers": {
            "tes": "Mobiltelefoner är användbara i skolan för att underlätta lärandet.",
            "sakargument": "Elever kan snabbt slå upp information på nätet, vilket gör att de kan arbeta snabbare och mer effektivt.",
            "känsloargument": "Det är viktigt för elever att ha mobiltelefoner i skolan av säkerhetsskäl.",
            "motargument": "Mobiltelefoner kan vara distraherande och påverka koncentrationen negativt.",
            "yrke": "En lärare nämns i slutet av texten."
        }
    },
    {
        "title": "Klimatförändringar: Vad kan vi göra för att stoppa dem?",
        "content": """Klimatförändringarna är ett av de största hoten mot vår planet. Med stigande temperaturer, smältande isar och extremväder som blir allt vanligare, är det tydligt att något måste göras. Frågan är dock: Vad kan vi egentligen göra för att stoppa dem?

        Ett av de starkaste argumenten för att bekämpa klimatförändringarna är att människans aktivitet, särskilt fossila bränslen, har en direkt påverkan på jordens klimat. Genom att minska utsläppen av växthusgaser, till exempel genom att använda mer förnybar energi och minska biltrafik, kan vi bromsa uppvärmningen av planeten. För att skydda våra resurser och framtida generationer är det avgörande att alla gör sin del.

        Å andra sidan finns det de som menar att klimatförändringar är en naturlig cykel och inte i första hand orsakade av människan. Vissa hävdar att klimatet alltid har förändrats över tid och att de förändringar vi ser idag inte är ovanliga. Dessa åsikter ifrågasätter behovet av drastiska åtgärder och förespråkar mer måttliga lösningar.

        Känslomässigt är klimatförändringar en skrämmande tanke för många, särskilt för unga människor som kan känna sig maktlösa inför denna globala utmaning. För många handlar det om att säkra en framtid för kommande generationer, vilket gör att klimatfrågan känns väldigt personlig och viktig.

        I slutändan är det avgörande att vi som samhälle agerar nu. Fördröjning kan få förödande konsekvenser, och det är upp till oss att fatta beslut som skyddar vår planet för framtida generationer."""
        ,
        "answers": {
            "tes": "Människans aktivitet påverkar klimatet och vi måste agera nu för att stoppa klimatförändringar.",
            "sakargument": "Genom att minska utsläppen av växthusgaser kan vi bromsa uppvärmningen av planeten.",
            "känsloargument": "För många handlar det om att säkra en framtid för kommande generationer.",
            "motargument": "Klimatförändringar är en naturlig cykel och inte orsakad av människan.",
            "yrke": "En klimatforskare nämns i slutet av texten."
        }
    },
    {
        "title": "Skoluniform: En lösning på mobbning?",
        "content": """Mobbning är ett stort problem i många skolor, och för att minska mobbning har vissa föreslagit införandet av skoluniformer. Målet är att uniformerna ska minska skillnader mellan elever, vilket i sin tur skulle kunna minska mobbning. Men är skoluniformen verkligen lösningen?

        Förespråkarna av skoluniformer menar att uniformen skapar en mer jämlik miljö, där elever inte kan skilja sig åt genom sina kläder. Detta skulle kunna minska trycket på elever att ha de senaste kläderna och istället fokusera på sina studier. Dessutom kan det hjälpa till att bygga en känsla av sammanhållning och enhet inom skolan.

        Motståndarna hävdar att skoluniformer inte löser mobbningen utan snarare döljer problemet. Mobbning kan fortfarande förekomma på andra sätt, som genom kommentarer om utseende eller prestation. Dessutom menar de att elever ska få uttrycka sin personlighet genom sina kläder, och att skoluniformen skulle vara en begränsning av individens frihet.

        Känslomässigt kan tanken på en uniform kännas begränsande för vissa elever. Att inte kunna välja sina egna kläder kan upplevas som ett hot mot deras personliga frihet och kreativitet. Samtidigt kan det för vissa vara en lättnad att slippa tänka på vad man ska ha på sig varje dag.

        Sammanfattningsvis finns det både fördelar och nackdelar med skoluniformer. För vissa skolor och elever kan det vara en lösning på mobbning, medan det för andra inte löser grundproblemet. Det är en fråga som kräver noggrant övervägande."""
        ,
        "answers": {
            "tes": "Skoluniformer kan minska mobbning genom att minska skillnader mellan elever.",
            "sakargument": "Skoluniformen skapar en mer jämlik miljö, där elever inte kan skilja sig åt genom sina kläder.",
            "känsloargument": "Att inte kunna välja sina egna kläder kan upplevas som ett hot mot deras personliga frihet.",
            "motargument": "Mobbning kan fortfarande förekomma på andra sätt, som genom kommentarer om utseende eller prestation.",
            "yrke": "En skolkurator nämns i slutet av texten."
        }
    }
]

# Funktion för att visa text och val
def display_text_and_choices(text):
    st.title(text["title"])
    st.write(text["content"])

    # Skapa radioknappar för att välja rätt svar
    selected_tes = st.radio("Välj tes:", options=[
        text["answers"]["tes"],
        "Fel tes 1",
        "Fel tes 2"
    ])
    selected_sakargument = st.radio("Välj sakargument:", options=[
        text["answers"]["sakargument"],
        "Fel sakargument 1",
        "Fel sakargument 2"
    ])
    selected_kansloargument = st.radio("Välj känsloargument:", options=[
        text["answers"]["känsloargument"],
        "Fel känsloargument 1",
        "Fel känsloargument 2"
    ])
    selected_motargument = st.radio("Välj motargument:", options=[
        text["answers"]["motargument"],
        "Fel motargument 1",
        "Fel motargument 2"
    ])
    
    if st.button("Kontrollera svar"):
        # Kontrollera om svaren är korrekta och visa resultat
        correct = 0
        if selected_tes == text["answers"]["tes"]:
            correct += 1
        if selected_sakargument == text["answers"]["sakargument"]:
            correct += 1
        if selected_kansloargument == text["answers"]["känsloargument"]:
            correct += 1
        if selected_motargument == text["answers"]["motargument"]:
            correct += 1
        
        st.write(f"Du fick {correct}/4 rätt.")
        if correct == 4:
            st.success("Bra jobbat!")
        else:
            st.warning("Försök igen.")

    if st.button("Fortsätt till nästa text"):
        return True
    return False

# Huvudlogik för att visa texter
for text in texts:
    if display_text_and_choices(text):
        continue

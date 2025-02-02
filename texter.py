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
            "tes": "Mobiltelefoner i skolan: En hjälp eller en fara?",
            "sakargument": "Elever kan snabbt slå upp information på nätet, vilket gör att de kan arbeta snabbare och mer effektivt.",
            "känsloargument": "Det är viktigt för elever att ha mobiltelefoner i skolan av säkerhetsskäl.",
            "motargument": "Många elever använder sina telefoner för att chatta, titta på sociala medier eller spela spel under lektionerna, vilket kan påverka deras koncentration.",
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
            "tes": "Klimatförändringar: Vad kan vi göra för att stoppa dem?",
            "sakargument": "Genom att minska utsläppen av växthusgaser, till exempel genom att använda mer förnybar energi och minska biltrafik, kan vi bromsa uppvärmningen av planeten.",
            "känsloargument": "För många handlar det om att säkra en framtid för kommande generationer.",
            "motargument": "Vissa hävdar att klimatet alltid har förändrats över tid och att de förändringar vi ser idag inte är ovanliga.",
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
            "tes": "Skoluniform: En lösning på mobbning?",
            "sakargument": "Skoluniformen skapar en mer jämlik miljö, där elever inte kan skilja sig åt genom sina kläder.",
            "känsloargument": "Att inte kunna välja sina egna kläder kan upplevas som ett hot mot deras personliga frihet.",
            "motargument": "Mobbning kan fortfarande förekomma på andra sätt, som genom kommentarer om utseende eller prestation.",
            "yrke": "En skolkurator nämns i slutet av texten."
        }
    },
    {
        "title": "Sociala medier: En fara för ungas psykiska hälsa?",
        "content": """Sociala medier har blivit en stor del av ungas liv och påverkar hur de kommunicerar och interagerar med omvärlden. Men frågan är: Har sociala medier en negativ inverkan på ungas psykiska hälsa?

        För det första, det finns bevis på att överanvändning av sociala medier kan leda till en känsla av ensamhet och depression. Elever och unga människor som ständigt jämför sig med andras perfekta bilder och livsstilar på sociala medier kan känna sig otillräckliga och ha låg självkänsla. Det är ett problem som inte kan ignoreras.

        Å andra sidan finns det de som menar att sociala medier också har positiva effekter. Det kan ge unga människor en möjlighet att uttrycka sig och bygga gemenskaper med likasinnade. Dessutom kan det vara ett bra sätt att hålla kontakten med vänner och familj, särskilt om de bor långt bort.

        Känslomässigt är sociala medier ofta både en källa till glädje och oro. På en sida kan de skapa en känsla av gemenskap, men på den andra sidan kan de leda till en negativ självkänsla och ångest. För många ungdomar är sociala medier en konstant källa till stress och jämförelse.

        Slutligen måste vi som samhälle vara medvetna om hur sociala medier påverkar våra unga. Genom att erbjuda stöd och utbildning kan vi hjälpa unga människor att hantera sociala medier på ett hälsosamt sätt."""
        ,
        "answers": {
            "tes": "Sociala medier: En fara för ungas psykiska hälsa?",
            "sakargument": "Överanvändning av sociala medier kan leda till en känsla av ensamhet och depression.",
            "känsloargument": "Sociala medier är en konstant källa till stress och jämförelse.",
            "motargument": "Sociala medier kan ge unga människor en möjlighet att uttrycka sig och bygga gemenskaper med likasinnade.",
            "yrke": "En psykolog nämns i slutet av texten."
        }
    },
    {
        "title": "Djurförsök: Ett nödvändigt ont för vetenskapen?",
        "content": """Djurförsök har länge varit ett ämne för kontrovers. Forskare använder djurförsök för att testa nya läkemedel och behandlingar, men detta väcker moraliska frågor. Är djurförsök verkligen nödvändiga för vetenskapens framsteg, eller är det en etisk gräns vi inte borde korsa?

        Förespråkarna för djurförsök hävdar att de är avgörande för medicinska genombrott. Utan djurförsök skulle många livräddande behandlingar aldrig ha utvecklats. Djurförsök gör det möjligt att testa säkerheten hos nya läkemedel innan de används på människor, och de har spelat en stor roll i utvecklingen av vaccin och andra behandlingar.

        De som är emot djurförsök argumenterar att djur inte ska utsättas för lidande för människans nytta. De menar att moderna alternativa metoder, såsom datorer och 3D-utskrivning, kan ersätta djurförsök och ge likvärdiga resultat utan att orsaka lidande.

        Känslomässigt är det svårt att bortse från det lidande som djur genomgår under försök. För många människor känns det fel att använda levande varelser för vetenskapliga experiment, särskilt när alternativa metoder finns tillgängliga.

        Sammanfattningsvis är frågan om djurförsök är nödvändiga en etisk fråga som vi måste ta på största allvar. Det är viktigt att hitta en balans mellan vetenskapliga framsteg och djurens välfärd."""
        ,
        "answers": {
            "tes": "Djurförsök: Ett nödvändigt ont för vetenskapen?",
            "sakargument": "Djurförsök gör det möjligt att testa säkerheten hos nya läkemedel innan de används på människor.",
            "känsloargument": "Det känns fel att använda levande varelser för vetenskapliga experiment.",
            "motargument": "Moderna alternativa metoder, såsom datorer och 3D-utskrivning, kan ersätta djurförsök och ge likvärdiga resultat.",
            "yrke": "En forskare nämns i slutet av texten."
        }
    }
]

# Funktion för att visa text och val
def display_text_and_choices(text):
    st.title(text["title"])
    st.write(text["content"])

    # Skapa radioknappar för att välja rätt svar
    selected_tes = st.radio("Välj tes:", options=[text["answers"]["tes"], "Fel tes"])
    selected_sakargument = st.radio("Välj sakargument:", options=[text["answers"]["sakargument"], "Fel sakargument"])
    selected_känsloargument = st.radio("Välj känsloargument:", options=[text["answers"]["känsloargument"], "Fel känsloargument"])
    selected_motargument = st.radio("Välj motargument:", options=[text["answers"]["motargument"], "Fel motargument"])
    selected_yrke = st.radio("Välj yrke:", options=[text["answers"]["yrke"], "Fel yrke"])

    if st.button("Kontrollera svar"):
        feedback = []
        feedback.append(f"Tes: {'Correct' if selected_tes == text['answers']['tes'] else 'Incorrect'}")
        feedback.append(f"Sakargument: {'Correct' if selected_sakargument == text['answers']['sakargument'] else 'Incorrect'}")
        feedback.append(f"Känsloargument: {'Correct' if selected_känsloargument == text['answers']['känsloargument'] else 'Incorrect'}")
        feedback.append(f"Motargument: {'Correct' if selected_motargument == text['answers']['motargument'] else 'Incorrect'}")
        feedback.append(f"Yrke: {'Correct' if selected_yrke == text['answers']['yrke'] else 'Incorrect'}")

        for item in feedback:
            st.write(item)

# Visa varje text och skapa interaktiv feedback
if __name__ == "__main__":
    for text in texts:
        display_text_and_choices(text)

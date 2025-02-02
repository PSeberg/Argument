import streamlit as st
import random

# Exempeltexter med rubriker kopplade till teserna och textstruktur utan markeringar
texts = [
    {
        "title": "Mobiltelefoner i skolan: En hjälp eller en fara?",
        "content": "Under de senaste åren har mobiltelefoner blivit allt vanligare i svenska skolor. Medan vissa hävdar att mobiltelefoner kan vara till stor nytta för elever, finns det andra som menar att de skapar distraktioner och stör lärandet. För att förstå om mobiltelefoner verkligen är en hjälp eller en fara i skolmiljön måste vi överväga båda sidor av argumentet.\n\nFör det första finns det de som anser att mobiltelefoner är ett kraftfullt verktyg för lärande. Elever kan snabbt slå upp information på nätet, vilket gör att de kan arbeta snabbare och mer effektivt. Dessutom kan mobiltelefoner användas för att ta anteckningar, lyssna på lärande-appar eller kommunicera med lärare och klasskamrater. På detta sätt kan mobiltelefoner bidra till att förbättra elevernas engagemang och interaktivitet i lärandeprocessen.\n\nSamtidigt måste vi ta hänsyn till de negativa effekterna som mobiltelefoner kan ha i klassrummet. Många elever använder sina telefoner för att chatta, titta på sociala medier eller spela spel under lektionerna, vilket kan påverka deras koncentration och lärande. Detta är ett problem som inte kan ignoreras, och därför bör det finnas striktare regler för användning av mobiltelefoner i skolan.",
        "answers": {
            "tes": "Mobiltelefoner är användbara i skolan för att underlätta lärandet.",
            "sakargument": "Elever kan snabbt slå upp information på nätet, vilket gör att de kan arbeta snabbare och mer effektivt.",
            "känsloargument": "Det är viktigt för elever att ha mobiltelefoner i skolan av säkerhetsskäl.",
            "motargument": "Mobiltelefoner kan vara distraherande och påverka koncentrationen negativt."
        }
    },
    {
        "title": "Klimatförändringar: Vad kan vi göra för att stoppa dem?",
        "content": "Klimatförändringarna är ett av de största hoten mot vår planet. Med stigande temperaturer, smältande isar och extremväder som blir allt vanligare, är det tydligt att något måste göras. Frågan är dock: Vad kan vi egentligen göra för att stoppa dem?\n\nEtt av de starkaste argumenten för att bekämpa klimatförändringarna är att människans aktivitet, särskilt fossila bränslen, har en direkt påverkan på jordens klimat. Genom att minska utsläppen av växthusgaser, till exempel genom att använda mer förnybar energi och minska biltrafik, kan vi bromsa uppvärmningen av planeten. För att skydda våra resurser och framtida generationer är det avgörande att alla gör sin del.",
        "answers": {
            "tes": "Människans aktivitet påverkar klimatet och vi måste agera nu för att stoppa klimatförändringar.",
            "sakargument": "Genom att minska utsläppen av växthusgaser kan vi bromsa uppvärmningen av planeten.",
            "känsloargument": "För många handlar det om att säkra en framtid för kommande generationer.",
            "motargument": "Klimatförändringar är en naturlig cykel och inte orsakad av människan."
        }
    },
    {
        "title": "Skoluniform: En lösning på mobbning?",
        "content": "Mobbning är ett stort problem i många skolor, och för att minska mobbning har vissa föreslagit införandet av skoluniformer. Målet är att uniformerna ska minska skillnader mellan elever, vilket i sin tur skulle kunna minska mobbning. Men är skoluniformen verkligen lösningen?\n\nFörespråkarna av skoluniformer menar att uniformen skapar en mer jämlik miljö, där elever inte kan skilja sig åt genom sina kläder. Detta skulle kunna minska trycket på elever att ha de senaste kläderna och istället fokusera på sina studier. Dessutom kan det hjälpa till att bygga en känsla av sammanhållning och enhet inom skolan.",
        "answers": {
            "tes": "Skoluniformer kan minska mobbning genom att minska skillnader mellan elever.",
            "sakargument": "Skoluniformen skapar en mer jämlik miljö, där elever inte kan skilja sig åt genom sina kläder.",
            "känsloargument": "Att inte kunna välja sina egna kläder kan upplevas som ett hot mot deras personliga frihet.",
            "motargument": "Mobbning kan fortfarande förekomma på andra sätt, som genom kommentarer om utseende eller prestation."
        }
    }
]

# Hämta nuvarande index från session_state
if "index" not in st.session_state:
    st.session_state.index = 0

text = texts[st.session_state.index]
st.title(text["title"])
st.write(text["content"])
